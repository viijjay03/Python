#Loops

#[Q1] print "hello world" 5 times

user = int(input("Enter a Number : "));
for i in range(user):
    print("hello world "); 

#[Q2] natural numbers
num = int(input("Enter a number : "));
for i in range(1,num,1):
    print(i);

#[Q3] reverse of a number
 
num1 = int(input("Enter a number : "));
for i in range(num1,0,-1):
    print(i); 
 
#[Q4] Table of a number
num2 = int(input("Enter a number : "));
for i in range(1,11,1):
    print(num2*i); 
 
#[Q5] sum of n natural numbers
num3 = int(input("Enter a number : "));
sum = 0
for i in range(1,num3+1,1):
    sum += i;
print("Sum of n natural numbers is : ",sum); 
 
#[Q6] factorial of a number
num4 = int(input("Enter a number : "));
fact = 1
for i in range(1,num4+1,1):
    fact *= i;
print("Factorial of the number is : ",fact);
 
 
#[Q7] sum of odd and even of a number
num5 = int(input("Enter a number : "));
 
even = 0
odd = 0
for i in range(1,num5+1,1):
    if i%2 == 0:
        even += i;
    else :
        odd += i;
print("Sum of even numbers is : ",even);
print("Sum of odd numbers is : ",odd);

# [Q8] factors of a number
user1 = int(input("Enter a number : "));
print(f"Factors of {user1} are :",end = " ");
 
for i in range(1,user1+1):
    if user1 % i == 0:
        print(i, end=" ");
# [Q9] perfect number
user2 = int(input("Enter a number : "));

sum = 0 
for i in range(1,user2,1):
    if user2 % i == 0 :
        sum = sum + i;

if sum == user2:
    print("perfect number");
else : 
    print("not a perfect number");
 
#[Q10] prime number
user3 = int(input("Enter a number : "));
count = 0
for i in range(1,user3+1,):
    if user3 % i == 0 :
        count = count + 1;
if count == 2 :
    print ("prime number");

else : 
    print("not a prime number");