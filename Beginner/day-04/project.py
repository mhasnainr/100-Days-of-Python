# ------------------------ 09: Project: Rock, Paper and Scissors

import random
rock = """

                                             
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  

"""


paper = """

8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88              

"""


scissors = """

                                                                              
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"'

"""

# Rules

# 1. Rock wins against scissors
# 2. Scissors win against Paper
# 3. Paper wins against Rock

# 0: rock, 1: paper, 2: scissors


game_images = [rock, paper, scissors]

user = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user > 2 or user < 0:
    print("You typed a wrong number")
else:
    print(game_images[user])

    pc = random.randint(0, 2)
    print(f"\nPC Chose:")
    print(game_images[pc])

    if user == 0 and pc == 2:
        print('You win!')
    elif pc == 0 and user == 2:
        print('You lose!')
    elif pc > user:
        print('You lose!')
    elif user > pc:
        print('You win!')
    elif pc == user:
        print('Draw!')
