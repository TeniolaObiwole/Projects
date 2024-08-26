'''
N is the number of rows.

Create an outer for loop and set it to range N+1. We're going to count the rows from 1.

Create an inner for loop and set it to range( 1, N - i +1).
The first inner for loop is to determine the number of white spaces we need to print before the stars. 
The number of white spaces can be calculated by subtracting the current row from the total number of rows.

Print the white spaces using the print argument end so the cursor remains on the same line(row) after printing.

Create a second inner for loop to print the stars and set it to range(1, i+1).
The number of stars to be printed is equal to the value of the current row.
Print the stars.
Print a new line.

'''

rows  = int(input('Enter the number of rows:\n')) 

for row in range(rows+1):
    for space in range(1, rows- row +1):
        print(end =' ')
    for star in range(1, row+1):
        print('*', end = ' ')
    print()

