"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item("Наушники", 0, 0)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    assert item3.calculate_total_price() == 0


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item1 = Item("Наушники", 0, 0)

    # Установим новый уровень цен и применим скидку
    Item.pay_rate = 0.8
    item.apply_discount()
    item1.apply_discount()

    assert item.price == 8000.0
    assert item1.price == 0

    # Восстановим исходный уровень цен для других тестов
    Item.pay_rate = 1.0


def test_all_instances():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1 in Item.all
    assert item2 in Item.all

    # Убедимся, что экземпляры были добавлены в список all
    assert all(item in Item.all for item in [item1, item2])
