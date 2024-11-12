#1)შექმენით სია შემდგარი რიცხვებისგან და პირველ რიცხვს დაუმატეთ ბოლო რიცხვი სიიდან

numbers = [15, 25, 35, 45, 55]
numbers[0] += numbers[-1]
print(numbers)

#2)მომხმარებელს შემოატანინეთ მისი გვარი და გაოუტანეთ იგივე გვარი ოღონდ შებრუნებულად

last_name=input("enter your last name here: ")
reversed_last_name = last_name[::-1]
print(reversed_last_name)

#3)შექმენით სია სადაც გექნებათ 5 ელემენტი და გამოიტანეთ ბოლო ორი ელემენტი სიიდან

my_list = [11, 30, 40, 50, 60]
last_two_elements = my_list[-2:]
print(last_two_elements)

# 4)შექმენით სია შემდგარი 5 სახელისგან და მესამე სახელი შეცვალეთ თქვენი სახელით

names_list = ["მარიამი", "დავით", "სალომე", "ნიკა", "ელენე"]
names_list[2] = "ლუკა"
print(names_list)