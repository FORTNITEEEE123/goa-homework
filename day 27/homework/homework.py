def ჩაწერე(სტრ):
    return  input(სტრ)

def პრინტ(name):
    return print(name)

def ინტენჯერად(int0):
    return int(int0)

def ინტენჯერად(str0):
    return str(str0)

def ინტენჯერად(floate):
    return float(floate)

def ინტენჯერად(boolean1):
    return bool(boolean1)

def  სიშორე(range1):
    return range(range1)

#1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ნამრავლი.
def multiply_numbers(ა, ბ):
    return ა * ბ
#2)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.
def check_even_odd(ნუმ):
    if ნუმ % 2 == 0:
        return "კენტი"
    else:
        return "ლუწი"
#3)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.
def greet(name):
    პრინტ(name)

# Calling the function twice with different names
greet("გიოტგი")
greet("ნინო")
#4)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.
def concatenate_strings(str1, str2):
    return str1 + str2