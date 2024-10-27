from infrastructure.models import ProductModel
from core.entities import Product

class ProductRepository:
    def create(self, product: Product):
        """Save a product entity to the database."""
        ProductModel.objects.create(
            name=product.name,
            description=product.description,
            price=product.price,
        )

    def get_all(self):
        """Retrieve all products from the database."""
        products = ProductModel.objects.all()
        return [Product(p.name, p.description, p.price) for p in products]