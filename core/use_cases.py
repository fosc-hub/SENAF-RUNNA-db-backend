'''
from core.entities import Product

class ProductUseCase:
    def create_product(self, name, description, price):
        """Creates a new product entity."""
        return Product(name, description, price)

    def discount_product(self, product, percentage):
        """Applies discount to the product."""
        product.apply_discount(percentage)
        return product

'''