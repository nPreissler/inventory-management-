from random import randint 

class Product:
    def __init__ (self, product, quantity, prod_id):
        self._product = product
        self._quantity = quantity
        self._prod_id = str(randint(0,9999))
    def __str__(self) -> str:
        return f'Name : {self._product.ljust(30)} | Qtd : {self._quantity.ljust(30)} | ID : {self._prod_id.ljust(30)}'

tv = Product('TV', '12', '0')