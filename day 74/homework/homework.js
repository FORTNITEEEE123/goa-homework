// 3)შექმენით ორი სია, პრიველში დაამატეთ 10 ცალი ცაიფრი მეორეში 10 ცალი სტრინგი, შემდეგ ეს ორი სია გაერთიანეთ ერთ სიაში მეთოდის საშუალებით, შემდეგ delete ით შეცვალეთ მეხუთე ინდექსზე მდგომი ელემენტი undefined ით,  შემდეგ სიიდან ამოაგდეთ ბოლო ელემენტი, შემდეგ ამოაგდეთ პირველი ელემენტი და პირველ ინდექსზე ჩასვით "ვანო",  შემდგომბოლოშ ჩაამატეთ ერთი ელემენტი "მოთიაშვილი", საბოლოოდ გამოიტანეთ ეს მთლიანი სია გადაქცეული სტრინგად (დაიხმარეთ რესურსები)
const ListNum = [1,2,3,4,5,64,77,1000,640,21]
const ListStr = ["luka","otarashvili","ლუკა","ოთარაშვილი","mr.vano","motiashvili","ბატონი-ვანო","მოთიაშვილი","მე-ვარ","მინილიდერი"]
// 1)
let JoinedStrNum = ListNum.concat(ListStr)
//2)
delete JoinedStrNum[5]
//3)
JoinedStrNum.pop()
//4)
JoinedStrNum.shift()
JoinedStrNum.unshift("ვანო")
//5)
JoinedStrNum.push("მოთიაშვილი")
//6)
console.log(JoinedStrNum.toString())
//4)შექმენით 3 სია, პირველს შეაურთედ მეორე და შეინახეთ ცვალდშ, შემდეგ ეგ სია შეურთედ მესამეს და ისიც შეინახეთ ცვლადიშ, შემდგომ splice ის საშუალების მე 2 ინდექსიდან ემ 5 ინდექსამდე წაშალეთ ელემენტები და მესამე ელემენტო გახადეთ undefined, delete ის საშუალებით, შემდგომ გამოიტანეთ ამ სიის ბოლო ელემენტი
let list1 = [1, 2, 3]
let list2 = [4, 5, 6]
let list3 = [7, 8, 9]
let combinedList1 = list1.concat(list2)
let combinedList2 = combinedList1.concat(list3)
console.log("საწყისი გაერთიანებული სია:", combinedList2)
combinedList2.splice(2, 4)
console.log("splice-ის შემდეგ:", combinedList2)
delete combinedList2[2]; 
console.log("delete-ის შემდეგ:", combinedList2)
let lastElement = combinedList2[combinedList2.length - 1];
console.log("ბოლო ელემენტი:", lastElement)