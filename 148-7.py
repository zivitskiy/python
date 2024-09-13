from random import randint

arr: list[int] = []

def retrieve() -> None:
    for _ in range(8):
        arr.append(randint(-30, 30))

def main() -> None:
    retrieve()
    pos: int= sum([num for num in arr if num > 0])
    neg: int = len([num for num in arr if num < 0])
    print(f"Сума додатніх чисел: {pos}\nСума відʼємних чисел: {neg}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

