#შექმენით 10ელემენტიანი სია და გამოიტანეთ ბოლო და პირველი ელემენტის სხვაობა

number=[5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
difference = number[-1]-number[0]
print(difference)

#2)შექმენით სია და slicing ის გამოყენებით გამოიტანეთ სიის ყველა ელემენტი მე2დან მე5 ინდექსი ჩათვლით

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
number= my_list[2:6]
print(number)

#3)გაიხსენეთ for ციკლი:
 #. გამოიტანეთ for ციკლის საშუალებით თქვენი სახელი ხუთჯერ
 #. მომხმარებელს შემოატანინეთ წინადადება და გამოიტანეთ ამ წინადადების  თითოეული ასო ცალ-ცალკე

for i in range(5):
    print("luka")
 
sentence = input("please enter random sentence here: ")
for char in sentence:
    print(char)

#4)შექმენით სია და გადაეცით for ციკლს სიის ცვლადი, შემდეგ დაბეჭდეთ საიტერაციო ცვლადი და ნახეთ შედეგი (გატესტეთ უბრალოდ) 

my_list = [11, 21, 35, 54, 64]
for item in my_list:
    print(item)

#5)კომენტარის სახით ახსნეით რა არის mutable და რა არის imutable

#Mutable ობიექტები შეიძლება შეიცვალოს უშუალოდ მათი შექმნის შემდეგ.

#Immutable ობიექტები არ შეიძლება შეიცვალოს, რაც მათი შექმნის შემდეგ ხდება.