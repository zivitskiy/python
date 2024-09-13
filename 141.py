from random import randint

arr: list[int] = []

def main() -> None:
    r: int = int(input("Введіть значення особистого рекорду: "))
    for i in range(10):
        arr.append(randint(r-10, 194))
        if arr[i] < r:
            arr[i] = 0

    print(arr)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
