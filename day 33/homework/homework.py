#შექმენით manual_split ფუნქცია
def მანუალური_გამყოფი(სტრ, სიმბოლი):
     result=[]
     test=""
     for i in str:
         if i !=სიმბოლი:
             test+=i
         else:
             result.append
             test=""
     if(test):
         result.append(test)
     return result

 
#შექმენით manual_replace ფუნქცია
#ვერ გავაკეთე :(
ჩემ_შესახებ=("მე მქვია name ,მე ვარ 11 წლის.")
print(ჩემ_შესახებ.replace("name","ლუკა"))


#შექმენით manual_join ფუნქცია
def მანუალური_შემაერთებელი(arr,symbole):
    result=""
    for i in arr:
        result+=i+symbole
    return result[0:-1]