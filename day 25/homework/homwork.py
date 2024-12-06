# 1)შექმენით ცარიელი სია, შემდეგ For Loop-ის მეშვეობით ამ სიაში ჩაამატეთ ყველა კენტი რიცხვი 0დან 100მდე, ბოლოს დაბეჭდეთ ეს სია.
odd_numbers = []
for num in range(0, 101):
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)
#2)მომხმარებელს შემოატანინეთ მისი საყვარელი 5 საჭმელი (For Loop-ის მეშვეობით), შემდეგ შემოატანინეთ რიცხვი და ამ რიცხვის ინდექზე მდგომი ელემენტი ჯერ დაუბეჭდეთ, ბოლო ამოაგდეთ და ამოგდების შემდეგ დაბეჭდეთ სია.
favorite_foods = []
for i in range(5):
    food = input(f"შეიტყვეთ თქვენი საყვარელი საჭმელი {i + 1}: ")
    favorite_foods.append(food)
numb= int(input("შეიტყვეთ რიცხვი (0-4), რათა მოიძიოთელემენტი: "))
if 0 <= numb < len(favorite_foods):
    print(favorite_foods[numb])
else:
    print("ოცნების ინდექსი მიუღებელია!")
removed_food = favorite_foods.pop() if favorite_foods else None
print(favorite_foods)
if removed_food:
    print(removed_food)
#3)შექმენით სია, მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ შეეკითხეთ როგორ უნდა რო შეცვალოს ეს სახელი / თუ გადმოგცემთ "upper" სიაში დაამატეთ მომხმარებლის სახელი გადიდებულად, თუ გადმოგცემთ "lower" სიაში დაამატეთ დაპატარავებულად, თუ გადმოგცათ "capitalize" სიაში დაამატეთ ისე, რომ სახელის პირველი ასო გადიდებული იყოს...
name = input("შეიტყვეთ თქვენი სახელი: ")
formatted_names = []
format_choice = input("როგორ გსურთ თქვენი სახელი: 'upper', 'lower' თუ 'capitalize'? ")
if format_choice == "upper":
    formatted_names.append(name.upper())
elif format_choice == "lower":
    formatted_names.append(name.lower())
elif format_choice == "capitalize":
    formatted_names.append(name.capitalize())
else:
    print("გთხოვთ, მიუთითოთ 'upper', 'lower' ან 'capitalize'.")

print(formatted_names)
#4)მომხმარებელს შემოატანინეთ მისი სახელი, თუ ეს სახელი იქნება სიგრძეში 6 სიმბოლოზე მეტი ან ტოლი, მაშინ დაუბეჭდეთ "Hello", თუ იქნება სიგრძეში 5 სიმბოლო, დაუბეჭდეთ "Ola", სხვა შემთხვევაში დაუბეჭდეთ "Bonju".
name1=input("გთოხვთ დაწეროთ თქვენი სახელი აქ: ")
name1_=len(name1)
if name1_ >= 6:
    print("გამარჯობა")
elif name1_ == 5:
    print("ოლა")
else:
    print("ბონჯიო")
#5)შექმენით ორი ცარიელი სია (odd = [] / even = []), შემდეგ For Loop-ის მეშვეობით შექმენით რიცხვების თანმიმდევრობა 0დან 100მდე და გაფილტრეთ ეს რიცხვები (ლუწი რიცხვები ჩაამატეთ even სიაში, ხოლო კენტი რიცხვები ჩაამატეთ odd სიაში) ბოლოს დაბეჭდეთ ორივე სია.
odd = []
even = []
for number in range(101):
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print("ლუწი რიცხვები:", even)
print("კენტი რიცხვები:", odd)
#6)შექმენით სია 5 ელემენტით, მომხმარებელს შემოატანინეთ მისი საყვარელი საჭმელი და ასევე შემოატანინეთ რიცხვი, შემდეგ მომხმარებლის საყვარელი საჭმელი ჩასვით სიაში იმ ინდექსზე რომელი რიცხვიც შემოიტანა, ბოლოს დაბეჭდეთ სია. 
list1=[4,6,64,640,6400]
guest=input("ჩაწერეთ აქ თქვენი საყვარელი საჭმელი: ")
guest1=int(input("ჩაწერეთ აქ რიცხვი 0დან 4დე: "))
list1.append(guest)
list1.pop(guest1)
print(list1)