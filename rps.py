from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("400x400+450+70")
root.resizable(False,False)
root.title("GAME")

frame1 = Frame(root,height=140,width=400,bg="black")
frame1.place(x=0,y=0)
label = Label(frame1,text="ROCK | PAPER | SCISSOR",font="bold 17")
label.place(x=60,y=8)

d = {1:"ROCK",2:"PAPER",3:"SCISSOR"}
c,h = 0,0

def button(n,t):

    global h,c
    print(t)
    com = random.randint(1,3)
    human_opt.config(text=d[n])
    com_opt.config(text=d[com])

    if n==1:
        if com==1:
            pass
        elif com==2:
            c+=1
            com_score.config(text="COMPUTER: "+str(c))
        elif com==3:
            h+=1  
            human_score.config(text="HUMAN: "+str(h))
    elif n==2:
        if com==1:
            h+=1  
            human_score.config(text="HUMAN: "+str(h))
        elif com==2:
            pass
        elif com==3:
            c+=1
            com_score.config(text="COMPUTER: "+str(c))
    elif n==3:
        if com==1:
            c+=1
            com_score.config(text="COMPUTER: "+str(c))
        elif com==2:
            h+=1  
            human_score.config(text="HUMAN: "+str(h))
        elif com==3:
            pass
    if c==(t//2+1):
        messagebox.showinfo("GAME OVER","COMPUTER WON!!!")
        c=0;h=0
        com_score.config(text="COMPUTER: "+str(c))
        human_score.config(text="HUMAN: "+str(h))
        
    elif h==(t//2+1):
        messagebox.showinfo("GAME OVER","YOU WON!!!")
        c=0;h=0
        com_score.config(text="COMPUTER: "+str(c))
        human_score.config(text="HUMAN: "+str(h))


            
def mainloop(t):

    f.destroy()

    global frame2,frame3
    
    frame2 = Frame(root,height=240,width=190,bg="black")
    frame2.place(x=5,y=150)

    frame3 = Frame(root,height=240,width=190,bg="black")
    frame3.place(x=205,y=150)
    
    
    rock_button = Button(frame2,text="ROCK",font="bold 12",padx=29,pady=5,activebackground="black",activeforeground="blue",command=lambda:button(1,t))
    rock_button.place(x=35,y=40)
    paper_button = Button(frame2,text="PAPER",font="bold 12",padx=25,pady=5,activebackground="black",activeforeground="blue",command=lambda:button(2,t))
    paper_button.place(x=35,y=100)

    scissors_button = Button(frame2,text="SCISSOR",font="bold 12",padx=17,pady=5,activebackground="black",activeforeground="blue",command=lambda:button(3,t))
    scissors_button.place(x=35,y=160)

    computer = Label(frame3,text="COMPUTER:",font="bold 12")
    computer.place(x=43,y=35)

    human = Label(frame3,text="HUMAN:",font="bold 12")
    human.place(x=43,y=130)

    global human_opt,com_opt

    com_opt = Label(frame3,text="",font="bold 13")
    com_opt.place(x=43,y=75)

    human_opt = Label(frame3,text=" ",font="bold 13")
    human_opt.place(x=43,y=170)
def home():
    global f
    f = Frame(root,height=240,width=390,bg="black")
    f.place(x=5,y=150)

    l = Label(f,text="Choose the BEST OF",font="bold 15")
    l.place(x=90,y=28)

    b1 = Button(f,text="3",font="bold 12",padx=25,pady=5,activebackground="black",activeforeground="blue",command=lambda:mainloop(3))
    b1.place(x=55,y=105)

    b2 = Button(f,text="5",font="bold 12",padx=25,pady=5,activebackground="black",activeforeground="blue",command=lambda:mainloop(5))
    b2.place(x=155,y=105)

    b3 = Button(f,text="7",font="bold 12",padx=25,pady=5,activebackground="black",activeforeground="blue",command=lambda:mainloop(7))
    b3.place(x=255,y=105)

    c,h=0,0
    global com_score,human_score

    com_score = Label(frame1,text="COMPUTER: 0",font="bold 15")
    com_score.place(x=115,y=83)

    human_score = Label(frame1,text="HUMAN: 0",font="bold 15")
    human_score.place(x=275,y=83)

    score_label = Label(frame1,text="SCORE:",font="bold 15")
    score_label.place(x=15,y=82)



def back():
    frame2.destroy()
    frame3.destroy()
    home()
    

#Home button
b4 = Button(frame1,text="<-",font="bold 12",activebackground="black",bg="red",command=back)
b4.place(x=18,y=8)
home()
