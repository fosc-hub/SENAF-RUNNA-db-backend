from core.entities import Product
from core.use_cases import ProductUseCase

class InMemoryProductRepository:
    """A simple in-memory repository for testing purposes."""
    def __init__(self):
        self.products = []

    def create(self, product):
        self.products.append(product)

def test_create_product():
    """Test the creation of a product using the ProductUseCase."""
    repo = InMemoryProductRepository()
    use_case = ProductUseCase(repo)

    product = use_case.create_product("Test Product", "Test Description", 99.99)
    
    assert len(repo.products) == 1
    assert repo.products[0].name == "Test Product"