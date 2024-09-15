from random import randint

def retrieve() -> list:
    arr: list = input().split()
    return arr

def main() -> None:
    arr: list = retrieve()

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    v: int = randint(1, 5)
    i: int = arr.count(v)

    print(v, i)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
