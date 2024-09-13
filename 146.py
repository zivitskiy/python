import random


arr: list = []
s: int = 0

def main() -> None:
    for i in range(10):
        arr.append(round(random.random() + 9.0, 2))
        s: None | int = s + arr[i]

    s = s / 10

    print(arr)
    print(round(s, 2))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
