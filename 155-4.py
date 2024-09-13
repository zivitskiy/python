from random import uniform

arr: list[float] = []
ctrl: float = 8.0

def retrieve() -> None:
    arr.append(uniform(ctrl-0.7, ctrl))

def main() -> None:
    retrieve()
    for i, res in enumerate(arr):
        if res == ctrl:
            print(f"Номер спроби що повторює контрольний результат: {i+1}")
        else:
            print("Немає спроб які повторюють результат")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
