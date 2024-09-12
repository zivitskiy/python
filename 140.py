arr: list[int] = []

for i in range(10):
    arr.append(int(input("Введіть елемент списку: ")))
    arr[i] = arr[1]**2

print(arr)
