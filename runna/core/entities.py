class Product:
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def apply_discount(self, percentage: float):
        """Apply a discount to the product price."""
        self.price -= self.price * (percentage / 100)
