numbers=list(map(int,input().split()))
totalsum=int(len(numbers))
evennos=[]
oddnos=[]
twodigit=[]
positive=[]
print("1. Maximin number =",max(numbers))
print("2. Minimum number =",min(numbers))
print("3. Sum of the numbers =",sum(numbers))
print("4. Average of the numbers =",sum(numbers)//totalsum)
print("5. Second maximum number =")
for i in numbers:
    if i%2==0:
        evennos.append(i)
print("6. Even numbers =",str(evennos).replace("[","").replace("]",""))
for i in numbers:
    if i%2==1:
        oddnos.append(i)
print("7. Odd numbers =",str(oddnos).replace("[","").replace("]",""))
for i in numbers:
    if 10<=i<=99:
        twodigit.append(i)
print("8. Two digit numbers =",str(twodigit).replace("[","").replace("]",""))
for i in numbers:
    if i<0:
        positive.append(i)

        
        

    
