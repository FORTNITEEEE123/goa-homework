
# 1)მომხმარებელს შემოატანინეთ მისი სახელი და თუ ეს სახელი უდრის თქვენს სახელს, დაბეჭდეთ "Hello" სხვა შემთხვევაში "Bye".

my_name="luka"
costumer_name=input("please enter your name here: ")
if my_name == costumer_name:
    print("hello")
else:
    print("bye")

# 2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".

my_favorite_num=64 #იმიტომ არის 64 ჩემი საყვარელი რიცხი უბრალოდ მომწონს 6ის და 4ის კომბინაცია :)
costumers_favorite_num=int(input("please enter your favorite number here: "))
if my_favorite_num == costumers_favorite_num:
    print("perfect")
elif my_favorite_num < costumers_favorite_num:
    print("more")
else:
    print("less")

# 3)(რთული დავალება) შექმენით for ციკლი 150ის დიაპაზონში და შეამოწმეთ თითოეული რიცხვი, თუ ეს რიცხვი არის ლუწი, მაშინ დაბეჭდეთ "Luwia" და გვერძე მიაწერეთ რიცხვი (მინიშნება ---> print("Luwia", i) ხოლო თუ იქნება კენტი, დაბეჭდეთ "Kentia" და გვერძე მიუწერეთ ეს რიცხვი. (მინიშნება % ოპერატორი) (აბრუნებს ნაშთს)

for i in range(151):
    if i % 2 == 0: 
        print("ლუწია", i)
    else:           
        print("კენტია", i)

# 4)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".
    
costumers_age=int(input("please enter your age here: "))
costumers_name=input("please enter your name here: ")
my_name2="luka"
my_age=11
if my_name2 == costumers_name and  my_age == costumers_age:
    print('were twins')
else:
    print("were not twins")