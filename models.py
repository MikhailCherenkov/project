from django.db import models


# Модель Цвета
class Color(models.Model):
    """
    Модель для представления цветов.

    Attributes:
    - name (CharField): Наименование цвета (максимальная длина 100 символов).
    - code (CharField): Код цвета (максимальная длина 10 символов).
    - is_reserved (BooleanField): Флаг, указывающий, является ли цвет зарезервированным (по умолчанию False).

    Meta:
    - verbose_name (str): Наименование в единственном числе для отображения в административном интерфейсе Django.
    - verbose_name_plural (str): Наименование во множественном числе для отображения в административном интерфейсе Django.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.CharField(max_length=100, verbose_name="Наименование цвета", null=True)
    code = models.CharField(max_length=10, verbose_name="Код цвета", null=True)
    is_reserved = models.BooleanField(default=False, verbose_name="Зарезервирован")

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return f'{self.name} {self.code}'


# Модель ГОРОДА
class City(models.Model):
    """
    Модель для представления городов.

    Attributes:
    - name (CharField): Наименование города (максимальная длина 20 символов).

    Meta:
    - verbose_name (str): Наименование в единственном числе для отображения в административном интерфейсе Django.
    - verbose_name_plural (str): Наименование во множественном числе для отображения в административном интерфейсе Django.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.CharField(max_length=20, verbose_name="Наименование города")

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'г. {self.name}'


# Модель УЛИЦЫ
class Street(models.Model):
    """
    Модель для представления улиц.

    Attributes:
    - name (CharField): Наименование улицы (максимальная длина 255 символов).

    Meta:
    - verbose_name (str): Наименование в единственном числе для отображения в административном интерфейсе Django.
    - verbose_name_plural (str): Наименование во множественном числе для отображения в административном интерфейсе Django.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.CharField(max_length=255, verbose_name="Наименование улицы")

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    def __str__(self):
        return f'ул. {self.name}'


# Модель АДРЕСА объекта
class Address(models.Model):
    """
    Модель для представления адресов.

    Attributes:
    - city (ForeignKey): Внешний ключ к модели City, представляющий город.
    - street (ForeignKey): Внешний ключ к модели Street, представляющий улицу.
    - number (CharField): Номер дома (максимальная длина 5 символов).
    - building (CharField, optional): Строение (максимальная длина 5 символов, необязательное поле).

    Meta:
    - verbose_name (str): Наименование в единственном числе для отображения в административном интерфейсе Django.
    - verbose_name_plural (str): Наименование во множественном числе для отображения в административном интерфейсе Django.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name="Улица")
    number = models.CharField(max_length=5, verbose_name="Номер")
    building = models.CharField(max_length=5, null=True, blank=True, verbose_name='Строение')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        if self.building:
            return f'{self.city}, {self.street}, {self.number}с{self.building}'
        else:
            return f'{self.city}, {self.street}, {self.number}'


# Модель ОБЪЕКТА
class BuilderObject(models.Model):
    """
    Модель для представления строительных объектов.

    Attributes:
    - name (CharField): Наименование объекта (максимальная длина 50 символов).
    - address (ForeignKey): Внешний ключ к модели Address, представляющий адрес объекта.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.CharField(verbose_name='Наименование объекта', max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name="Адрес объекта")

    def __str__(self):
        return self.name


# Модель ЭТАЖА
class Floor(models.Model):
    """
    Модель для представления этажей.

    Attributes:
    - number (CharField): Номер этажа (максимальная длина 255 символов).

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    number = models.CharField(max_length=255, verbose_name="Номер этажа")

    class Meta:
        verbose_name = 'Этаж'
        verbose_name_plural = 'Этажи'

    def __str__(self):
        return f'Этаж {self.number}'


# Модель КОМПАНИИ
class Company(models.Model):
    """
    Модель для представления компаний.

    Attributes:
    - name (CharField): Наименование компании (максимальная длина 255 символов).
    - color (ForeignKey): Внешний ключ к модели Color, представляющий цвет компании.
    - object (ForeignKey): Внешний ключ к модели BuilderObject, представляющий расположение компании.
    - number_of_employees (CharField): Количество сотрудников компании (максимальная длина 255 символов).

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.CharField(max_length=255)  # наименование компании
    color = models.ForeignKey('Color', on_delete=models.CASCADE, null=True)  # цвет компании
    object = models.ForeignKey('BuilderObject', on_delete=models.CASCADE)  # расположение компании
    number_of_employees = models.CharField(max_length=255)  # количество сотрудников

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


# Модель ПОМЕЩЕНИЯ объекта
class Room(models.Model):
    """
    Модель для представления помещений.

    Attributes:
    - floor (ForeignKey): Внешний ключ к модели Floor, представляющий этаж, на котором находится помещение.
    - number (CharField): Номер помещения, представленный строкой из выбора (максимальная длина 1 символ).
    - company (ForeignKey): Внешний ключ к модели Company, представляющий занимающую компанию (может быть null).

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE, verbose_name='Этаж')
    number = models.CharField(
        max_length=1,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
        ],
        verbose_name='Номер помещения'
    )
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='occupied_rooms', verbose_name='Занимаемая компания')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return f'{self.floor.number}0{self.number}'


# Модель ЭЛЕКТРОЭНЕРГИИ
class Electricity(models.Model):
    """
    Модель для представления электроэнергии.

    Attributes:
    - price (DecimalField): Цена за кВт·ч (максимальное количество цифр: 10, десятичные места: 2).
    - volume (CharField): Объем электроэнергии за цену (максимальная длина 255 символов).

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за кВт·ч")
    volume = models.CharField(max_length=255, verbose_name="Объем за цену")

    class Meta:
        verbose_name = 'Электроэнергия'
        verbose_name_plural = 'Электроэнергия'

    def __str__(self):
        return f'Цена за {self.volume} кВт·ч: {self.price} руб.'


# Модель предметов для помещения
class InventoryItems(models.Model):
    """
    Модель для представления предметов инвентаря.

    Attributes:
    - name (CharField): Наименование предмета (максимальная длина 255 символов).
    - energy_consumption (DecimalField): Потребляемая энергия в кВт·ч (максимальное количество цифр: 10, десятичные места: 5).

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.CharField(max_length=255)
    energy_consumption = models.DecimalField(max_digits=10, decimal_places=5)  # потребляемая энергия в кВт·ч

    class Meta:
        verbose_name = 'Предметы'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name


class InventoryItemsNumber(models.Model):
    """
    Модель для представления предметов в помещении.

    Attributes:
    - name (ForeignKey): Внешний ключ к модели InventoryItems, представляющий предмет.
    - room (ForeignKey): Внешний ключ к модели Room, представляющий помещение, в котором размещается предмет.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    name = models.ForeignKey(InventoryItems, verbose_name="Предмет", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name="Помещение", on_delete=models.CASCADE)

    class Meta:
        verbose_name = '№ Предмета'
        verbose_name_plural = '№ Предметы'

    def __str__(self):
        return f'{self.name}, {self.room}'


class EnergyConsumption(models.Model):
    """
    Модель для учета потребленной энергии.

    Attributes:
    - company (ForeignKey): Внешний ключ к модели Company, представляющий компанию.
    - room (ForeignKey): Внешний ключ к модели Room, представляющий помещение, может быть null и blank.
    - floor (ForeignKey): Внешний ключ к модели Floor, представляющий этаж, может быть null и blank.
    - date (DateField): Дата потребления энергии.
    - consumption_without_an_assistant (JSONField): Потребление электроэнергии без помощника в формате JSON.
    - consumption_with_an_assistant (JSONField): Потребление электроэнергии с помощником в формате JSON.
    - total_amount_of_electricity_consumed_without_an_assistant (FloatField): Общее количество потребляемой электричества без помощника.
    - total_amount_of_electricity_consumed_with_the_assistant (FloatField): Общее количество электричества, потребляемого с помощником.
    - total_cost_without_an_assistant (JSONField): Общая стоимость потребления без помощника в формате JSON.
    - total_cost_with_an_assistant (JSONField): Общая стоимость потребления с помощником в формате JSON.
    - humidity (JSONField): Значение влажности в формате JSON.
    - temperature (JSONField): Значение температуры в формате JSON.
    - illumination (JSONField): Значение освещенности в формате JSON.
    - motion (JSONField): Наличие движения в формате JSON.

    Methods:
    - __str__: Метод для представления объекта в виде строки.

    """
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='energy_consumptions')
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True)
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()  # дата

    consumption_without_an_assistant = models.JSONField()  # Потребление электроэнергии без помощника
    consumption_with_an_assistant = models.JSONField()  # Потребление электроэнергии с помощником
    total_amount_of_electricity_consumed_without_an_assistant = models.FloatField()  # общее количество потребляемой электричества без помощником
    total_amount_of_electricity_consumed_with_the_assistant = models.FloatField()  # общее количество_электричества, потребляемого с помощником
    total_cost_without_an_assistant = models.JSONField()  # общая стоимость без_помощи
    total_cost_with_an_assistant = models.JSONField()  # общая_стоимость с_ан_ассистентом

    humidity = models.JSONField()  # Значение влажности
    temperature = models.JSONField()  # Значение температуры
    illumination = models.JSONField()  # Значение освещенности
    motion = models.JSONField()  # Наличие движения

    def __str__(self):
        return f'Компания: {self.company.name}|{self.room}, Дата: {self.date}'

    class Meta:
        verbose_name = 'Потребление энергии'
        verbose_name_plural = 'Потребление энергии'
