def main():
    nazva: list = []
    num: int = int(input("Введіть кількість уроків: "))

    for i in range(num):
        lesson: str = input(f"Введіть назву уроку {i+1}: ")
        nazva.append(lesson)

    print("\nРозклад уроків:")
    for lesson in nazva:
        print(lesson)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
