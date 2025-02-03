from tkinter import * 
from tkinter import messagebox 
import base64 


screen = Tk() 
screen.geometry("375x398") 
screen.title("PctApp") 

def reset():
    code.set("")
    text1.delete(1.0, END)

def encrypt():
    global text1, code
    password = code.get()
    
    if password == "1234": 
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="Arial", fg="white", bg="#ed3833").place(x=10, y=0)
        
        text2 = Text(screen1, font=("Arial", 10), bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt)
    
    elif password == "": 
        messagebox.showerror("Encryption", "Input Password")
    
    else:  
        messagebox.showerror("Encryption", "Invalid Password")

def decrypt():
    global text1, code
    password = code.get()
    
    if password == "1234": 
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()  
        try:
            base64_bytes = base64.b64decode(message)
            decrypt = base64_bytes.decode("ascii")

            Label(screen2, text="DECRYPT", font="Arial", fg="white", bg="#00bd56").place(x=10, y=0)
            
            text2 = Text(screen2, font=("Arial", 10), bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypt)

        except Exception as e:
            messagebox.showerror("Decryption", "Invalid Encrypted Text")
    
    elif password == "": 
        messagebox.showerror("Decryption", "Input Password")
    
    else:  
        messagebox.showerror("Decryption", "Invalid Password")


Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10) 

text1 = Text(font=("Arial", 12), bg="white", relief=GROOVE, wrap=WORD, bd=0) 
text1.place(x=10, y=50, width=355, height=100) 

Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170) 

code = StringVar() 
Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200) 

Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250) 
Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250) 
Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300) 

screen.mainloop() 
