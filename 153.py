from random import randint

n: int = 9
max: int = 99

arr: list = []

def apply() -> None:
    for _ in range(1, max):
        arr.append(randint(1, max))

    print(arr)


def main() -> None:
    apply()
    mn: int = min(arr)
    print(mn)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

