from random import randint

arr: list[int] = []

def retrieve() -> None:
    for _ in range(10):
        arr.append(randint(1, 100))

def main() -> None:
    retrieve()
    cond = 40
    for el in arr:
        if el > cond:
            print("Елемент підходить під умову [елемент > 40]")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

