import turtle
import random
import sys

start = True
guess = septtra = again = False


wn = turtle.Screen()
rand_num = None
wri = turtle.Turtle()
hilo = turtle.Turtle()


def print_box(x_pos, y_pos, num):
    write(num, 50, x_pos, y_pos)


def num_board(num):
    sept = turtle.Turtle()
    sept.shape("blank")
    sept.tracer(10)
    sept.speed(0)
    sept.up()

    box = 0
    x_pos = 150
    y_pos = 650

    for i in range(10):
        for u in range(10):
            box += 1
            print_box(x_pos, y_pos, box)
            x_pos += 75
            if box > num:
                return
        x_pos = 150
        y_pos -= 60
    while septtra:
        sept.up()
        sept.forward(.1)
        sept.backward(.1)
        sept.down()


def write(word, font_size, x, y):
    global wri
    wri.speed(0)
    wri.shape("blank")
    wri.up()
    wri.goto(x, y)
    wri.write(word, move=False, align="center", font=("Arial", font_size, "normal"))
    wri.stamp()


def startup():
    write("GUESSING GAME\n\nCLICK TO START", 75, 500, 500)


def game(x, y):
    global wri, start, guess, hilo, rand_num, septtra, again

    if start:
        start = False
        guess = septtra = True
        if 0 < x < 1000 and 0 < y < 1000:
            wri.clear()
            write("INSTRUCTIONS", 50, 500, 800)
            num_board(100)

    if guess:
        if 337 < x < 660 and 808 < y < 861:
            septtra = False
            wri.clear()
            write("Click a number to guess between 1 and 100\n You win if you click the correct number", 50, 500, 500)
            start = True
        elif 124 < x < 174 and 656 < y < 706:

            num = 1
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
        elif  199 < x < 244 and 660 < y < 696:
            num = 2
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(1)
        elif 277 < x < 320 and 656 < x < 705:
            num = 3
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(2)
        elif 354 < x < 392 and 659 < y < 706:
            num = 4
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(3)
        elif 409 < x < 485 and 650 < y < 710:
            num = 5
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(4)
        elif 485 < x < 560 and 560 < y < 710:
            num = 6
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(5)
        elif 560 < x < 633 and 650 < y < 710:
            num = 7
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(6)
        elif 633 < x < 714 and 650 < y < 710:
            num = 8
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(7)
        elif 714 < x < 781 and 650 < y < 710:
            num = 9
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(8)
        elif 781 < x < 870 and 650 < y < 710:
            num = 10
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(9)
        elif 124 < x < 174 and 590 < y < 660:
            num = 11
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(10)
        elif  199 < x < 244 and 590 < y < 660:
            num = 12
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(11)
        elif 277 < x < 320 and 590 < y < 660:
            num = 13
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(12)
        elif 354 < x < 392 and 590 < y < 660:
            num = 14
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(13)
        elif 409 < x < 485 and 590 < y < 660:
            num = 15
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(14)
        elif 485 < x < 560 and 590 < y < 660:
            num = 16
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(15)
        elif 560 < x < 633 and 590 < y < 660:
            num = 17
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(16)
        elif 633 < x < 714 and 590 < y < 660:
            num = 18
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(17)
        elif 714 < x < 781 and 590 < y < 660:
            num = 19
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(18)
        elif 781 < x < 870 and 590 < y < 660:
            num = 20
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(19)
        elif 124 < x < 174 and 530 < y < 590:
            num = 21
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(20)
        elif  199 < x < 244 and 530 < y < 590:
            num = 22
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(21)
        elif 277 < x < 320 and 530 < y < 590:
            num = 23
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(22)
        elif 354 < x < 392 and 530 < y < 590:
            num = 24
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(23)
        elif 409 < x < 485 and 530 < y < 590:
            num = 25
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(24)
        elif 485 < x < 560 and 530 < y < 590:
            num = 26
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(25)
        elif 560 < x < 633 and 530 < y < 590:
            num = 27
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(26)
        elif 633 < x < 714 and 530 < y < 590:
            num = 28
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(27)
        elif 714 < x < 781 and 530 < y < 590:
            num = 29
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(28)
        elif 781 < x < 870 and 530 < y < 590:
            num = 30
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(29)
        elif 124 < x < 174 and 470 < y < 530:
            num = 31
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(30)
        elif 199 < x < 244 and 470 < y < 530:
            num = 32
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(31)
        elif 277 < x < 320 and 470 < y < 530:
            num = 33
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(32)
        elif 354 < x < 392 and 470 < y < 530:
            num = 34
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(33)
        elif 409 < x < 485 and 470 < y < 530:
            num = 35
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(34)
        elif 485 < x < 560 and 470 < y < 530:
            num = 36
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(35)
        elif 560 < x < 633 and 470 < y < 530:
            num = 37
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(36)
        elif 633 < x < 714 and 470 < y < 530:
            num = 38
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(37)
        elif 714 < x < 781 and 470 < y < 530:
            num = 39
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(38)
        elif 781 < x < 870 and 470 < y < 530:
            num = 40
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(39)
        elif 124 < x < 174 and 410 < y < 470:
            num = 41
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(40)
        elif  199 < x < 244 and 410 < y < 470:
            num = 42
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(41)
        elif 277 < x < 320 and 410 < y < 470:
            num = 43
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(42)
        elif 354 < x < 392 and 410 < y < 470:
            num = 44
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(43)
        elif 409 < x < 485 and 410 < y < 470:
            num = 15
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(44)
        elif 485 < x < 560 and 410 < y < 470:
            num = 16
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(45)
        elif 560 < x < 633 and 410 < y < 470:
            num = 47
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(46)
        elif 633 < x < 714 and 410 < y < 470:
            num = 48
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(47)
        elif 714 < x < 781 and 410 < y < 470:
            num = 49
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(48)
        elif 781 < x < 870 and 410 < y < 470:
            num = 50
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(49)
        elif 124 < x < 174 and 350 < y < 410:
            num = 51
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(50)
        elif  199 < x < 244 and 350 < y < 410:
            num = 52
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(51)
        elif 277 < x < 320 and 350 < y < 410:
            num = 53
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(52)
        elif 354 < x < 392 and 350 < y < 410:
            num = 54
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(53)
        elif 409 < x < 485 and 350 < y < 410:
            num = 55
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(54)
        elif 485 < x < 560 and 350 < y < 410:
            num = 56
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(55)
        elif 560 < x < 633 and 350 < y < 410:
            num = 57
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(56)
        elif 633 < x < 714 and 350 < y < 410:
            num = 58
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(57)
        elif 714 < x < 781 and 350 < y < 410:
            num = 59
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(58)
        elif 781 < x < 870 and 350 < y < 410:
            num = 60
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(59)
        elif 124 < x < 174 and 290 < y < 350:
            num = 61
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(60)
        elif  199 < x < 244 and 290 < y < 350:
            num = 62
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(61)
        elif 277 < x < 320 and 290 < y < 350:
            num = 63
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(62)
        elif 354 < x < 392 and 290 < y < 350:
            num = 64
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(63)
        elif 409 < x < 485 and 290 < y < 350:
            num = 65
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(64)
        elif 485 < x < 560 and 290 < y < 350:
            num = 66
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(65)
        elif 560 < x < 633 and 290 < y < 350:
            num = 67
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(66)
        elif 633 < x < 714 and 290 < y < 350:
            num = 68
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(67)
        elif 714 < x < 781 and 290 < y < 350:
            num = 69
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(68)
        elif 781 < x < 870 and 290 < y < 350:
            num = 70
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(69)
        elif 124 < x < 174 and 230 < y < 290:
            num = 71
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(70)
        elif  199 < x < 244 and 230 < y < 290:
            num = 72
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(71)
        elif 277 < x < 320 and 230 < y < 290:
            num = 73
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(72)
        elif 354 < x < 392 and 230 < y < 290:
            num = 74
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(73)
        elif 409 < x < 485 and 230 < y < 290:
            num = 75
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(74)
        elif 485 < x < 560 and 230 < y < 290:
            num = 76
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(75)
        elif 560 < x < 633 and 230 < y < 290:
            num = 77
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(76)
        elif 633 < x < 714 and 230 < y < 290:
            num = 78
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(77)
        elif 714 < x < 781 and 230 < y < 290:
            num = 79
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(78)
        elif 781 < x < 870 and 230 < y < 290:
            num = 80
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(79)
        if 124 < x < 174 and 170 < y < 230:
            num = 81
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(80)
        elif  199 < x < 244 and 170 < y < 230:
            num = 82
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(81)
        elif 277 < x < 320 and 170 < y < 230:
            num = 83
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(82)
        elif 354 < x < 392 and 170 < y < 230:
            num = 84
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(83)
        elif 409 < x < 485 and 170 < y < 230:
            num = 85
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(84)
        elif 485 < x < 560 and 170 < y < 230:
            num = 86
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(85)
        elif 560 < x < 633 and 170 < y < 230:
            num = 87
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(86)
        elif 633 < x < 714 and 170 < y < 230:
            num = 88
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(87)
        elif 714 < x < 781 and 170 < y < 230:
            num = 89
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(88)
        elif 781 < x < 870 and 170 < y < 230:
            num = 90
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(89)
        if 124 < x < 174 and 110 < y < 170:
            num = 91
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(90)
        elif 199 < x < 244 and 110 < y < 170:
            num = 92
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(91)
        elif 277 < x < 320 and 110 < y < 170:
            num = 93
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(92)
        elif 354 < x < 392 and 110 < y < 170:
            num = 94
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(93)
        elif 409 < x < 485 and 110 < y < 170:
            num = 95
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(94)
        elif 485 < x < 560 and 110 < y < 170:
            num = 96
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(95)
        elif 560 < x < 633 and 110 < y < 170:
            num = 97
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(96)
        elif 633 < x < 714 and 110 < y < 170:
            num = 98
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(97)
        elif 714 < x < 781 and 110 < y < 170:
            num = 99
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(98)
        elif 781 < x < 870 and 110 < y < 170:
            num = 100
            if num == rand_num:
                wri.clear()
                write("Play Again?\n\nYES        NO", 50, 500, 500)
                guess = False
                again = True
            elif num < rand_num:
                hilo.clear()
                high_low("Too Low")
            elif num > rand_num:
                hilo.clear()
                high_low("Too High")
                num_board(99)
    if again:
        if 368 < x < 481 and 500 < y < 563:
            again = False
            start = True
        elif 543 < x < 627 and 500 < y < 563:
            wn.exitonclick()
    wn.onscreenclick(game)


def high_low(highlow):
    hilo.up()
    hilo.shape("blank")
    hilo.goto(500, 750)
    hilo.write(highlow, move=False, align="center", font=("Arial", 50, "normal"))


def randnum():
    global rand_num
    rand_num = random.randint(1, 100)
    print rand_num


def main():
    wn.setworldcoordinates(0, 0, 1000, 1000)
    randnum()
    startup()
    wn.onscreenclick(game)
    turtle.done()

main()
