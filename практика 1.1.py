def find_product(products: list, target: str):
    for index, product in enumerate(products, start=1):
        if product == target:
            return index
    return "Товар не знайдено"

products_list = ["Ноутбук", "Смартфон", "Навушники", "Монітор"]
print(find_product(products_list, "Навушники"))
print(find_product(products_list, "Мишка"))      