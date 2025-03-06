i=1
while i<=5:
    j=0
    while j<=3:
        print(i*j,end="")
        j+=1
    print(i)
    i+=1
    
#for loop
name='nit'
for i in name:
    print(i)

#5 multiples
for i in range(5,100):
    if i%5==0:
        print(i)
for i in range(5,100):
    if i%5!=0:
        print(i)
for i in range(1,11):
    if i==6:
        break    #for stopping the loop at a certain point
    print(i)
for i in range(1,11):
    if i==6:
        continue  #for skipping a certain point
    print(i)
for i in range(1,11):
    if i==6:
        pass  #for doing nothing and it passes the error
    print(i)

for i in range(1,50):
    if i%3!=0:
        if i%5!=0:
            print(i)
for i in range(1,50):
    if i%3!=0 or i%5!=0:
        continue
        print(i)

for i in range(1,5):
    print('# # # #')
    i+=i
for i in range(1,5):
    if i<=5:
        print("# # # #")
for i in range(4):
    for j in range(i+1):
        print('#',end=" ")
    print()
for i in range(4):
    for j in range(4-i):
        print('#',end=" ")
    print()


nums=[12,13,1,4,15,19,20]
for num in nums:
    if num%5==0:
        print(num)
        # break    #for printing only one value

for num in nums:
    if num%5==0:
        print(num)
        break
    else:
        print('num not found') #checks every iteration
        #if we use break it will stop at the first iteration until it finds the number

num1=17
for i in range(2,num1):
    if num1%i==0:
        print("not prime")
        break
    else:
        print('prime')
        break

for i in range(1,6):
    print(' * '*i)
for i in range(5,0,-1):
    print(' * '*i)