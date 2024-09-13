arr: list[int] = []

def main() -> None:
    for i in range(10):
        arr.append(int(input("Введіть елемент списку: ")))
        arr[i] = arr[1]**2

    print(arr)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
