import cv2
from datetime import datetime
import time
import os

# Buat folder log & screenshots jika belum ada
os.makedirs('screenshots', exist_ok=True)

# Load model deteksi wajah dari OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inisialisasi webcam
cap = cv2.VideoCapture(0)

# Timer untuk deteksi wajah hilang
last_seen = time.time()
face_missing_start = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 1. Deteksi lebih dari satu wajah
    if len(faces) > 1:
        msg = f"[{now}] Lebih dari satu wajah terdeteksi!"
        print(msg)
        with open("cheating_log.txt", "a") as log:
            log.write(msg + "\n")
        cv2.imwrite(f'screenshots/cheating_{datetime.now().strftime("%H%M%S")}.jpg', frame)

    # 2. Deteksi wajah menghilang
    if len(faces) == 0:
        if face_missing_start is None:
            face_missing_start = time.time()
        elif time.time() - face_missing_start >= 3:
            msg = f"[{now}] Wajah tidak terlihat lebih dari 3 detik!"
            print(msg)
            with open("cheating_log.txt", "a") as log:
                log.write(msg + "\n")
            cv2.imwrite(f'screenshots/missing_{datetime.now().strftime("%H%M%S")}.jpg', frame)
            face_missing_start = None  # reset setelah log
    else:
        face_missing_start = None  # reset jika wajah terlihat

        # 3. Deteksi wajah tidak fokus (tidak menghadap layar)
        for (x, y, w, h) in faces:
            face_center_x = x + w // 2
            frame_center_x = frame.shape[1] // 2
            offset_ratio = abs(face_center_x - frame_center_x) / frame_center_x

            if offset_ratio > 0.4:  # lebih dari 40% off-center
                msg = f"[{now}] Wajah tidak fokus pada layar (offset: {offset_ratio:.2f})"
                print(msg)
                with open("cheating_log.txt", "a") as log:
                    log.write(msg + "\n")
                cv2.imwrite(f'screenshots/offfocus_{datetime.now().strftime("%H%M%S")}.jpg', frame)

    # Tampilkan kotak wajah
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.putText(frame, f"Detected Faces: {len(faces)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Ujian Online - Deteksi Kecurangan", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
