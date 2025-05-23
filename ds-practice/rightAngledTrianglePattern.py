'''
Set outer loop to print the rows.
Set inner loop to print the columns.
Set the value of the inner loop to the current value of the count.
Set the count to be 0.
After each iteration of the outer loop, increase the value of the inner loop by 1 i.e increase count by 1.
In the inner loop create an if condiitonal to print the stars if the count is less than or equal to N else exit the loop?




'''
N = 5
count = 1
for i in range(N):
    for j in range(count):
        print('*', end = ' ')
    count += 1    
    print()



