from random import choice as randchoice

arr: list[int] = [12 , 23, 34, 45, 56, 67, 78, 89, 90]

def main() -> None:
    chmod: int = randchoice(arr)
    i: int = arr.index(chmod)

    print(f"{chmod}\n{i}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)

