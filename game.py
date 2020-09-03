import turtle
from turtle import Turtle
import random
import time
from datetime import datetime
from configparser import ConfigParser


def log_game(win_or_loss, old_balance, new_balance, bet_amount):
    # "a" for append
    log = open("game_log.log", "a")
    log.write(f"[{datetime.now()}] {win_or_loss + ' | Bet: ' + str(bet_amount) + ' | Old balance: ' + str(old_balance) + ' | New balance: ' + str(new_balance)}\n")
    log.close()


def log_restart():
    # "a" for append
    log = open("game_log.log", "a")
    log.write(f"[{datetime.now()}] {'GAME RESTARTED'}\n")
    log.close()


conf = ConfigParser()
conf.read("opt.conf", encoding='utf-8')

# Set up the screen
wn = turtle.Screen()
wn.setup(width=500, height=400, startx=-200, starty=-600)
wn.title("Slot Machine")
wn.colormode(255)
wn.bgcolor("lightgrey")

shape1 = turtle.Turtle()
shape2 = turtle.Turtle()
shape3 = turtle.Turtle()

shape1.setheading(90)
shape2.setheading(90)
shape3.setheading(90)

shape1.up()
shape2.up()
shape3.up()

shape1.shapesize(3, 3)
shape2.shapesize(3, 3)
shape3.shapesize(3, 3)

shape1.goto(-120, 0)
shape2.goto(120, 0)

keep_playing = True
shape_list = ['circle', 'square', 'triangle']

welcome_text = turtle.Turtle()
welcome_text.up()
welcome_text.goto(-230, 120)
welcome_text.write('Welcome to Primdahls Slot Machine!\n3 Circles = 5 times amount back\n3 Squares = 15 times amount '
                   'back\n3 Triangles = 25 times amount back', font=("Arial", 12, "normal"))

money_text = turtle.Turtle()

bet_text = turtle.Turtle()
bet_text.up()
bet_text.goto(-230, -100)

result_text = turtle.Turtle()
result_text.up()
result_text.goto(-230, -165)

highscore_text = turtle.Turtle()
highscore_text.up()
highscore_text.goto(105, -175)
highscore_text.write('highscore: ' + str(conf.getint('score', 'highscore')), font=("Arial", 12, "normal"))

money = 1500
score_result = 1500

while keep_playing is True:
    if money < 20:
        print('No more money, you loose!\nYour score: ' + str(score_result))
        print('Resetting game...\n')

        log_restart()

        game_over_box = turtle.Turtle()
        game_over_box.up()
        game_over_box.shape('square')
        game_over_box.shapesize(8, 17)

        game_over_text = turtle.Turtle()
        game_over_text.up()
        game_over_text.color('white')
        game_over_text.goto(0, -50)
        game_over_text.write('GAME OVER!\nYOUR SCORE: ' + str(score_result) + '\nRESTARTING GAME...', align='center',
                             font=("Deja Vu Sans Mono", 20, "bold"))

        time.sleep(5)

        game_over_box.hideturtle()
        game_over_box.clear()
        game_over_text.hideturtle()
        game_over_text.clear()

        money_text.clear()
        result_text.clear()
        bet_text.clear()

        highscore_text.clear()
        highscore_text.up()
        highscore_text.goto(105, -175)
        highscore_text.write('highscore: ' + str(conf.getint('score', 'highscore')), font=("Arial", 12, "normal"))

        money = 1500
        score_result = 1500

    money_text.clear()
    money_text.up()
    money_text.goto(-230, 60)

    print('You have: ' + str(money) + '$ to use')
    money_text.write('You have: ' + str(money) + '$ to use', font=("Arial", 16, "normal"))
    bet = int(input('Amount to bet: '))

    result_text.clear()
    result_text.up()
    result_text.goto(-230, -170)

    if bet > money:
        print('Sorry, not enough balance\n')
        bet_text.clear()
        bet_text.write('Not enough balance for the bet', font=("Arial", 12, "normal"))
        bet_text.up()
        bet_text.goto(-230, -80)
        continue

    if bet < 20:
        print('Bet needs to be 20$ or over\n')
        bet_text.clear()
        bet_text.write('Bet needs to be 20$ or over', font=("Arial", 12, "normal"))
        bet_text.up()
        bet_text.goto(-230, -80)
        continue

    money_before_bet = money
    money = money - bet

    bet_text.clear()
    bet_text.write('Your bet: ' + str(bet) + '$', font=("Arial", 12, "normal"))
    bet_text.up()
    bet_text.goto(-230, -80)

    for i in range(3):
        shape1.shape(shape_list[i])
        time.sleep(0.1)
        shape2.shape(shape_list[i])
        time.sleep(0.1)
        shape3.shape(shape_list[i])
        time.sleep(0.1)

    result1 = random.choice(shape_list)
    shape1.shape(result1)

    result2 = random.choice(shape_list)
    shape2.shape(result2)

    result3 = random.choice(shape_list)
    shape3.shape(result3)

    bet_amount = bet

    if result1 == result2 and result2 == result3:
        if result1 == 'circle':
            print('WINNER 3 CIRCLES!')
            bet = bet * 5
            old_money_amount = money
            money = money + bet
            print('You get 5 times the bet again\nNew balance: ' + str(money) + '$\n')
            result_text.write('WINNER 3 CIRCLES!\nYou get 5 times the bet again\nOld balance: ' + str(old_money_amount) +
                              '$\nNew balance: ' + str(money) + '$', font=("Arial", 12, "normal"))

            if score_result < money:
                score_result = money
                cnfFile = open('opt.conf', "w")
                conf.set('score', 'highscore', str(score_result))
                conf.write(cnfFile)
                cnfFile.close()

            log_game('WIN 5x', old_money_amount, money, bet_amount)

        elif result1 == 'square':
            print('WINNER 3 SQUARES!')
            bet = bet * 15
            old_money_amount = money
            money = money + bet
            print('You get 15 times the bet again\nNew balance: ' + str(money) + '$\n')
            result_text.write('WINNER 3 SQUARES!\nYou get 15 times the bet again\nOld balance: ' + str(old_money_amount) +
                              '$\nNew balance: ' + str(money) + '$', font=("Arial", 12, "normal"))

            if score_result < money:
                score_result = money
                cnfFile = open('opt.conf', "w")
                conf.set('score', 'highscore', str(score_result))
                conf.write(cnfFile)
                cnfFile.close()

            log_game('WIN 15x', old_money_amount, money, bet_amount)

        elif result1 == 'triangle':
            print('WINNER 3 TRIANGLES!')
            bet = bet * 25
            old_money_amount = money
            money = money + bet
            print('You get 25 times the bet again\nNew balance: ' + str(money) + '$\n')
            result_text.write('WINNER 3 TRIANGLES!\nYou get 25 times the bet again\nOld balance: ' + str(old_money_amount) +
                              '$\nNew balance: ' + str(money) + '$', font=("Arial", 12, "normal"))

            if score_result < money:
                score_result = money
                cnfFile = open('opt.conf', "w")
                conf.set('score', 'highscore', str(score_result))
                conf.write(cnfFile)
                cnfFile.close()

            log_game('WIN 25x', old_money_amount, money, bet_amount)

    else:
        print('Sorry, you loose - try again\n')
        result_text.write('Sorry, you loose - try again', font=("Arial", 12, "normal"))

        log_game('LOST', money_before_bet, money, bet)

