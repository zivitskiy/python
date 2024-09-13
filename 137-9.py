from random import uniform

def main():
    const: list = [round(uniform(6.0, 7.0), 2) for _ in range(5)]

    print("Гравітаційні сталі:")
    for _ in range(2):
        print(const)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
