from tkinter import *

click = 0
def click_button():
    global click
    click += 1
    root.title("Working")
    #BtnText.set("Clicks {}".format(click))
    btn1.config(text = "Clicks {}".format(click))
    lbl2.config(text = "work")
    #lbl2.pack(side = BOTTOM)

root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")

BtnText = StringVar()
#BtnText.set("Hello it is {}".format(click))

lbl1 = Label(root, text = 'Hello', font = 14)
lbl1.pack(side = TOP)

lbl2 = Label(root, text = 'Hello', font = 14)
lbl2.pack(side = BOTTOM)


btn1 = Button(root,text="Hello", font="12", command = click_button )

#btn1.pack(side = TOP)
btn1.place(relx = 0.5, rely = 0.5, height = 30, width = 130, anchor = 'c')

btn2 = Button(root,text="Left", font="12")

btn2.pack(side = LEFT)

btn3 = Button(root,text="Right", font="12")

btn3.pack(side = RIGHT)


mess = StringVar()
mess_entry = Entry(textvariable = mess)

root.mainloop()