import pygame
import sys
import os
import random
import datetime
from datetime import date
# from pygame import mixer

pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 120

color_white = (255, 255, 255)
color_light = (180, 180, 180)
color_dark = (110, 110, 110)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

black = (0, 0, 0)
cclr = (240, 240, 240)
# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
font = pygame.font.Font('freesansbold.ttf', 22)

# TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

window = pygame.display.set_mode((WIDTH, HEIGHT))
width = window.get_width()
height = window.get_height()

img = pygame.image.load("img/atm_intro.jpg")
window.blit(img, [0, 0])

clock = pygame.time.Clock()

# font = pygame.font.SysFont("Arial", 24)

# **************************************************************
loaded: bool = False
bal1 = random.randrange(1000, 100000, 100)
bal2 = random.randrange(100, 50000, 1)
onlyback = False
inputmode = False
cashSTR = ""
cashSUM = 0
depoSUM1 = 0
proctyp = 0
cashTOTAL = 0


# ************************PROCEDURES***************************

def clk(btn):
    pygame.mixer.init()

    if btn == 1:
        pygame.mixer.music.load("sounds/numbtn.mp3")
    if btn == 2:
        pygame.mixer.music.load("sounds/scrbtn.mp3")
    if btn == 3:
        pygame.mixer.music.load("sounds/Entbtn.mp3")
    if btn == 4:
        pygame.mixer.music.load("sounds/card_in.mp3")
    if btn == 5:
        pygame.mixer.music.load("sounds/cash_snd.mp3")
    if btn == 6:
        pygame.mixer.music.load("sounds/chkprn.mp3")
    if btn == 7:
        pygame.mixer.music.load("sounds/card_out.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()


def exit_menu():
    img = pygame.image.load("img/atm_intro.jpg")
    window.blit(img, [0, 0])


# ***************************MENU_DRAWING***********************************
def rect_proc(t1, t2, t3, t4):
    text1 = font.render(t1, True, blue, white)
    text2 = font.render(t2, True, blue, white)
    text3 = font.render(t3, True, blue, white)
    text4 = font.render(t4, True, blue, white)

    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect4 = text4.get_rect()

    textRect1.center = (340, 275)
    textRect2.center = (340, 320)
    textRect3.center = (340, 370)
    textRect4.center = (340, 420)

    img = pygame.image.load("img/atm.jpg")

    inputmode = True

    window.blit(img, [0, 0])

    window.blit(text1, textRect1)
    window.blit(text2, textRect2)
    window.blit(text3, textRect3)
    window.blit(text4, textRect4)

    pygame.display.update()


# **************************************************************************
def main_menu():
    tt1 = 'Account information      Balance'
    tt2 = 'Withdraw Cash                 Deposit'
    tt3 = 'Pin Change         Print Statement'
    tt4 = 'Transfer                                   Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False


def AccInfo():
    tt1 = 'Account:         7445821454819'
    tt2 = 'Credit limit:                  ' + str(bal2) + ' $'
    tt3 = 'Virtual card:    1234 5678 9000'
    tt4 = 'Print                                       Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False


def balance():
    tt1 = 'Account:       7445821454819'
    tt2 = 'Balance Inquiry:        ' + str(bal1) + ' $'
    tt3 = ' '
    tt4 = '                                             Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False


def withdraw():
    inputmode = True
    tt1 = 'Please select Amount'
    tt2 = '$50                                           $100'
    tt3 = '$200                                        $500'
    tt4 = '$1000                                       Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False
    # if inputmode == True:
    #     prnchek()


def pinchange():
    tt1 = 'PIN CODE CHANGE'
    tt2 = 'Please enter new PIN            '
    tt3 = 'The new Pin will be sent        '
    tt4 = '    to your e-mail.                   Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False


def deposit():
    global bal1
    s = True
    dep1 = ""

    tt1 = 'Account:        7445821454819'
    tt2 = 'Current Balance:        ' + str(bal1) + ' $'
    tt3 = 'Please enter deposit: '
    tt4 = '                                             Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False
    # input(depoSUM1)
    while s:
        for event in pygame.event.get():
            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    s = False
                if event.key == pygame.K_KP0:
                    dep1 = dep1 + str(0)
                if event.key == pygame.K_KP1:
                    dep1 = dep1 + str(1)
                if event.key == pygame.K_KP2:
                    dep1 = dep1 + str(2)
                if event.key == pygame.K_KP3:
                    dep1 = dep1 + str(3)
                if event.key == pygame.K_KP4:
                    dep1 = dep1 + str(4)
                if event.key == pygame.K_KP5:
                    dep1 = dep1 + str(5)
                if event.key == pygame.K_KP6:
                    dep1 = dep1 + str(6)
                if event.key == pygame.K_KP7:
                    dep1 = dep1 + str(7)
                if event.key == pygame.K_KP8:
                    dep1 = dep1 + str(8)
                if event.key == pygame.K_KP9:
                    dep1 = dep1 + str(9)
    bal1 = bal1 + int(dep1)


def statement():
    tt1 = 'Checks & debits:'
    tt2 = ' Deposits & credits:      '
    tt3 = 'Atm locations used:  '
    tt4 = '                                             Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False


def transfer():
    tt1 = ' Transfer money'
    tt2 = '   Enter amount of money :         '
    tt3 = ' Receiver Card:      '
    tt4 = '                               Back'
    rect_proc(tt1, tt2, tt3, tt4)
    onlyback = False


def prnchek():
    dt_now = datetime.datetime.now()  # Дату-Время(только дата)
    dt_now = date.today()
    font = pygame.font.Font('img/cour.ttf', 7)  # шрифт

    # ****_ЧекКККК_*************************
    tt1 = '     GOLDEN BANK'
    tt2 = 'ASTANAIT, C1.1.357K'
    tt3 = 'Tel: (177) 798-75-57'
    tt4 = 'ATM # 54287301'
    tt5 = 'CASH WITHDRAWAL'
    tt6 = 'DATE:' + str(dt_now)
    tt7 = 'CARD # 1234 5678 9000'
    tt8 = 'AVAILABLE AMOUNT:'
    tt9 = '   +' + str(bal1) + ' $'
    tt10 = 'TOTAL:  ' + str(cashTOTAL) + ' USD'
    tt11 = 'THANK YOU VERY MUCH!'
    tt12 = '75+ point pls'
    tt13 = '**********************'
    tt14 = '  WWW.GOLDENBANK.COM'

    text1 = font.render(tt1, True, black, cclr)
    text2 = font.render(tt2, True, black, cclr)
    text3 = font.render(tt3, True, black, cclr)
    text4 = font.render(tt4, True, black, cclr)
    text5 = font.render(tt5, True, black, cclr)
    text6 = font.render(tt6, True, black, cclr)
    text7 = font.render(tt7, True, black, cclr)
    text8 = font.render(tt8, True, black, cclr)
    text9 = font.render(tt9, True, black, cclr)
    text10 = font.render(tt10, True, black, cclr)
    text11 = font.render(tt11, True, black, cclr)
    text12 = font.render(tt12, True, black, cclr)
    text13 = font.render(tt13, True, black, cclr)
    text14 = font.render(tt14, True, black, cclr)

    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()
    textRect3 = text3.get_rect()
    textRect4 = text4.get_rect()
    textRect5 = text5.get_rect()
    textRect6 = text6.get_rect()
    textRect7 = text7.get_rect()
    textRect8 = text8.get_rect()
    textRect9 = text9.get_rect()
    textRect10 = text10.get_rect()
    textRect11 = text11.get_rect()
    textRect12 = text12.get_rect()
    textRect13 = text13.get_rect()
    textRect14 = text14.get_rect()

    textRect1.midleft = (620, 415)
    textRect2.midleft = (620, 425)
    textRect3.midleft = (620, 442)
    textRect4.midleft = (620, 458)
    textRect5.midleft = (620, 474)
    textRect6.midleft = (620, 490)
    textRect7.midleft = (620, 506)
    textRect8.midleft = (620, 522)
    textRect9.midleft = (620, 538)
    textRect10.midleft = (620, 554)
    textRect11.midleft = (620, 570)
    textRect12.midleft = (620, 586)
    textRect13.midleft = (620, 602)
    textRect14.midleft = (620, 618)

    img = pygame.image.load("img/atm_check.jpg")

    window.blit(img, [0, 0])

    window.blit(text1, textRect1)
    window.blit(text2, textRect2)
    window.blit(text3, textRect3)
    window.blit(text4, textRect4)
    window.blit(text5, textRect5)
    window.blit(text6, textRect6)
    window.blit(text7, textRect7)
    window.blit(text8, textRect8)
    window.blit(text9, textRect9)
    window.blit(text10, textRect10)
    window.blit(text11, textRect11)
    window.blit(text12, textRect12)
    window.blit(text13, textRect13)
    window.blit(text14, textRect14)

    pygame.display.update()
    onlyback = False

    clk(5)
    pygame.time.wait(1000)
    clk(6)
    pygame.time.wait(1000)
    clk(7)

    # *******_Пауза 10 сек и завершение сеанса_*****************
    pygame.time.wait(10000)

    pygame.quit()
    quit(0)


# **************************************************************

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            x, y = pygame.mouse.get_pos()
            #print("Mouse position: ({}, {})".format(x, y))

    # *****************CARD_Button************************************
    if event.type == pygame.MOUSEBUTTONDOWN:
        if loaded == False:
            if 617 <= mouse[0] <= 709 and 330 <= mouse[1] <= 488:
                clk(4)
                loaded = True
                pygame.time.wait(4000)
                main_menu()
            # window.fill((0, 0, 0))
    # *****************Enter_Button***********************************
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 422 <= mouse[0] <= 486 and 650 <= mouse[1] <= 668:
            clk(3)
            prnchek()
        # window.fill((0, 0, 0))

    # *****************Clear_Button***********************************
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 422 <= mouse[0] <= 488 and 682 <= mouse[1] <= 698:
            clk(3)
            # pygame.quit()
            cashSUM = 0
        # window.fill((0, 0, 0))

    # *****************Cancel Button***********************************
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 424 <= mouse[0] <= 490 and 713 <= mouse[1] <= 729:
            clk(3)

            pygame.quit()
            quit(0)
    # window.fill((0,0,0))

    # if event.type == pygame.MOUSEBUTTONUP:
    #     if 424 <= mouse[0] <= 490 and 713 <= mouse[1] <= 729:

    # pygame.quit()
    # window.fill((0,0,0))

    # =============DISPLAY_SIDE_BUTTONS_EVENT_HANDLER====================================
    # 00000000000000000000000000000000000000000000000000000000000000000000000000000000000
    # 00000000000000000000000000000000000000000000000000000000000000000000000000000000000
    # 00000000000000000000000000000000000000000000000000000000000000000000000000000000000
    if event.type == pygame.MOUSEBUTTONDOWN:  # Left-1
        if 120 <= mouse[0] <= 157 and 260 <= mouse[1] <= 287:
            clk(2)

            if onlyback == False:
                AccInfo()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Left-2
        if 120 <= mouse[0] <= 157 and 309 <= mouse[1] <= 335:
            clk(2)
            cashTOTAL = 50
            if onlyback == False:
                # proctyp = 3
                withdraw()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Left-3
        if 117 <= mouse[0] <= 155 and 357 <= mouse[1] <= 381:
            clk(2)
            cashTOTAL = 200
            if onlyback == False:
                # proctyp = 3
                pinchange()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Left-4
        if 117 <= mouse[0] <= 153 and 403 <= mouse[1] <= 429:
            clk(2)
            cashTOTAL = 1000
            if onlyback == False:
                # proctyp = 3
                transfer()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Right-1
        if 525 <= mouse[0] <= 565 and 260 <= mouse[1] <= 285:
            clk(2)
            if onlyback == False:
                balance()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Right-2
        if 527 <= mouse[0] <= 567 and 307 <= mouse[1] <= 337:
            clk(2)
            cashTOTAL = 100
            if onlyback == False:
                # proctyp = 3
                deposit()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Right-3
        if 530 <= mouse[0] <= 567 and 355 <= mouse[1] <= 381:
            clk(2)
            cashTOTAL = 500
            if onlyback == False:
                # proctyp = 3
                statement()
                onlyback = True
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Right-4
        if 527 <= mouse[0] <= 569 and 403 <= mouse[1] <= 429:
            clk(2)
            if onlyback == True:
                main_menu()
                onlyback = False
                # window.fill((0,0,0))
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # =============NUMERIC_BUTTONS_EVENT_HANDLER=========================================
    if event.type == pygame.MOUSEBUTTONDOWN:  # Zero
        if 258 <= mouse[0] <= 308 and 743 <= mouse[1] <= 763:
            clk(1)
            # pygame.quit()
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Triple_Zero
        if 424 <= mouse[0] <= 494 and 743 <= mouse[1] <= 763:
            clk(1)
            # pygame.quit()
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # One
        if 196 <= mouse[0] <= 242 and 650 <= mouse[1] <= 668:
            clk(1)
            #if inputmode == True:
                #cashSTR = cashSTR + "1"
                #cashSUM = str(cashSTR)
                # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Two
        if 266 <= mouse[0] <= 315 and 650 <= mouse[1] <= 668:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Three
        if 338 <= mouse[0] <= 386 and 650 <= mouse[1] <= 668:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Four
        if 190 <= mouse[0] <= 238 and 680 <= mouse[1] <= 698:
            clk(1)
            # pygame.quit()
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Five
        if 264 <= mouse[0] <= 312 and 680 <= mouse[1] <= 698:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Six
        if 338 <= mouse[0] <= 386 and 680 <= mouse[1] <= 698:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Seven
        if 186 <= mouse[0] <= 234 and 713 <= mouse[1] <= 729:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Eight
        if 262 <= mouse[0] <= 310 and 713 <= mouse[1] <= 729:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # Nine
        if 336 <= mouse[0] <= 386 and 713 <= mouse[1] <= 729:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # UP
        if 180 <= mouse[0] <= 230 and 743 <= mouse[1] <= 763:
            clk(1)
    # window.fill((0,0,0))
    if event.type == pygame.MOUSEBUTTONDOWN:  # DOWN
        if 334 <= mouse[0] <= 386 and 743 <= mouse[1] <= 763:
            clk(1)
    # window.fill((0,0,0))
    # ===================================================================================

    mouse = pygame.mouse.get_pos()  #получаем координаторы курсора

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit(0)