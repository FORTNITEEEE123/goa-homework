// 1) შექმენით ცვლადი სადაც შეინახავთ თქვენთვის სასურველ ასაკს, თუ იქნება 13 წელზე ნაკლების გამოუტანეთ You are kid, თუ იქნება 18 წელზე ნაკლების მაგრამ 13'ზე მეტის გამოუტანეთ You are not adult yet
//და თუ იქნება 18 წელზე მეტის გამოუტანეთ You are adult
let age = 12
if(age < 13){
    console.log("you are little kid nigger joking ;)")
}else if(age > 13 && age <18){
    console.log("you are not adult yet like nigger joking ;)")
}else if(age > 18){
    console.log("bravo you are finelly an adult like nigger joking")
}


// 2) შექმენით ცვლადი სადაც შეიტანთ რაიმე რიცხვს, თუ რიცხვი იყოფა 2'ზე უნაშთოდ გამოიტანეთ ეს რიცხვი, სხვა შემთხვევაში დააბრუნეთ "ეს რიცხვი კენტია"
let number = 64
if (number % 2){
    console.log("ეს რიცვი ჩემო კარგო არის ლუწი")
}else{
    console.log("ჩემო სიყვარულო ეს რიცხვი კენტია")
}


// 3) პირველი დავალება შეასრულეთ python'შიც და დაწერეთ განსხვავებები python'ისა და js'ს შორის.
//განსხავებაა ენა სინტაქსი

//age = 12
//if age < 13:
//  print("you are little kid nigger joking ;)")
//elif age > 13 and age <18:
//  print("you are not adult yet like nigger joking ;)")
//elif age > 18:
//  print("bravo you are finelly an adult like nigger joking")

//4) რას აკეთებს "!" ოპერატორი ახსენით თქვენი სიტყვებით
//იგივე რაც პიტონში not

//5) შექმენით ცვლადი სადაც შეინახავთ რაღაც რიცხვს შემდეგ შეამოწმეთ თუ ეს რიცხვი იყობა 3'ზეც და 9'ზეც გამოიტანეთ ეს რიცხვი, სხვა შემთხვევაში დააბრუნეთ "task was not completed."
let RandomNum = 64 + 0
if (RandomNum % 3 && RandomNum % 9){
    console.log(RandomNum)
}else{
    console.log("task was not completed. you cool nigga joking ;)")
}