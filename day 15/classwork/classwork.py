# 1)კომენტარის სახით ახსენით როდის ვიყენებთ for ციკლს და როდის while ციკლს.
#1.ჩვენ for ციკლს ვიყენებთ როდესაც გვიდა გავიმეოროთ ერთი და იგივე სიტყვის დაპრინტვა მაგრამ ვიცით რამდენის
#2.ჩვენ while ციკლს ვიყენებთ როდესაც გვიდა გავიმეოროთ ერთი და იგივე სიტყვის დაპრინტვა მაგრამ არვიცით რამდენის

# 2)ცვლადში შეინახეთ ორიგინალი პაროლი და მომხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემთხვევა ორიგინალ პაროლს. (გამოიყენეთ input, while, !=)
original_password="64"
new_password=input("please enter your new password here: ")
while original_password != new_password:
    print(input("please enter your new password here: "))
