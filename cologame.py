from tkinter import *
import random
import time
import datetime

window = Tk()
window.geometry("800x600")
window.title("Welcome to Brain Game ")

colors = ['red','blue','green','pink','black','yellow','orange',
          'white','brown']
score = 0
timeleft = 30

# Adding Date & Time
qtime = Frame(window)
qtime.pack()
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(qtime, font=('arial', 20, 'bold'),
                                text=localtime,
                                fg="Steel Blue",
                                bd=10,
                                anchor='w')
lblInfo.grid(row=1, column=0)
#-----------------------------------------------------------------------------------------------------------------------

def NewWindow():
    # Exit Function both pop-up Window
        window.destroy()
#-----------------------------------------------------------------------------------------------------------------------
# function that will start the game
def startGame(event):
    if timeleft == 30:
        # start the countdown timer
        countdown()

    # function to choose the next color
    nextColor()

#-----------------------------------------------------------------------------------------------------------------------
# function to choose and display the next color
def nextColor():
    global score
    global timeleft

    if timeleft > 0:

        # make the text entry box active
        entry.focus_set()

        # if the typed color is equal to the color of the text
        if entry.get().lower() == colors[1].lower():
            score += 1

        # clear the text entry box
        entry.delete(0, END)

        random.shuffle(colors)

        # change the color to type by changing the text and the color to a random value
        label.config(fg=str(colors[1]), text = str(colors[0]))

        # update the score
        scoreLabel.config(text = "Score:" + str(score))

#-----------------------------------------------------------------------------------------------------------------------
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:

        timeleft -= 1       # decrement by 1

    # update the time left label
    timeLable.config(text = "Time left:" + str(timeleft))

    # run the function again after 1 second
    timeLable.after(1000, countdown)
#-----------------------------------------------------------------------------------------------------------------------


welcome = Label(window,text = "▶▶ ᗯEᒪᑕOᗰE ◀◀",
                                font=('helvetica', 20, 'bold'),
                                fg="Black",
                                bd=10,
                                anchor='w')
welcome.pack()

instruction = Label(window,text = "Type in the color of the words, and not the word text:",
                                    font=('helvetica', 20, 'bold'),
                                    fg="Black",
                                    bd=10,
                                    anchor='w')
instruction.pack()

# Add a score label
scoreLabel = Label(window, text = "Press Enter Key to Start !",
                                    font=('helvetica', 20, 'bold'),
                                    fg="Black",
                                    bg = "green",
                                    bd=10,
                                    anchor='w')

scoreLabel.pack()

# adding left time label
timeLable = Label(window, text = "✺✺ ＴＩＭＥ  ＬＥＦＴ ✺✺:  " + str(timeleft))
timeLable.pack()

# adding a label for displaying the color
label = Label(window, font = ('Helvetica', 60))
label.pack()

# add a text entry box for typing in
entry = Entry(window, font=('arial', 16, 'bold'),
                                bd=10,
                                insertwidth=4,
                                bg="powder blue",
                                justify='right')

# run the "startgame" function when the enter key is pressed
window.bind('<Return>', startGame)
entry.pack()

# set focus on the entry box
entry.focus_set()

# Exit button
down_frame = Frame(window)
down_frame.pack()
closebutton = Button(down_frame, padx=12,
                                        pady=2,
                                        bd=16,
                                        fg="black",
                                        font=('arial', 16, 'bold'),
                                        width=10,
                                        text = "CLOSE",
                                        command=NewWindow)
closebutton.pack(side = "bottom")


window.mainloop()
