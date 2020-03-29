#!us/bin/python3.7
from tkinter import * #從tkinter import所有元件


if __name__ == "__main__":  #程式進入點
    window = Tk() #建立視窗
    #所有程式碼需寫在這中間
    window.title("LED Control")
    window.geometry("300x200")
    Button(window, text="Press").pack(expand=YES, fill=BOTH, padx=5, pady=20)
    
    window.mainloop() 