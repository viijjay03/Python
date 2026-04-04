#Input and Output
#(Accept a number from user and print it)

user = int(input("Enter a number : "));
print("your number is ",user); 

#Operators 
#comparison operator
#[Q1]
num1 = 55;
num2 = 65;
print (num1 > num2);  

#[Q2]
Aman_have = 456;
Ramu_have = 456;
Raja_have = 235;
Amit_have = 236;

print((Aman_have == Ramu_have) != (Raja_have == Amit_have));
 



#[Q3]
 
aa = 11;
bb = 22;
cc = 33;
dd = 44;
ee = 55;
ff = 66;
gg = 77;
hh = 88;

print((aa == bb) or (cc == dd) or (ee == ff) or (gg != hh));


#[Q4]

Tina = True;
Ram = 0.0;

print(Tina and bool(Ram)); 


#Conditional Statements
#[Q1] 
no_1 = int(input("Enter first number : "));
no_2 = int(input("Enter second number : "));
if no_1 > no_2 :
    print("First number is greater than second number", no_1);
elif no_1 < no_2 :
    print("Second number is greater than first number",no_2);
else :
    print("Both numbers are Equal ");  


#[Q2]
 
sex = input("Enter your sex(M/F) : ");


if sex == "M" :

    print("your have male human body");
elif sex == "F" :
    print("you have female  human body");
else :
    print("you are not human being, you are alien");
 

#[Q3]

no = int(input("enter a number : "));

if no % 2 == 0 :
    print("your number is even number");
else :
    print("your number is odd number"); 

#[Q4]

Uuser = input("Enter Your Name : ");
Uuser_age = int(input("Enter Your Age : "));

if Uuser_age >= 18 :
    print("Congratulations ",Uuser, "you are eligible for voting");
else :
    print("Sorry",Uuser, "you are not eligible for voting"); 