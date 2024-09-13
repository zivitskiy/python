from random import randint

iter: int = 9
max: int = 99

arr: list[int] = []

def main() -> None:
    s: int = 0
    for _ in range(iter):
        arr.append(randint(1, max))
    print(arr)
    for i in range(iter):
        if arr[i] % 2 == 0:
            s += arr[i]
    print(f"Сума парних чисел з поданих дорівнює: {s}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

