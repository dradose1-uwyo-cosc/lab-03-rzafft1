myArray = []
animals = ["cat", "dog", "bird"]

animals.append("sheep")
animals.insert(1, "someting you want to add here")
print(animals)

animals.remove("dog")
animals.pop()
del animals[0]
print(animals)

number = [4, 7, 1, 2, 9, 3, 8]
print(sorted(number))
number.sort(reverse=False)

number.reverse()
print(number)