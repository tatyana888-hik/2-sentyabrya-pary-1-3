class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def draw(self):
        print(f"На экране рисуется кот {self.name}, порода {self.breed}.")


cat1 = Cat("Британская", "Мурзик", 3)
cat2 = Cat("Сиамская", "Луна", 2)
cat3 = Cat("Мейн-кун", "Барсик", 5)


print(cat1.breed, cat1.name, cat1.age)
print(cat2.breed, cat2.name, cat2.age)
print(cat3.breed, cat3.name, cat3.age)

cat1.draw()
cat2.draw()
cat3.draw()