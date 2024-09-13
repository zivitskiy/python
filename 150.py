arr: list = []

def check() -> int | None:
    for i in range(9):
        if arr[i+1] == arr[0]:
            flag: int = int(i + 1)
            return flag

def main() -> None:
    for _ in range(10):
        arr.append(int(input("Введіть елемент списку: ")))
    print(arr)
    if check() > 0:
        print(check())
    else:
        print("Елемент не існує")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
