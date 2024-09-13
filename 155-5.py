from random import randint

arr: list[int] = []

def retrieve() -> None:
    for _ in range(7):
        arr.append(randint(2, 13))

def main() -> None:
    retrieve()
    print(f"Найбільша температура за тиждень: {max(arr)}; найменша: {min(arr)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
