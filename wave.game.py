n=input().lower()
for i in range(len(n)):
    print(n[0:i].lower() + n[i].upper() + n[i+1:].lower())
