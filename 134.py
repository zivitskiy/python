from tkinter import *

root = Tk()

txtvar: StringVar = StringVar()

arr: list = []

def click() -> None:
    usr: int = int(txtvar.get())
    for _ in range(usr):
        arr.append(usr)
        print(arr)

def main() -> None:
    label: Label= Label(text='Введіть кількість елементів:')
    label.pack()

    entry: Entry = Entry(root, textvariable=txtvar)
    entry.pack()

    btn: Button = Button(root, text='Розпочати введення', command=click)
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
