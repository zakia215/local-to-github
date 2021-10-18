x = int(input("Masukkan X: "))            
prime = True                                

for i in range(2, x):
    if x % i == 0:
        prime = False

if not prime:
    print(f"{x} is not a prime number")    
else:
    print(f"{x} is a prime number")  
