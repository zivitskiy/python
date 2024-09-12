from random import choice as randchoice

arr: list[int] = [12 , 23, 34, 45, 56, 67, 78, 89, 90]

chmod: int = randchoice(arr)

i: int = arr.index(chmod)

print(f"{chmod}\n{i}")

