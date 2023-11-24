# list of numbers
list=[10,501,22,37,100,999,87,351]
#store the prime numbers in empty list
prime=[]
#loop through each number in the list
for i in list:
# starting count 0
    count=0
    for j in range(1,i):
        if i%j==0:
            count=count+1
 # If the count is 1, the number is prime 
    if count==1:
        prime.append(i)
#print the prime number
print("prime numbers are:",prime)