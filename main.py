from random import randint

ne_vajno = int(input(f"Здраствуйте, у нас свободно {randint(1,10)} столиков. За какой столик сядите?: "))

first = {
    "Борщ" : 50,
    "Солянка" : 90,
    "Гороховый суп" : 100,
    "Грибной суп" : 30,
    "Сырный суп" : 200
}
second = {
    "Картофель пюре" : 100,
    "Макароны с сыром" : 200,
    "Рис с овощями" : 180,
    "Котлеты" : 350,
    "Гуляш" : 700
}
sweets = {
    "Торт" : 100,
    "Пироженое" : 150,
    "Конфеты" : 200,
    "Печенье" : 250,
    "Мороженое" : 350,
}
hot_bar = {
    "Чай" : 50,
    "Кофе" : 100,
    "Какао" : 200,
    "Горячий шоколад" : 150,
    "Молоко" : 300
}
bar = {
    "Мартини Фиеро" : 1599,
    "Лонг Айленд Айс Ти" : 999,
    "Пина Колада" : 899,
    "Мохито" : 745,
    "Джин-Тоник" : 699
}
menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
order_name = []
order_price = []
def pages(page):
    while True:
        match page:
            case 1:
                print(first)
                y_n = input("Чтото возьмете?")
                if y_n == "n":
                    menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                    pages(menu)
                elif y_n =="y":
                    dish1 = input("Выберите блюдо из списка: ")
                    for i in first:
                        if dish1 == i:
                            order_price.append(first[dish1])
                            order_name.append(dish1)
                            menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                            pages(menu)
            case 2:
                print(second)
                y_n = input("Чтото возьмете?")
                if y_n == "n":
                    menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                    pages(menu)
                elif y_n =="y":
                    dish2 = input("Выберите блюдо из списка: ")
                    for i in second:
                        if dish2 == i:
                            order_price.append(second[dish2])
                            order_name.append(dish2)
                            menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                            pages(menu)
            case 3:
                print(sweets)
                y_n = input("Чтото возьмете?")
                if y_n == "n":
                    menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                    pages(menu)
                elif y_n =="y":
                    dish3 = input("Выберите блюдо из списка: ")
                    for i in second:
                        if dish3 == i:
                            order_price.append(sweets[dish3])
                            order_name.append(dish3)
                            menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                            pages(menu)
            case 4:
                print(hot_bar)
                y_n = input("Чтото возьмете?")
                if y_n == "n":
                    menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                    pages(menu)
                elif y_n =="y":
                    dish4 = input("Выберите блюдо из списка: ")
                    for i in second:
                        if dish4 == i:
                            order_price.append(hot_bar[dish4])
                            order_name.append(dish4)
                            menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                            pages(menu)
            case 5:
                print(bar)
                y_n = input("Чтото возьмете?")
                if y_n == "n":
                    menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                    pages(menu)
                elif y_n =="y":
                    dish5 = input("Выберите блюдо из списка: ")
                    for i in second:
                        if dish5 == i:
                            order_price.append(bar[dish5])
                            order_name.append(dish5)
                            menu = int(input("Выберите страницу меню: (1-5, 6-показать чек)"))
                            pages(menu)
            case 6:            
                print(f"Ваши блюда: {order_name}")
                print(f"Цены: {order_price}")
                price = sum(order_price)
                total_price = price + (price * 10 / 100)
                print(f"Общий счёт с учетом обслуживания 10%: {total_price} Рублей")
                break
                
            

pages(menu)



