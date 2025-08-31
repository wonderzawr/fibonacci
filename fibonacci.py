n=int(input()) 
a = 1 
b = 0 
for i in range(n): 
    c = a 
    a += b 
    b = c 
    print(b, end=" ")
