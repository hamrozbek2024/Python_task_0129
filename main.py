class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self):
        self.menu = []
        self.total = 0

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        for i, f in enumerate(self.menu):
            print(i, f.name, f.price)

    def order(self, index, qty):
        food = self.menu[index]
        cost = food.price * qty
        self.total += cost
        print(f"Buyurtma qabul qilindi: {cost}")

    def report(self):
        print("Kassa:", self.total)


res = Restaurant()
res.add_food(Food("Burger", 25000))
res.add_food(Food("Pizza", 60000))

while True:
    print("\n1.Menyu 2.Buyurtma 3.Kassa 0.Exit")
    c = input(">>> ")

    if c == "1":
        res.show_menu()
    elif c == "2":
        res.order(int(input("Index: ")), int(input("Soni: ")))
    elif c == "3":
        res.report()
    elif c == "0":
        break
