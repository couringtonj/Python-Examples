def calc_love_score(name1,name2):
    trimmed_name1=name1.replace(" ","")
    trimmed_name2=name2.replace(" ","")
    t = 0
    r=0
    u=0
    e=0
    l=0
    o=0
    v=0
    e2=0
    
    for ltr in (trimmed_name1+trimmed_name2):
        if ltr=="T" or ltr=="t":
            t+=1
        elif ltr=="R" or ltr=="r":
            r+=1
        elif ltr=="U" or ltr=="u":
            u+=1
        elif ltr=="E" or ltr=="e":
            e+=1
        elif ltr=="L" or ltr=="l":
            l+=1
        elif ltr=="O" or ltr=="o":
            o+=1
        elif ltr=="V" or ltr=="v":
            v+=1
        elif ltr=="E" or ltr=="e":
            e2+1        
            
    num1=t+r+u+e
    num2=l+o+v+e2
    display(num1,num2)
def display(num1,num2):
    print(f"Your love score is {num1}{num2}")

first_name=input("Whats is your name? ")
second_name=input("Whats your significant others name? ")
calc_love_score(first_name,second_name)