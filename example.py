from time import time

_meta = 'Analytics signal'
__meta2 = 'Inner signal'
product = 'Abstract product'


def timelog(func):
    def wrapper (*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Working time is: {round(t2-t1, 10)} sec')
        return result
    return wrapper


class Product:
    _meta = 'Analytics signal'
    __meta2 = 'Inner signal'
    product = 'Abstract product'

    @timelog
    def add_to_cart(self, count):
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')
        print(f'Add {count} products [{self.product}] to cart')

    @timelog
    def edit_description(self):
        print(f'Edit description')

    @timelog
    def add_review(self, text):
        print(f'Add review, text')


class Book(Product):

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __add__(self, other):  # Определяем, как надо складывать объекты класса
        return Book(
            name=f'{self.name}|{other.name}',
            author=f'{self.author}|{other.author}',
            pages=self.pages + other.pages
        )

    def __str__(self):
        return f'BOOK: {self.author}: "{self.name}"'

    def get_pages_count(self):
        print(f'pages count in this biik: {self.pages}')

    def add_to_cart(self, count):
        # super().add_to_cart(self, count)
        print(f'777 {count} 777 [{self.product}] 777')


b1 = Product()
b1.add_to_cart(4)