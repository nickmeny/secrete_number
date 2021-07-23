
import random
import datacontroller as db

# it's my first project in python. it's simple to make it but the interface it's very beautiful.
# if it has any bug, please send me an email with this bug. 
# if you liked this game, please recomende to your friends. if you do this, you will suport me a lot.







welcom = r"""

                         __                      __        __
 _          _           |  |            __ _ ___|   \    /   |
| |   __   | |          |  |_________  |   __   | |\ \  / /| |
| |  /  \  | |_ ____ __ |  | ________| |  |  |  | | \ \/ / | |__ ___ __
| | / /\ \ | |___ __ __\|  | |         |  |  |  | |  \__/  | |___ _____\
| |/ /  \ \| |_ __ __   |  | |_______  |  |__|  | |        | |___ _____
|__ /    \ __|__ __ _|  |__|_________| |___ _ __|_|        |_|_ ____ ___\


"""



# this is a def for rgb colors in lines
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

try:
    score = db.reader()
except:
    db.create()
easy = 10
normal = 20
hard = 30
x = None
tries = None

#here is the heart symbol (you can put this symbol with Alt + 3 from keypad. For more, visit this link:https://www.alt-codes.net/ )
heart = colored(255,0,0, '♥')




print(colored(0,0,255,welcom))

def _main_(score):
    #let's make the interface 
    print("*" * 40)
    print('\n')
    print("*"+colored(51,255,153,"This game made by Nick"))
    print(colored(51,255,153,"What mode do you want to play the secret number?"))
    print(colored(255,255,51,"1)")+ colored(0,255,0,"Easy"))
    print(colored(255,255,51,"2)")+ colored(255, 128, 0,"Normal"))
    print(colored(255,255,51,'3)') +colored(255,0,0,'Hard'))
    print(colored(255,255,51,'h)') +colored(0, 255, 255,"Help"))
    print(colored(255,255,51,'q)')+ colored(130, 11, 154,"quit")) 
    print('\n')
    print('\n')


    global tries
    global mode
    mode = str(input(colored(51,255,153,"What mode(1-3)? : ")))
    if mode == '1':
        x = easy
        tries = 5
        guess(x,tries,heart,score)
    if mode == '2':
        x = normal
        tries = 4
        guess(x,tries,heart,score)
    if mode == '3':
        x = hard
        tries = 3
        guess(x,tries,heart,score)
    if mode == "h":
        _help_()
    if mode == "q":
        yesno_quit()
    if mode != "1" or "2" or "3" or "h" or "q":
        print ("You need to write '1' for easy, '2' for normal and '3' for hard")
        _main_(score)
    

#here is the busic def for the game 

def guess(x,tries,heart,score):
    number = random.randint(1,x)
    guess = 0
    while guess != number:
        print(number)
        guess = int(input(f'Guess a number between 1 - {x}: '))
        if guess < number :
            print("To low. Guess again!")
            tries -= 1
            print(tries * heart)
            while tries <= 0:
                print(colored(162,12,12,"You lose"))
                print(f'The number is {number}')
                yesno(score)
        elif guess > number:
            print("To high. Guess again!")
            tries  -= 1
            print(tries * heart)
            while tries <= 0:
                print(colored(162,12,12,"You lose"))
                print(colored(153,51,255,f'The number is{colored(255,128,0, number)}'))
                yesno(score)
    print(colored(51,251,51,f'Congratulation! You found the hidden number'))
    load_score = db.reader()
    score += 1

    if load_score > score:
        load_score += 1
        db.writer(load_score)
    if load_score <= score:
        db.writer(score)
    print('\n')

    yesno(score)




def yesno(score):
    yn = input(colored(51,255,153,"Do you want to play again the Secret Number?(y/n)"))
    if yn == "y":
        print (colored(51,255,153,"ok"))
        _main_(score)
    if yn == "n":
        sure()
    if yn != "n" or "y":
        print(colored(51,255,153,"You need to input n for no or y for yes"))
        yesno(score)


def sure():
    sure1 = input(colored(255,255,51,"Are you sure?(y/n)"))
    if sure1 == "y":
        print('\n')
        print(colored(51,255,153,"Thank you very much"))
        quit()
    if sure1 == "n":
        yesno(score)
    if sure1 != "n" or "y":
        print(colored(51,255,153,"You need to input n for no or y for yes"))
        sure()





def _help_():
    print(colored(51,255,153,"This is the help guide for Secret number"))
    print('*' * 40)
    print(colored(51,255,153,"We need to input a guess for a number between 1 - 10 or 1- 20 or 1 - 30. It's a very simple game!"))
    help1 = input(colored(51,255,153,"do you want to go back to the game?(y/n) "))
    if help1 == "y": 
        _main_(score)
    if help1 == "n":
        _help_()


def yesno_quit():
    sure2 = str(input(colored(51,255,153,"Are you sure?(y/n)")))
    if sure2 == "y":
        print(colored(51,255,153,"Thank you very much"))
        quit()
    if sure2 != "n" or "y":
        print(colored(51,255,153,"You need to input n for no or y for yes"))





_main_(score)