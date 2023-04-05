#write a script to check if the list contains three consecutive common numbers in Python using udf.

def commonsecutive(n):
    count=0
    k=[]
    for i in range(len(n)-2):
        if n[i]==n[i+1] and n[i+1]==n[i+2]:
            k.append(n[i])
            count+=1
    if count>0:
        print(f"Consecutive common number in list {n} as follow:{k}")
    else:
        printf("this number is no a  consecutive number in list!!")
 
