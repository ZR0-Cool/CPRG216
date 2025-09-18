import random
import time
import os
import tkinter as tk
a = 0
b = 0
c = 0
n = True
e = 10
f = 15
g = 20
x = 2
k = 1
i = 10
m = 100
def slot1():
    global row1
    global a
    global e
    while e != 0:
        a = random.randint(1,9)
        e = e-1
        row1 = tk.Frame(slots, width=10, height=10, bg="white")
        row1.pack(side="left")
        break
def slot2():
    global row2
    global f
    global b
    while f != 0:
        b = random.randint(1,9)
        f = f-1
        row2 = tk.Frame(slots, width=10, height=10, bg="white")
        row2.pack()
        break
def slot3():
    global row3
    global g
    global c
    while g != 0:
        c = random.randint(1,9)
        g = g-1
        row3 = tk.Frame(window, width=10, height=10, bg="white")
        row3.pack(side="right")
        break
def money_lost():
    global m
    m = m-1
def output():
    global a,b,c
    print(a,b,c)
window = tk.Tk()
window.title("SLOTZ")
window.maxsize(250,250)
window.minsize(250,250)
slots = tk.Frame(window, width=190, height=50, bg="grey")
slots.pack()
row1 = tk.Frame(slots, width=10, height=10, bg="white")
row2 = tk.Frame(slots, width=10, height=10, bg="white")
row3 = tk.Frame(slots, width=10, height=10, bg="white")

def Spun():
    global row1,row2,row3
    row1.destroy()
    row2.destroy()
    row3.destroy()
    global a,b,c,d,e,f,g
    global m    
    
    Money = tk.Label(window, text=("money:",m))
    Money.pack()
    x = 2
    e = 10
    f = 15
    g = 20
    money_lost()
    while x != 0:
        i = 10
        while i >= 0:
            global a,b,c
            time.sleep(0.05)
            slot1()
            slot2()
            slot3()
            os.system('cls' if os.name == 'nt' else 'clear')
            output()
            i = i-1
        x = x-1
    if a == 7 and b == 7 and c == 7:
        print("$$$!!!JACKPOT!!!$$$")
        print("+100")
        m = m+100
        time.sleep(3)
    elif a+1 == b and b+1 == c or a == b == c:
        
        print("$$BIG WIN$$")
        print("+10")
        m = m+10
        time.sleep(1)
    elif a == c:
        print("+1")
        m = m+1
    
Spin = tk.Button(window, text="SPIN!", command=Spun)
Spin.pack(side="bottom")
window.mainloop()