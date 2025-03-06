x=33
r=x%2
if(r==0):
    print('even')
    if(x>30):
        print('greater than 30')
    else:
        print('less than 30')
else:         #we can just come out of if loop to get the answer as odd if r==1 but if loop is true it prints both the statements so we use else for printing only one statement
    print('odd')

y=6
if(y==1):
    print('one')
elif(y==2):
    print('two')
elif(y==3):
    print('three')
else:
    print('num not found')

for i in range(1000):
    print('hehe')
    
print('hello\n' * 100)

j=9
while j<=9:
    print('world',j)
    j=j+1
    
#we use end="" when the output is in a loop so that it prints in the same line