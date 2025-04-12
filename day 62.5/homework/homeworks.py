#1)შექმენით while loop რომელიც გამოიტანს "hello world!" სანამ არ გაუტოლდება 20'ს
number=0
while number < 20:
  print("hello world")
  number += 1

list0 = input("შეიყვანეთ ელემენტები გამოყავით ელემნტები , ნიშნით : ")

#2)მომხმარებელს შემოატანინეთ სია და for loop ის საშუალებით გამოიტანეთ ყველა ელემენტი
list1=print("")
for i in list0:
    print(i)

#3)რას ნიშნავს immutable, mutable 
print("Immutable = შეუცვლელი")
print("mutable = შეცვლადი")

#4)and და or ოპერატორებზე გააკეთეთ 5-5 მაგალითი 
print(True and False)#=false
print(True and True)#=true
print(False and False)#=false

print(True or False)#=True
print(True or True)#=True
print(False or False)#=False