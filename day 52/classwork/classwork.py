#1)შექმენით ფუნქცია რომელსაც გადაეცემა გვარი, თქვენი დავალებაა ამ გვარიდან ამოშალოთ ყველა ხმოვანი (a / e / i / o / u ) და  ისე დააბრუნოთ ეს გვარი /// გამოიყენეთ in ოპერატორი)
def remove_vowels(გვარი):
    vowels = "aeiouAEIOU"  
    result = "" 
    for i in გვარი:
        if i not in vowels:  
            result += i
    return result
