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