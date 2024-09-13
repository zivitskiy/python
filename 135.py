from tkinter import *
from tkinter import messagebox
from random import randint

root: Tk = Tk()

txtvar: StringVar = StringVar()

arr: list = []

def click() -> None:
    n: int = int(txtvar.get())
    sl = ""
    for i in range(n):
        arr.append(randint(1, 10))
        sl: str = sl + str(arr[i]) + ''
        messagebox.showinfo(f'Результат: {sl}')

def main() -> None:
    label: Label = Label(text='Введіть кількість елементів:')
    label.pack()

    entry: Entry = Entry(root, textvariable=txtvar)
    entry.pack()

    btn: Button = Button(text='Розпочати', command=click)
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
