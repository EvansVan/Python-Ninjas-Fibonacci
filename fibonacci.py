count = 0

#function to print the sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-2) + fibonacci(n-1))
        

#Request user input for numbers in sequence
nterms = int(input('Enter the number of numbers in the sequence: '))

#Check that user has entered a positive number
if nterms <=0:
    print('Please enter a valid number')
else:
    print('The numbers in the sequence are')
    while count < nterms:
        print(fibonacci(count))
        count+=1
