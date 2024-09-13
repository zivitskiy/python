arr: list[float] = [0, 5.5, 21.5, 60.5, 4.3, 45.1]

def check() -> int:
    n: int = arr.index(max(arr))
    if arr[0] == 0:
        k: int = n * 2

    elif arr[0] == -1:
        k = n * 2 - 1

    return k

def main() -> None:
    print("Номер будинку: ", check())

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
