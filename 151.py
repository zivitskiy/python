arr: list = []

def get() -> None:
    for _ in range(24):
        arr.append(float(input("Отримана температура: ")))


def main() -> None:
    k: int = 0
    get()
    for i in range(1, 24):
        if arr[i] == arr[0]:
            k += 1
    print(k)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
