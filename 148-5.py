from random import randint

arr: list = []

def retrieve() -> None:
    for _ in range(10):
        arr.append(randint(5500, 13400))
    print(f"Зарплати: {arr}")

def main() -> None:
    retrieve()
    sal: list = [el * (1 + 0.15) for el in arr]
    print(f"Збільшені зарплати: {sal}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
