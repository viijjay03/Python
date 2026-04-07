# #[Q1]
# count = 1 ; 

# while count <= 10 :
#     print(count);
#     count = count + 1;

#[Q2]

# num = 1;
# while num <= 10 :
#     print(num);
#     num = num + 1;

#[Q3]
# num1 = int(input("Enter a Number :"));

# rev = 0;
# while num1 > 0 :
#     rev = rev * 10 + num1 % 10
#     num1 = num1 // 10;

# print(rev);

#[Q4] The Gusse Game

import random
game_no = random.randint(1,22);
# print(game_no);

tries = 0;
while True:
    user_no = int(input ( " Enter a number btween 1 to 22 : "));



    if game_no == user_no :

        tries += 1;
        print(f"Congratulations! You have won the GAME in {tries} tries : {game_no}");
        break
    
    elif game_no > user_no :

        tries += 1;
        print("Your number is smaller than the game number! ");
    
    elif game_no < user_no :

        tries += 1;
        print("Your number is greater than the game number! ");
    

    else :

        tries += 1;
        print("Better Luck Nxt time! ");
