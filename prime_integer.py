x = int(input("Masukkan X: "))            
prime = True                                

for i in range(2, x):
    if x % i == 0:
        prime = False

if not prime:
    print(f"{x} bukan bilangan prima")    
else:
    print(f"{x} adalah bilangan prima")   