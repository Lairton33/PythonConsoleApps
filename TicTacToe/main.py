from tkinter import *
from dum_mod import win_check


MARK = 'O'
indexes = ([],[])

root = Tk()


btn_width = 5
btn_height = btn_width // 2

title = Frame(root)

title_label = Label(title,text="Welcome To Tic-Tac-Toe",bg='#342D7C',fg='#15E1C5')

title_label.grid()
title.grid(row=0)


row1 = Frame(root)

row1_bnt1 = Button(row1,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(1))
row1_bnt2 = Button(row1,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(2))
row1_bnt3 = Button(row1,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(3))

row1_bnt1.grid(row=0,column=0)
row1_bnt2.grid(row=0,column=1)
row1_bnt3.grid(row=0,column=2)

row1.grid(row=1)

row2 = Frame(root)

row2_bnt1 = Button(row2,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(4))
row2_bnt2 = Button(row2,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(5))
row2_bnt3 = Button(row2,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(6))

row2_bnt1.grid(row=0,column=0)
row2_bnt2.grid(row=0,column=1)
row2_bnt3.grid(row=0,column=2)

row2.grid(row=2)

row3 = Frame(root)

row3_bnt1 = Button(row3,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(7))
row3_bnt2 = Button(row3,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(8))
row3_bnt3 = Button(row3,text='',width=btn_width,height=btn_height,bg='Black',fg='white',command=lambda :click(9))

row3_bnt1.grid(row=0,column=0)
row3_bnt2.grid(row=0,column=1)
row3_bnt3.grid(row=0,column=2)

row3.grid(row=3)

row4 = Frame(root)

l1 = Label(row4,text='X Is Your Time',width=18,background='Black',fg='yellow')

btn_exit = Button(row4,text='EXIT',width=18,bg='black',fg='blue',command= lambda: click(0))


l1.grid(row=0)
btn_exit.grid(row=1)

row4.grid(row=4)



def click(place_number):
    global MARK
    global indexes

    # How many places are already occupied.
    counter = len(set(indexes[0])) + len(set(indexes[1]))

    # Append to indexes array, check if place number is already into indexes, and check if someone has won.
    if (place_number not in indexes[0] and place_number not in indexes[1]) and (win_check(indexes) == 0):
        if MARK == 'X':        
            indexes[0].append(place_number)

        if MARK == 'O':
            indexes[1].append(place_number)
        
        # to place the mark (i.e. change the text of a button) 
        if place_number == 1:
            if MARK == 'X':
                row1_bnt1.config(text='O',)
                MARK = 'O'
            else:
                row1_bnt1.config(text='X',)
                MARK = 'X'

        if place_number == 2:
            if MARK == 'X':
                row1_bnt2.config(text='O',)
                MARK = 'O'
            else:
                row1_bnt2.config(text='X',)
                MARK = 'X'

        if place_number == 3:
            if MARK == 'X':
                row1_bnt3.config(text='O',)
                MARK = 'O'
            else:
                row1_bnt3.config(text='X',)
                MARK = 'X'
        
        if place_number == 4:
            if MARK == 'X':
                row2_bnt1.config(text='O',)
                MARK = 'O'
            else:
                row2_bnt1.config(text='X',)
                MARK = 'X'

        if place_number == 5:
            if MARK == 'X':
                row2_bnt2.config(text='O',)
                MARK = 'O'
            else:
                row2_bnt2.config(text='X',)
                MARK = 'X'

        if place_number == 6:
            if MARK == 'X':
                row2_bnt3.config(text='O',)
                MARK = 'O'
            else:
                row2_bnt3.config(text='X',)
                MARK = 'X'
            
        if place_number == 7:
            if MARK == 'X':
                row3_bnt1.config(text='O',)
                MARK = 'O'
            else:
                row3_bnt1.config(text='X',)
                MARK = 'X'
        
        if place_number == 8:
            if MARK == 'X':
                row3_bnt2.config(text='O',)
                MARK = 'O'
            else:
                row3_bnt2.config(text='X',)
                MARK = 'X'

        if place_number == 9:
            if MARK == 'X':
                row3_bnt3.config(text='O',)
                MARK = 'O'
            else:
                row3_bnt3.config(text='X',)
                MARK = 'X'

        # swap the mark
        mark = 'O' if MARK == 'X' else 'X'
        l1.config(text=f'{mark} is Your time!')

    # func coming from dum_mod module and will return ['x','o',0] 0 if nobody won yet
    if win_check(indexes) != 0:
        l1.config(text=f'{win_check(indexes).upper()} wins')
        
    # if there's more than 7 places occupied and nobody has won yet 
    if counter > 7:
        l1.config(text='It\'s a tie!')


    if place_number == 0:
        root.quit()


root.mainloop()