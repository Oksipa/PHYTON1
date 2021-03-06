# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

price_list = [56.34, 48, 43.18, 87, 45.12, 10.86, 100.87, 152, 63.13, 45.7, 98.20, 90]
new_price_list = []
for price in price_list:
    rubles = int(price)
    kop = round((price - rubles) * 100)
    new_price_list.append(f'{rubles} руб {kop:02d} коп')
print(', '.join(new_price_list))
price_list.sort()
print(price_list)
id_1 = id(price_list)
print(id(price_list) == id_1)
rev_prices = sorted(price_list, reverse=True)
print(rev_prices)
print(sorted(rev_prices[:5]))
