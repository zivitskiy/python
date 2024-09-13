from random import randint

arr: list[int] = []

def retrieve() -> None:
    for _ in range(7):
        arr.append(randint(1, 10))

def custom(l) -> list[int]:
    desc: list[int] = sorted(l, reverse=True)
    asc: list[int] = sorted(l)

    return desc + asc

def main() -> None:
    retrieve()

    custom(arr)
    print(arr)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

