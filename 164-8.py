arr: list[str] = []

def main() -> None:
    while True:
        arr.append(str(input("Введіть слово: ")))
        arr.sort()

        for el in arr:
            print(el)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
