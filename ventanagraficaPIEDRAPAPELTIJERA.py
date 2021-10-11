import random
import tkinter as tk


window = tk.Tk()
window.geometry("400x300")
window.title("Piedra, Papel o Tijera")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOISE = ""

def choice_to_number(choice):
    rps = {'Piedra':0, 'Papel':1, 'Tijera':2}
    return rps[choice]
def numbre_to_choice(number):
    rps ={0: 'Piedra', 1: 'Papel', 2:'Tijera'}
    return rps[number]

def random_computer_choice():
    return random.choice(['Piedra', 'Papel', 'Tijera'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("EMPATE")
    elif((user-comp)%3==1):
        print("GANASTE")
        USER_SCORE+=1
    else:
        print("COMPUTADORA GANO")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(tk.END,answer)

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Piedra'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Papel'
    COMP_CHOICE= random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='Tijera'
    COMP_CHOICE=random_computer_choice() 
    result(USER_CHOICE,COMP_CHOICE)

button1 = tk.Button(text="       Piedra      ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Papel      ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="       Tijera    ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)

window.mainloop()
