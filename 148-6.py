arr: list[int] = []

def retrieve() -> None:
    for i in range(1, 9):
        arr.append(int(input(f"Введіть товар за {i} годину: ")))

def main() -> None:
    retrieve()
    print(f"Продано за зміну: {sum(arr)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
