import tkinter as tk
from designPatterns.StatePattern.Phone import Phone

phone = Phone()


def Home():
    print(phone.get_state.home())


def OffOn():
    print(phone.get_state.onOffOn())


root = tk.Tk()
root.title("Phone Example")
root.geometry("300x500")

button1 = tk.Button(root, text="Home", command=Home)
button1.pack(pady=20)

button2 = tk.Button(root, text="OffOn", command=OffOn)
button2.pack(pady=20)

root.mainloop()
