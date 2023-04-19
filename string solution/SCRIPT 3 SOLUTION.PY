#script to enter 5 string and print even length of string

def evenlenstr(l):
    k=0
    for i in range(5):
       n=input("Enter String : ")
       l.append(n)
    print(l)
    for j in l:
       if len(j)%2==0:
          k+=1
          print(j)
    print(f"Total String With Even Length : {k}")
l=[]
evenlenstr(l)
