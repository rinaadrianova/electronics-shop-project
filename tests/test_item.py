"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


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


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("НоутбукIntelCore3000", 20000, 5)

    assert item1.name == 'Смартфон'
    assert item2.name == 'НоутбукInt'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_all():
    Item.instantiate_from_csv()
    item = Item.all[0]
    assert item.name == 'Смартфон'