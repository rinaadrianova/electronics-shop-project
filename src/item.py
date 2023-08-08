import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # для хранения уровня цен с учетом скидки
    all = []  # для хранения созданных экземпляров класса

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        '''Класс-метод, инициализирующий
        экземпляры класса Item данными из файла src/items.csv
        '''

        with open("D:\skypro\electronics-shop-project\src\items.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                cls(row["name"], int(row["price"]), int(row["quantity"]))

    @staticmethod
    def string_to_number(string):
        '''
        Статический метод, возвращающий число из числа-строки
        '''
        return int(float(string))


