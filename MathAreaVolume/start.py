from area import circle, square, triangle
from volume import circle2, square2 , trapezoid

# Define Area
luas_lingkaran = circle.luas_lingkaran
luas_persegi = square.luas_persegi
luas_segitiga = triangle.luas_segitiga

# Define Volume
volume_bola = circle2.volume_bola
volume_kubus = square2.volume_kubus
volume_trapesium = trapezoid.volume_trapesium

print("Area Measurement")
print()
print("1. Circle")
print("    r=22/7","radius=21")
print("    pi*r*r =", luas_lingkaran(radius=21))
print("2. Square")
print("    s=5")
print("    s*s =", luas_persegi(sisi=5))
print("3. Triangle")
print("    a=5","t=12")
print("    0.5*a*t =", luas_segitiga(alas=5, tinggi=12))

print()

print("Volume Measurement")
print()
print("1. Sphere")
print("    radius=21")
print("    4/3*pi*r*r*r =", volume_bola(radius=21))
print("2. Cube")
print("    s=5")
print("    s*s*s =", volume_kubus(sisi=5))
print("3, Trapezoid")
print("    a=5","b=12","h=10")
print("    0.5*(a+b)*h =", volume_trapesium(a=5, b=12, h=10))