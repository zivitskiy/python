from random import randint

def retrieve() -> list:
    w: int = 5
    l: int = 3
    arr: list = [randint(50, 150) for _ in range(l)]
    return arr

def main() -> None:
    retrieve()
    print("Навантаження на одну лінію:", retrieve())
    print("Сумарне навантаження:", sum(retrieve()))

if __name__ == "__main__":
    main()
