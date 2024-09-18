n=list(map(int,input().split()))
maior=n[0]
for i in n:
    if i>maior:
        maior=i
print(maior)
