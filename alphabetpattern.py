
a = 65  
n = 5  

for i in range(n):
    
    for j in range(n - i):
        print(chr(a + i), end="")
    print("")
