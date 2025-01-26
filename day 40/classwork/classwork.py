#2)შექმენით ფუნქცია manual_join() რომელიც გააკეთებს იგივე დავალებას რასაც აკეთებს მეთოდი .join() (ანუ შექმენით join-ის კლონი).
def manual_join(str1,):
    return str1.join(str1)

#3)შექმენით ორი ცვლადი, პირველში შეინახეთ ემაილი, მეორეში შეინახეთ პაროლი, შემდეგ მომხმარებელს შეეკითხეთ პაროლი და ემაილი სანამ არ დაემთხვევა სწორ პაროლ და ემაილს.
email=input("please enter your emile here: ")
password=(input("please enter your password: "))
print("email and password was saved")
print("error accourd please enter youre again correctly email and password")
email1=input("please enter your emile here: ")
password1=input("please enter your password: ")
for i in email1 and password1:
    if email1 != email and password1!= password :
        print("please enter your password and email again")
        email1=input("please enter your emile here: ")
        password1=input("please enter your password: ")
    elif email1 == email and password1 == password:
        print("email and password was succcesfully saved")