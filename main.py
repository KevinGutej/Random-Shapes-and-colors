from tkinter import *
import random

tk = Tk()
img = Canvas(tk, width=400, height=400)
img.pack()
colors = ["#2F00FF","#FF1100","#00FF00","#FB00FF","#6200FF","#FFFB00","#00FFDD"]

def random_squares(width):
    x1 = random.randrange(width)
    y1 = x1
    x2 = x1 + random.randrange(width)
    y2 = x2
    img.create_rectangle(x1, y1, x2, y2,outline=random.choice(colors))



def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    img.create_rectangle(x1, y1, x2, y2,outline=random.choice(colors))

def random_circle(width,height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    img.create_oval(x1,y1,x2,y2,outline=random.choice(colors))

def random_shapes(width,height):
    random_rectangle(width,height)
    random_circle(width,height)
    random_squares(width)



button = Button(tk, text ="rectangles", command=lambda:random_rectangle(400,400))
button.pack()
button2 = Button(tk, text ="squares", command=lambda:random_squares(400))
button2.pack()
button3 = Button(tk, text ="circles", command=lambda:random_circle(400,400))
button3.pack()
button4 = Button(tk, text ="All shapes", command=lambda:random_shapes(400,400))
button4.pack()



tk.mainloop()

# from tkinter import *
# import random
#
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
# colors = ["#2F00FF","#FF1100","#00FF00","#FB00FF","#6200FF","#FFFB00","#00FFDD"]
#
# def arc(degrees):
#     img.delete('all')
#     img.create_arc(10, 320, 200, 400,extent=degrees, style=ARC,outline=random.choice(colors))
#
#
#
#
# button = Button(tk, text ="45", command=lambda:arc(45))
# button.pack()
# button2 = Button(tk, text ="90", command=lambda:arc(90))
# button2.pack()
# button3 = Button(tk, text ="180", command=lambda:arc(180))
# button3.pack()
# button4 = Button(tk, text ="360", command=lambda:arc(360))
# button4.pack()
#
#
#
# tk.mainloop()

# from tkinter import *
# import random
#
# tk = Tk()
# img = Canvas(tk, width=400, height=400)
# img.pack()
#
#
# def good_morning():
#     img.delete('all')
#     img.create_text(130,120,text = "Good morning")
#
#
# def good_afternoon():
#     img.delete('all')
#     img.create_text(130, 120, text="Good afternoon")
#
#
# def good_evening():
#     img.delete('all')
#     img.create_text(130,120,text = "Good evening")
#
#
#
#
# button = Button(tk, text ="Good morning", command=good_morning)
# button.pack()
# button2 = Button(tk, text ="Good afternoon", command=good_afternoon)
# button2.pack()
# button3 = Button(tk, text ="Good evening",  command=good_evening)
# button3.pack()
#
# tk.mainloop()

# from tkinter import * #import tkinter all
#
# root = Tk()
# root.geometry("300x250")
# myLabel = Label(root, text="Wassup")# Label widget
# myLabel.pack()#pack putting it on the screen
#
# def good_morning():
#     myLabel.config(text="Good Morning!")
# def good_afternoon():
#     myLabel.config(text="Good Afternoon")
# def good_evening():
#     myLabel.config(text="Good Evening!")
#
# button1 = Button(root, text_="good morning", command=good_morning)
# button1.pack()
# button2 = Button(root, text_="good afternoon", command=good_afternoon)
# button2.pack()
# button3 = Button(root, text_="good evening", command=good_evening)
# button3.pack()
# root.mainloop()#gui loop