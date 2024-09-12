from random import randint

r: int = int(input("Введіть значення особистого рекорду: "))

arr: list[int] = []

for i in range(10):
    arr.append(randint(r-10, 194))
    if arr[i] < r:
        arr[i] = 0

print(arr)
