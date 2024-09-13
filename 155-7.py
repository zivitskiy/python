from random import uniform

arr: list[float] = []

def retrieve() -> None:
    for _ in range(8):
        arr.append(uniform(7.0, 9.5))

def main() -> None:
    retrieve()
    arr.remove(max(arr))
    arr.remove(min(arr))

    avg = sum(arr) / len(arr)
    print(f"Оцінка якості: {avg}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

