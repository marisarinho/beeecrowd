n = float(input())
cem = int(n // 100)       
resto = n % 100      
cinq = int(resto // 50)   
resto2 = resto % 50      
vinte = int(resto2 // 20)  
resto3 = resto2 % 20       
dez = int(resto3 // 10)   
resto4 = resto3 % 10      
cinco = int(resto4 // 5)  
resto5 = resto4 % 5       
dois = int(resto5 // 2)   
resto6 = resto5 % 2       
um = int(resto6 // 1)     
resto7 = resto6 % 1
zero5 = int(resto7 // 0.50)
resto8 = resto7 % 0.50
zero25 = int(resto8 // 0.25) 
resto9 = resto8 % 0.25
zero10 = int(resto9 // 0.10) 
resto10 = resto9 % 0.10
zero05 = int(resto10 // 0.05) 
resto11 = resto10 % 0.05
zero1 = int(round(resto11 / 0.01))

print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinq} nota(s) de R$ 50.00')
print(f'{vinte} nota(s) de R$ 20.00')
print(f'{dez} nota(s) de R$ 10.00')
print(f'{cinco} nota(s) de R$ 5.00')
print(f'{dois} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{um} moeda(s) de R$ 1.00')
print(f'{zero5} moeda(s) de R$ 0.50')
print(f'{zero25} moeda(s) de R$ 0.25')
print(f'{zero10} moeda(s) de R$ 0.10')
print(f'{zero05} moeda(s) de R$ 0.05')
print(f'{zero1} moeda(s) de R$ 0.01')
