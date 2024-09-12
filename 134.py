from tkinter import *

root = Tk()

txtvar: StringVar = StringVar()

arr: list = []

def main() -> None:
    usr: int = int(txtvar.get())
    for _ in range(usr):
        arr.append(usr)
        print(arr)

label: Label= Label(text='Введіть кількість елементів:')
label.pack()

entry: Entry = Entry(root, textvariable=txtvar)
entry.pack()

btn: Button = Button(root, text='Розпочати введення', command=main)
btn.pack()

root.mainloop()
