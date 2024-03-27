def menu():
    print("Calculator Program")
    print('Menu')
    print("1. Triangle Area")
    print("2. Rectangular Area")
    print("3. Quit")


choose_menu = int(input("choose the menu :"))

if choose_menu  < 0 and choose_menu <= 3:
    if choose_menu == 1:
        print("Triangle Area Calculator Choosed")
    length_value= int(input("Put the Length :"))
    heigth_value= int(input("Put the Height :"))
    result= 0.5 * length_value * heigth_value
    print("Result:", result)
    decision = input("Do you want to repeat the Program ?")
    if decision == "yes":
        menu()
    else:
        exit()
    

elif choose_menu == 2:
    print("Rectangular Area Calculator Choosed")
    length_value= int(input("Put the Length :"))
    width_value= int(input("Put the Height :"))
    result = length_value * width_value
    print("Result:", result)
    decision = input("Do you want to repeat the Program ?")
    if decision == "yes":
        menu()
    else:
        exit()

elif choose_menu == 3:
    print("Thanks for Using This Program!")
    exit()

#pritn odd numbers
i = 1
while i <= 10:
    if i % 2 == 1:
        print(i)
    i +=1

#make the multiple table
value = int(input('input the value: '))

x = range(1, 11)
for n in x:
    result = value * n
    print(f"{value} * {n} = {result} ")