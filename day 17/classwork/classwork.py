# 1)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი, შემდეგ მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ თუ მისი რიცხვი ემთხვევა თქვენს საყვარელ რიცხვს, გამოიტანეთ Hello, თუ არ ემთხვევა მაშინ Goodbye

favorite_num=64
random_num=int(input("enter random number here: "))
if favorite_num == random_num:
    print("hello")
else:
    print("goodbye")

# 2)შემოიტანეთ ორი რიცხვი, თუ პირველი რიცხვი მეტია მეორეზე, დაბეჭდეთ "First" / თუ მეორე რიცხვი მეტია პირველზე, დაბეჭდეთ "Second" თუ ხოლო თუ ისინი ტოლია, დაბეჭდეთ "Equal"

num=int(input("enter random number here: "))
num_1=int(input("enter second random number here: "))
if num > num_1:
    print("first")
elif num < num_1:
    print("second")
else:
    print("Equal")