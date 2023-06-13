from tkinter import *

import tkinter.messagebox
tk = Tk()
tk.title("TATI By Fwldom")

click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "p"
        click = True

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
          button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
          button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
          button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
          button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
          button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
          button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
          button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
          tkinter.messagebox.showinfo("Winner X", " X Win game")


    elif (button1["text"] == "p" and button2["text"] == "p" and button3["text"] == "p" or
            button4["text"] == "p" and button5["text"] == "p" and button6["text"] == "p" or
            button7["text"] == "p" and button8["text"] == "p" and button9["text"] == "p" or
            button3["text"] == "p" and button5["text"] == "p" and button7["text"] == "p" or
            button1["text"] == "p" and button5["text"] == "p" and button9["text"] == "p" or
            button1["text"] == "p" and button4["text"] == "p" and button7["text"] == "p" or
            button2["text"] == "p" and button5["text"] == "p" and button8["text"] == "p" or
            button3["text"] == "p" and button6["text"] == "p" and button9["text"] == "p"):
            tkinter.messagebox.showinfo("Winner P", "P Win game")

buttons=StringVar()

button1 = Button(tk,text= " " ,font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button1))

button1.grid(row=1, column=0, sticky = S+N+E+W)

button2 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button2))

button2.grid(row = 1, column =1, sticky = S+N+E+W)

button3 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button3))

button3.grid(row = 1, column =2, sticky = S+N+E+W)
    
button4 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command =lambda:checker(button4))
    
button4.grid(row = 2, column =0, sticky = S+N+E+W)

button5 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button5))

button5.grid(row = 2, column =1, sticky = S+N+E+W)

button6 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button6))

button6.grid(row = 2, column =2, sticky = S+N+E+W)

button7 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button7))

button7.grid(row = 3, column =0, sticky = S+N+E+W)

button8 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button8))

button8.grid(row = 3, column =1, sticky = S+N+E+W)
    
button9 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button9))

button9.grid(row = 3, column =2, sticky = S+N+E+W)

tk.mainloop() 
