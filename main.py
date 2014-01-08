from Tkinter import *
import random

top = Tk()

def random_answer():
    return word_list[random.randint(0,len(word_list)-1)]

def make_list():
    word_list = []
    with open('english-words.10') as f:
        for line in f:
            line = line[:-1]
            word_list.append(line)
    return word_list

def make_guess():
    string = guess.get()
    while len(guess.get())>0:
        guess.delete(0)
    if len(string) == 1 and string not in GuessedVar.get()[9:]:
        process_guess(string)
        GuessedVar.set(GuessedVar.get() + string)
    else:
        # Pop up a window that informs user of how to make a guess
        pass

def process_guess(string):
    displayed_answer_string = displayed_answer.get()
    i = 0
    if string in answer.get():
        for char in answer.get():
            if char == string:
                displayed_answer.set(displayed_answer_string[:i] + answer.get()[i] + displayed_answer_string[i+1:])
                displayed_answer_string = displayed_answer.get()
                win_check()
            i += 1
    else:
        miss()

def win_check():
    if displayed_answer.get() == answer.get():
        win_window = Toplevel()
        win_message = Label(win_window, text="You Win!")
        win_button = Button(win_window, text="Like a BAWS", command=lambda:reset_game(win_window))
        win_message.grid(row=0)
        win_button.grid(row=1)

def miss():
    x = misses.get()
    x += 1
    misses.set(x)
    if misses.get() == 1:
        head = hm_display.create_oval(185,70,265,150) #Head
        canvas_id_list.append(head)
    elif misses.get() == 2:
        body = hm_display.create_line(225,150,225,280) #Body
        canvas_id_list.append(body)
    elif misses.get() == 3:
        larm = hm_display.create_line(225,200,175,200) #L Arm
        canvas_id_list.append(larm)
    elif misses.get() == 4:
        rarm = hm_display.create_line(225,200,275,200) #R Arm
        canvas_id_list.append(rarm)
    elif misses.get() == 5:
        lleg = hm_display.create_line(225,280,175,350) #L Leg
        canvas_id_list.append(lleg)
    elif misses.get() == 6:
        rleg = hm_display.create_line(225,280,275,350) #R Leg
        canvas_id_list.append(rleg)
        loser()

def loser():
    lose_window = Toplevel()
    lose_message = Label(lose_window, text="You Lose!")
    lose_button = Button(lose_window, text="Aw man =[", command=lambda:reset_game(lose_window))
    lose_message.grid(row=0)
    lose_button.grid(row=1)

def reset_game(window=None):
    misses.set(0)
    answer.set(random_answer())
    displayed_answer.set(hyphonify(answer.get()))
    GuessedVar.set('Guessed: ')
    global canvas_id_list
    for ID in canvas_id_list:
        hm_display.delete(ID)
    canvas_id_list = []
    if window:
        window.destroy()

def hyphonify(string):
    return_string = '-'*(len(string))
    return return_string

global word_list
word_list = make_list()

global canvas_id_list
canvas_id_list = []

misses = IntVar()
answer = StringVar()
displayed_answer = StringVar()
GuessedVar = StringVar()
reset_game()

answer_lab = Label(top, textvariable=displayed_answer)
answer_lab.grid(column=1,row=2)

hm_display = Canvas(top, bg='white', height=400, width=400)
hm_display.create_line(20,380,380,380) #Base
hm_display.create_line(70,380,70,50,225,50,225,70) #Frame
hm_display.grid(column=1,row=1,columnspan=2)

guess = Entry(top)
guess.grid(column=1,row=3)

submit = Button(top, text='OK', command=make_guess)
submit.grid(column=2,row=3)

guessed = Label(top, textvariable=GuessedVar)
guessed.grid(column=1,row=0)

top.mainloop()
