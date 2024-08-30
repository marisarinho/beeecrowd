cod,quant=map(int,input().split())
total=0
if cod==1:
    total=quant*4
if cod==2:
    total=quant*4.50
if cod==3:
    total=quant*5
if cod==4:
    total=quant*2
if cod==5:
    total=quant*1.50
    
print(f'Total: R$ {total:.2f}')
