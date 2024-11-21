# SENAF-RUNNA-db-backend
This is the SENAF-RUNNA-db-backend repository.

To implement **Clean Architecture** in Django, you’ll need to focus on **separating concerns** and **decoupling the framework (Django)** from the **core business logic**. Below is how you can restructure your project following **Clean Architecture principles**.

---

### **1. Overview of Clean Architecture Principles**
1. **Entities**: Core business objects that encapsulate business rules (independent of frameworks).
2. **Use Cases (Interactors)**: Application-specific logic that orchestrates between entities and external systems.
3. **Interface Adapters**: Converts data between external systems (like Django models, HTTP requests) and the application’s core use cases.
4. **Frameworks & Drivers**: Django, databases, REST frameworks, external services are used here but **kept at the boundary**.

The goal is to make your **business logic independent of external frameworks** (like Django or DRF). Django only serves as an interface between the world and your core business rules.

---

### **2. Project Structure for Clean Architecture in Django**
Here’s a proposed structure with clean architecture principles:

```
/my_project/
│
├── manage.py                 # Django CLI utility
├── /my_project/              # Core Django setup
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Framework Configuration (DB, Middleware, etc.)
│   ├── urls.py               # Routes entry point
│   ├── wsgi.py
│
├── /core/                    # Business logic (Entities & Use Cases)
│   ├── __init__.py
│   ├── entities.py           # Domain models (independent of Django ORM)
│   ├── use_cases.py          # Application logic (e.g., product-related operations)
│
├── /infrastructure/          # Django models & adapters for database/ORM
│   ├── __init__.py
│   ├── models.py             # Django ORM models (only data access logic)
│   ├── repositories.py       # Repository pattern to interact with database
│
├── /api/                     # API layer (Django REST Framework)
│   ├── __init__.py
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views and controllers
│   ├── urls.py               # API-specific routes
│
├── /admin_custom/            # Custom Admin Interface (using Unfold)
│   ├── __init__.py
│   ├── admin.py              # Django Unfold customizations
│
└── /static/                  # Static files (CSS, JS, Images)
```

---

### **3. Example Code Implementation**

#### **1. Core Business Logic Layer (`core/entities.py`)**
The **entities** encapsulate business rules without depending on Django models.

```python
# core/entities.py
class Product:
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def apply_discount(self, percentage: float):
        """Apply a discount to the product price."""
        self.price -= self.price * (percentage / 100)
```

#### **2. Use Case Layer (`core/use_cases.py`)**
This layer contains the **application logic**.

```python
# core/use_cases.py
from core.entities import Product

class ProductUseCase:
    def create_product(self, name, description, price):
        """Creates a new product entity."""
        return Product(name, description, price)

    def discount_product(self, product, percentage):
        """Applies discount to the product."""
        product.apply_discount(percentage)
        return product
```

---

#### **3. Infrastructure Layer (Database & ORM)**
Here, we use the **repository pattern** to isolate Django’s ORM from the core logic.

##### **Django Models (`infrastructure/models.py`)**
```python
# infrastructure/models.py
from django.db import models

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

##### **Repository Pattern (`infrastructure/repositories.py`)**
```python
# infrastructure/repositories.py
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
```

---

#### **4. API Layer (`api/views.py` and `api/serializers.py`)**

##### **Serializers (`api/serializers.py`)**
```python
# api/serializers.py
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
```

##### **API Views (`api/views.py`)**
```python
# api/views.py
from rest_framework import status, viewsets
from rest_framework.response import Response

from core.use_cases import ProductUseCase
from api.serializers import ProductSerializer
from infrastructure.repositories import ProductRepository

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_use_case = ProductUseCase()
        self.product_repo = ProductRepository()

    def list(self, request):
        """List all products."""
        products = self.product_repo.get_all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Create a new product."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = self.product_use_case.create_product(**serializer.validated_data)
            self.product_repo.create(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

##### **API URLs (`api/urls.py`)**
```python
# api/urls.py
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = router.urls
```

---

#### **5. Custom Admin Setup (`admin_custom/admin.py`)**
```python
# admin_custom/admin.py
from django.contrib import admin
from infrastructure.models import ProductModel
from unfold.admin import UnfoldAdmin

@admin.register(ProductModel)
class ProductAdmin(UnfoldAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
```

---

### **4. Root URL Configuration (`my_project/urls.py`)**
```python
# my_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

---

### **5. Key Benefits of This Approach**
1. **Separation of Concerns**:
   - Core business logic resides in the `core` package, isolated from Django and frameworks.
   - Django models and views act as adapters, not as the core of the application.

2. **Testability**:
   - Core business logic and use cases can be tested independently without needing Django.

3. **Future Scalability**:
   - If necessary, the API layer or business logic can be moved to microservices with minimal refactoring.

4. **Framework Agnosticism**:
   - The application logic is **decoupled** from Django, making it easier to switch frameworks if needed.

---

### **Conclusion**
This **Clean Architecture** implementation for Django ensures your **business logic is independent** of the framework. Django acts as the delivery mechanism, interacting with the core through use cases and repositories. This approach provides better **testability, maintainability, and scalability** for your project.


The `/infrastructure/` module in **Clean Architecture** plays a crucial role by acting as a **bridge between the framework (Django, DRF, etc.) and your core business logic**. Its main goal is to handle the **low-level technical details**—like database interactions and external service integrations—while keeping the **business logic insulated**.

Let’s break this down further:

---

## **1. Purpose of the Infrastructure Module**
- **Abstraction of Frameworks:** Decouples Django ORM from your core business entities.
- **Data Access Layer:** Provides methods for interacting with databases, ensuring core logic does not directly interact with Django models.
- **Repositories & Adapters:** Implements the **repository pattern** to serve as an intermediary between your **core business logic** and **external data sources**.
- **External Integrations:** Handles third-party services, caching mechanisms, or APIs (if needed) within this module.

Think of it as the **"plumbing" layer** that connects your business logic to the outside world while hiding complexities.

---

## **2. Common Components Inside the Infrastructure Module**

Here is a detailed breakdown of what typically belongs inside `/infrastructure/`.

### **2.1. ORM Models (Django Models)**
This part defines your **Django ORM models** which represent database tables. These models serve as a representation of how your data is stored in the relational database.

```python
# infrastructure/models.py
from django.db import models

class ProductModel(models.Model):
    """Django ORM model for storing product information."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

**Purpose:**
- ORM models **map database tables to Python classes**.
- They handle **CRUD (Create, Read, Update, Delete) operations** via Django’s ORM.
- These models are specific to Django and should not leak into your core business logic.

---

### **2.2. Repository Pattern**

The **Repository Pattern** abstracts the data access logic, ensuring the **core use cases (business logic)** interact only with **abstract repositories** rather than Django models. This helps decouple the core logic from Django.

#### **Repository Example (`infrastructure/repositories.py`):**
```python
# infrastructure/repositories.py
from infrastructure.models import ProductModel
from core.entities import Product

class ProductRepository:
    """Repository to handle product data access."""

    def create(self, product: Product):
        """Save a product entity to the database."""
        ProductModel.objects.create(
            name=product.name,
            description=product.description,
            price=product.price,
        )

    def get_all(self) -> list[Product]:
        """Retrieve all products from the database and return as domain entities."""
        product_models = ProductModel.objects.all()
        return [Product(p.name, p.description, float(p.price)) for p in product_models]

    def get_by_id(self, product_id: int) -> Product:
        """Fetch a single product by ID."""
        product_model = ProductModel.objects.get(id=product_id)
        return Product(product_model.name, product_model.description, float(product_model.price))
```

**Purpose of the Repository:**
- **Abstraction Layer:** The core logic interacts with **ProductRepository**, not directly with Django models.
- **Entity Conversion:** Converts **Django ORM objects into core business entities** (in this case, `Product`).
- **Isolation from Django:** Core business logic never interacts with the ORM directly, which makes it easier to switch the data layer (e.g., to a NoSQL DB or external API).

---

### **2.3. Database Migrations**
Since Django models are used for database interaction, **migrations** are also handled within the infrastructure layer. These ensure your database schema aligns with your models.

#### **Usage:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **2.4. Service Integrations and External Adapters**
If your project involves **external services** like APIs, caching systems, or email services, you can implement **adapters** here to interact with them. This keeps the core logic independent of specific service providers.

#### **Example: Cache Adapter (`infrastructure/cache.py`)**
```python
# infrastructure/cache.py
from django.core.cache import cache

class ProductCache:
    """Adapter for caching product data."""

    def get_product(self, product_id: int):
        """Fetch product from cache."""
        return cache.get(f'product:{product_id}')

    def set_product(self, product_id: int, data):
        """Store product in cache."""
        cache.set(f'product:{product_id}', data, timeout=300)
```

**Purpose:**
- **Encapsulates external dependencies** (like Django’s cache framework) into an adapter.
- Keeps the **core business logic independent** of external caching mechanisms.

---

## **3. Key Benefits of the Infrastructure Layer**

1. **Framework Independence**: 
   - The business logic never directly interacts with Django models or APIs.
   - Makes it easier to **swap frameworks** or **databases** if needed (e.g., from Django ORM to SQLAlchemy).

2. **Testability**:
   - The core logic and use cases are easier to **unit test** without involving the database.
   - You can **mock the repository** in tests rather than setting up a full Django test database.

3. **Separation of Concerns**:
   - Data access logic is isolated within the infrastructure layer, ensuring the **core logic remains pure** and focused on business rules.
   - External systems (caches, APIs) are accessed through **adapters**, avoiding leaks into the core logic.

4. **Future-Proofing**:
   - If you switch to **microservices** or a new ORM (like SQLAlchemy), only the infrastructure layer needs to change, not the business logic.

---

## **4. Example Flow: Creating and Storing a Product**

Here’s how the components from different layers interact to **create and store a product**:

1. **API Layer**: Receives a product creation request.
2. **Use Case Layer**: Calls the `create_product` use case to create a `Product` entity.
3. **Infrastructure Layer (Repository)**: The use case calls the `ProductRepository` to persist the entity using Django’s ORM.

Here’s the flow in code:

#### **API View (`api/views.py`)**
```python
# api/views.py
from rest_framework.response import Response
from rest_framework import status, viewsets

from core.use_cases import ProductUseCase
from infrastructure.repositories import ProductRepository
from api.serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_use_case = ProductUseCase()
        self.product_repo = ProductRepository()

    def create(self, request):
        """API endpoint to create a product."""
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = self.product_use_case.create_product(**serializer.validated_data)
            self.product_repo.create(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

## **5. Summary**

The `/infrastructure/` module in Clean Architecture plays a critical role in isolating the **framework and technical details** from your **core business logic**. Key responsibilities include:

- Defining **Django models** to map database tables.
- Implementing the **repository pattern** to abstract data access.
- Providing **adapters** for external services (e.g., caching, APIs).
- Managing **database migrations** and technical integrations.

This approach ensures your application remains **framework-agnostic, highly testable, and maintainable**, making future changes or migrations easier.



That’s a great choice! Switching to **Clean Architecture** in Django will give your project better **maintainability, scalability, and flexibility**. To help you with the transition, here are some **additional tips and best practices** to ensure a smooth shift to this architecture:

---

## **Key Guidelines for Implementing Clean Architecture in Django**

### **1. Make Core Logic Framework-Agnostic**
- **Avoid Django imports in the core logic** (like `core/use_cases.py` and `core/entities.py`).
- Your **use cases** and **entities** should work without Django; they should just be plain Python code.

### **2. Use Dependency Injection for Repositories**
- **Inject repositories and adapters into the use cases** to keep them decoupled from specific implementations. You can achieve this using **constructor injection** or passing the repository as a parameter.

#### Example:
```python
# core/use_cases.py
class ProductUseCase:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def create_product(self, name, description, price):
        product = Product(name, description, price)
        self.product_repo.create(product)
        return product
```

---

### **3. Testing the Core in Isolation**
Since the core logic is decoupled from Django, you can test it without relying on Django’s test client or database.

#### Example of Unit Test for a Use Case:
```python
# tests/test_use_cases.py
from core.entities import Product
from core.use_cases import ProductUseCase

class InMemoryProductRepository:
    """A simple in-memory repository for testing purposes."""
    def __init__(self):
        self.products = []

    def create(self, product):
        self.products.append(product)

def test_create_product():
    repo = InMemoryProductRepository()
    use_case = ProductUseCase(repo)

    product = use_case.create_product("Test Product", "Test Description", 99.99)
    
    assert len(repo.products) == 1
    assert repo.products[0].name == "Test Product"
```
This approach avoids setting up a Django database for testing, leading to **faster tests**.

---

### **4. Handling Migrations Smoothly**
- Use Django ORM in the `/infrastructure/` layer for database interactions.
- Whenever you change your entities and use cases, **ensure your infrastructure models reflect the changes** and **run migrations**.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **5. Use Django Views as Controllers Only**
Your Django views should act as **controllers**, orchestrating requests and responses, but delegating the **business logic** to the core use cases.

#### Example:
```python
# api/views.py
from rest_framework import viewsets
from infrastructure.repositories import ProductRepository
from core.use_cases import ProductUseCase

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.product_use_case = ProductUseCase(ProductRepository())

    def list(self, request):
        products = self.product_use_case.get_all_products()
        return Response([product.to_dict() for product in products])
```

---

### **6. Manage Dependencies Wisely**
- Use Django’s **`INSTALLED_APPS`** only for infrastructure-level components (like models, admin, or REST framework).
- Your core logic should not be listed as a Django app since it’s **not coupled with Django**.

---

### **7. Optimize API Layer with DRF**
- Use **serializers** to validate incoming data and serialize outgoing responses.
- Keep the API views **lean** by focusing only on request handling and delegating logic to the core.

---

## **Next Steps for Your Transition**

1. **Refactor** your project into the new folder structure with:
   - `/core/` for business logic.
   - `/infrastructure/` for models, repositories, and adapters.
   - `/api/` for REST endpoints.
   - `/admin_custom/` for your Django Unfold admin.

2. **Write unit tests** for your core logic to ensure correctness during the transition.

3. **Gradually refactor** views and models, moving logic from Django views and models into use cases and entities.

4. **Document the new structure** for your team to ensure everyone is aligned with the new architecture.

---

## **Conclusion**

You are now on the path to building a robust, maintainable Django project using **Clean Architecture**! This shift will make your application easier to test, extend, and adapt over time. 

If you encounter any challenges during the transition, feel free to ask for advice. Good luck, and enjoy building a **clean and scalable Django project**! 🚀

In the **Clean Architecture** structure, tests are typically organized in a dedicated **`/tests/`** directory at the root level of the project. This keeps them separate from the application code and ensures a clear distinction between code and tests. You can further divide the tests based on the layer they target, such as core use cases, infrastructure, or API endpoints.

Here’s how the directory structure looks with the `tests` folder:

---

## **Updated Directory Structure**
```
/my_project/
│
├── manage.py                 # Django CLI utility
├── /my_project/              # Core Django setup (ASGI, settings, URLs, etc.)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── /core/                    # Business logic (Entities & Use Cases)
│   ├── __init__.py
│   ├── entities.py           # Domain models (independent of Django ORM)
│   ├── use_cases.py          # Application logic (e.g., product operations)
│
├── /infrastructure/          # Django models & adapters for data access
│   ├── __init__.py
│   ├── models.py             # Django ORM models
│   ├── repositories.py       # Repositories for database interactions
│
├── /api/                     # API layer (Django REST Framework)
│   ├── __init__.py
│   ├── serializers.py        # DRF serializers for data validation
│   ├── views.py              # API views and controllers
│   ├── urls.py               # API-specific routes
│
├── /admin_custom/            # Custom Admin Interface (using Unfold)
│   ├── __init__.py
│   ├── admin.py              # Django Unfold customizations
│
├── /tests/                   # Tests for all project components
│   ├── __init__.py
│   ├── /core/                # Tests for core logic (use cases, entities)
│   │   ├── __init__.py
│   │   └── test_use_cases.py # Unit tests for core use cases
│   ├── /infrastructure/      # Tests for repositories and models
│   │   └── test_repositories.py
│   ├── /api/                 # Tests for API views and endpoints
│       └── test_views.py
│
└── /static/                  # Static files (CSS, JS, Images)
```

---

## **Where to Place the `test_use_cases.py` File**
The `test_use_cases.py` file goes under:

```
/tests/core/test_use_cases.py
```

This structure ensures:
1. **Separation of tests by layer**: Tests for core use cases (`/core/`) are located under `/tests/core/`.
2. **Encapsulation of functionality**: Each module or layer has its own tests, e.g., `/tests/api/` for API-related tests, `/tests/infrastructure/` for data access layer tests.

---

### **Content of `/tests/core/test_use_cases.py`**

Here is the example test content again, placed under `/tests/core/test_use_cases.py`:

```python
# tests/core/test_use_cases.py
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
```

---

### **Running the Tests**

1. Use **`pytest`** (recommended) for running your tests, as it provides a clean syntax for assertions and good integration with Django:

   ```bash
   pip install pytest pytest-django
   pytest
   ```

2. Alternatively, you can use Django's built-in test runner:

   ```bash
   python manage.py test
   ```

Make sure the `pytest` or Django test runner discovers your tests by keeping your **test file names prefixed with `test_`**.

---

## **Summary**
The `test_use_cases.py` file should be placed in `/tests/core/`. This layout:
- Ensures **clear organization** of tests by layer.
- Facilitates **faster test runs** by keeping core logic tests isolated from the infrastructure (like the database).
- Provides **scalable test management** as your project grows.

With this structure, each layer of your project is easily testable and independently verifiable, following **Clean Architecture** principles.

Great! Let’s walk through the steps to **run your Clean Architecture-based Django project** smoothly. Below is a checklist to ensure everything is correctly set up and operational.

---

## **1. Install Dependencies**

First, ensure you have all the necessary dependencies installed. In your project directory, run:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` file, here’s a sample to get started:

```text
Django>=4.2
djangorestframework>=3.14
django-unfold
pytest
pytest-django
psycopg2-binary  # If you're using PostgreSQL
```

---

## **2. Apply Database Migrations**

Ensure your database schema is synchronized with your models by running the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

If everything is set up correctly, you should see messages confirming the creation of the necessary tables.

---

## **3. Create a Superuser**

To access the Django admin interface, you need to create a superuser account:

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

---

## **4. Collect Static Files**

If your project includes static files (CSS, JavaScript, etc.), run:

```bash
python manage.py collectstatic
```

This will gather all static files into a single directory for easier serving.

---

## **5. Start the Development Server**

Run the Django development server:

```bash
python manage.py runserver
```

You should see output similar to:

```
Performing system checks...

System check identified no issues (0 silenced).
October 27, 2024 - 15:34:57
Django version 4.2, using settings 'my_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## **6. Verify the Application**

### **6.1. Access the Admin Panel**
Go to:  
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

- Log in with the **superuser** credentials you created.
- Ensure your **Unfold-admin** customizations are visible.

### **6.2. Test the API**
Go to the API endpoint for your product:

[http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/)

If the API is working correctly, you should see either an empty response or existing products (if added).

---

## **7. Running Tests**

To ensure everything is working, run the tests:

1. **Using pytest**:
   ```bash
   pytest
   ```

2. **Using Django's test runner**:
   ```bash
   python manage.py test
   ```

You should see output indicating that all tests have passed.

---

## **8. Handling Common Issues**

1. **Port Conflict**:  
   If port 8000 is already in use, run:
   ```bash
   python manage.py runserver 8080
   ```

2. **Database Connection Errors**:  
   Ensure your database settings in `settings.py` are correct. If using PostgreSQL:
   - Ensure PostgreSQL is running.
   - Verify credentials, host, and port in `DATABASES`.

3. **Static File Not Found in Development**:  
   If you have trouble accessing static files, add the following to `settings.py`:
   ```python
   STATIC_URL = '/static/'
   ```

---

## **9. Deployment Checklist (Optional)**

If you plan to deploy the project to production, consider the following:
- Use **`gunicorn`** or **`daphne`** as your WSGI or ASGI server.
- Set `DEBUG = False` in `settings.py`.
- Configure **allowed hosts**:
  ```python
  ALLOWED_HOSTS = ['yourdomain.com']
  ```

---

## **Conclusion**

By following these steps, you should now have your Django application up and running using the **Clean Architecture** approach. 🎉

If you encounter any issues or have additional questions, feel free to ask!


If you need to **authenticate users using an external API** while also **adding custom fields**, the best approach is to:

- **Extend the Django `AbstractUser` model** to store additional user-related fields.
- **Leverage Django’s authentication system** for managing sessions and permissions.
- **Implement custom authentication logic** to validate credentials against the external API.

---

## **Recommended Approach: Custom User Model with External API Authentication**

### **1. Extend `AbstractUser` for Custom Fields**

This approach allows you to:
- Add **custom fields** such as `fecha_nacimiento`, `telefono`, etc.
- Use **Django’s session management** and permissions features.
- Implement **custom authentication backend** to validate users via an external API.

---

### **Step-by-Step Implementation**

#### **1. Create the Custom User Model**

```python
# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model with additional fields."""
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.email})"
```

**Explanation:**
- This model extends `AbstractUser` to retain Django’s built-in functionality.
- Custom fields like `fecha_nacimiento` and `telefono` are added.
  
Update your **`settings.py`** to use this new user model:
```python
AUTH_USER_MODEL = 'your_app.CustomUser'
```

---

#### **2. Create a Custom Authentication Backend**

The authentication backend will:
1. **Authenticate the user using an external API.**
2. If valid, **retrieve user details** from the external API or create a local user.

```python
# backends.py
import requests
from django.contrib.auth.backends import BaseBackend
from django.conf import settings
from your_app.models import CustomUser

class ExternalAPIBackend(BaseBackend):
    """
    Custom authentication backend to authenticate users via an external API.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Call the external API with the provided credentials
        response = requests.post(
            'https://external-api.com/auth/login/',
            data={'username': username, 'password': password}
        )

        if response.status_code == 200:
            user_data = response.json()
            # Check if user exists locally; if not, create one
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={
                    'email': user_data.get('email'),
                    'fecha_nacimiento': user_data.get('fecha_nacimiento'),
                    'sexo': user_data.get('sexo'),
                    'telefono': user_data.get('telefono'),
                }
            )
            return user  # Return the authenticated user
        return None  # Authentication failed

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
```

---

#### **3. Configure Django to Use the Custom Authentication Backend**

In **`settings.py`**, update the `AUTHENTICATION_BACKENDS` setting:

```python
AUTHENTICATION_BACKENDS = [
    'your_app.backends.ExternalAPIBackend',
    'django.contrib.auth.backends.ModelBackend',  # Fallback to default backend
]
```

---

#### **4. Create Login View Using Django's `authenticate()` Function**

```python
# views.py
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'username': user.username})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'POST request required'}, status=400)
```

---

#### **5. Update URLs for Login**

In **`urls.py`**, add the route for the login view:

```python
# urls.py
from django.urls import path
from your_app.views import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
]
```

---

#### **6. Handling Sessions and Permissions**

- **Django’s session management** works seamlessly with this setup, as the authenticated user is stored in the session.
- You can still **use Django permissions** and groups on the `CustomUser` model.

---

### **7. Run Migrations and Test**

1. Create the necessary database tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Test the **login endpoint** by sending a POST request:
   ```bash
   curl -X POST -d "username=testuser&password=secret" http://127.0.0.1:8000/login/
   ```

3. You should receive a JSON response confirming the login.

---

## **Advantages of This Approach**

1. **Custom Fields Support**:
   - You can store and manage user-related data specific to your application (like `fecha_nacimiento` and `telefono`).

2. **External API Authentication**:
   - Users are authenticated against an **external API** while still leveraging Django’s built-in session and permission system.

3. **Flexible Authentication**:
   - If the external API fails, you can **fallback** to Django’s internal authentication by keeping the default backend as a fallback.

---

## **Summary**

This approach gives you the **best of both worlds**:
- You get **custom user fields** by extending `AbstractUser`.
- You can **authenticate users via an external API** using a **custom authentication backend**.
- Django’s **session management, permissions, and admin interface** remain intact.

Let me know if you encounter any issues or need further customization! 🚀

You can create a custom Django management command to automate the process of running `makemigrations`, `migrate`, and creating a superuser. Below is a step-by-step guide to implementing this:

### Step 1: Create the Command Structure
In your Django app, create the following folder structure if it doesn't exist:

```
myapp/
    management/
        commands/
            __init__.py
            setup_project.py
```

### Step 2: Implement the Command Logic
In `setup_project.py`, implement the command:

```python
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Sets up the project by making migrations, migrating, and creating a superuser'

    def handle(self, *args, **kwargs):
        try:
            # Step 1: Make migrations
            self.stdout.write('Making migrations...')
            call_command('makemigrations')
            self.stdout.write(self.style.SUCCESS('Migrations created successfully.'))

            # Step 2: Apply migrations
            self.stdout.write('Applying migrations...')
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('Migrations applied successfully.'))

            # Step 3: Create superuser
            if not User.objects.filter(username='admin').exists():
                self.stdout.write('Creating superuser...')
                User.objects.create_superuser(
                    username='admin',
                    email='admin@gmail.com',
                    password='pepe1234'
                )
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
            else:
                self.stdout.write(self.style.WARNING('Superuser already exists.'))

        except CommandError as e:
            raise CommandError(f"Error: {e}")
```

### Step 3: Run the Custom Command
Once the command is implemented, run it like this:

```bash
python manage.py setup_project
```

### What This Command Does:
1. **`makemigrations`**: Generates new migrations based on the changes in your models.
2. **`migrate`**: Applies the migrations to the database.
3. **Creates a superuser**:
   - Username: `admin`
   - Email: `admin@gmail.com`
   - Password: `pepe1234`

### Notes:
- **Idempotence**: The command checks if the superuser already exists before creating it, ensuring it doesn't fail if run multiple times.
- **Customizable**: You can easily modify the username, email, or password directly in the command or via arguments if needed.

This provides an efficient way to set up your project environment quickly.

If you're strictly adhering to the **clean architecture** principles, you generally avoid using `ModelSerializer` because it tightly couples your API layer to the database models, which goes against the idea of keeping the infrastructure (Django models) separate from the core (entities and use cases).

However, if you still want to leverage the convenience of `ModelSerializer` for your infrastructure layer, you can adapt it as follows:

### Why Avoid `ModelSerializer` in Clean Architecture
- **Tight Coupling**: `ModelSerializer` directly maps to Django models, binding your API to the database schema.
- **Core Abstraction Violation**: It bypasses your core entities, making it harder to switch out the database or the ORM in the future.

### If You Choose to Use `ModelSerializer`
Here’s how you can use `ModelSerializer` while still maintaining some separation:

#### Step 1: Create Serializers for Models
Place these serializers in the `infrastructure` layer, specifically in the `api` directory:

```python
from rest_framework import serializers
from infrastructure.models import TLocalizacion, TUsuarioLinea, TDemanda, TPersona, TVulneracion

class LocalizacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacion
        fields = '__all__'


class UsuarioLineaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TUsuarioLinea
        fields = '__all__'


class DemandaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDemanda
        fields = '__all__'


class PersonaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPersona
        fields = '__all__'


class VulneracionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVulneracion
        fields = '__all__'
```

---

#### Step 2: Adapting Core Entities with ModelSerializers
You could then create **adapter serializers** that transform data between the core entities and the `ModelSerializer` layer:

```python
from core.entities import Localizacion
from infrastructure.api.serializers import LocalizacionModelSerializer

class LocalizacionEntityAdapter:
    @staticmethod
    def to_entity(localizacion_model):
        return Localizacion(
            calle=localizacion_model.calle,
            numero=localizacion_model.numero,
            referencia_geo=localizacion_model.referencia_geo,
            barrio=localizacion_model.barrio,
        )

    @staticmethod
    def from_entity(localizacion_entity):
        return {
            'calle': localizacion_entity.calle,
            'numero': localizacion_entity.numero,
            'referencia_geo': localizacion_entity.referencia_geo,
            'barrio': localizacion_entity.barrio,
        }

# Example of usage:
model_serializer = LocalizacionModelSerializer(data=LocalizacionEntityAdapter.from_entity(localizacion_entity))
```

---

### Clean Architecture Best Practices
If you want to stick to clean architecture:
1. **Avoid `ModelSerializer` in your core layer.**
2. Use `ModelSerializer` in the **infrastructure** to minimize boilerplate, but keep the core independent.

### Recommendations
- **Use `ModelSerializer` selectively** in the **infrastructure layer** if necessary for speed.
- Keep **adapter patterns** to ensure your core remains database-agnostic.

Would you like help implementing this hybrid approach or more examples?

To implement **Step 2** (adapting core entities with `ModelSerializer`), you'll use an **Adapter pattern** to bridge your core entities and infrastructure models. This ensures your API can benefit from the convenience of `ModelSerializer` while preserving clean architecture principles.

### Implementation

#### 1. **Create Entity-to-Model Adapters**

These adapters handle the conversion between core entities and Django models.

##### Example: `LocalizacionEntityAdapter`
```python
from core.entities import Localizacion
from infrastructure.models import TLocalizacion

class LocalizacionEntityAdapter:
    @staticmethod
    def to_entity(localizacion_model: TLocalizacion) -> Localizacion:
        """Convert a TLocalizacion model instance to a Localizacion entity."""
        return Localizacion(
            calle=localizacion_model.calle,
            numero=localizacion_model.numero,
            referencia_geo=localizacion_model.referencia_geo,
            barrio=localizacion_model.barrio,
        )

    @staticmethod
    def from_entity(localizacion_entity: Localizacion) -> dict:
        """Convert a Localizacion entity to a TLocalizacion model dictionary."""
        return {
            'calle': localizacion_entity.calle,
            'numero': localizacion_entity.numero,
            'referencia_geo': localizacion_entity.referencia_geo,
            'barrio': localizacion_entity.barrio,
        }
```

#### 2. **Integrate Adapters with `ModelSerializer`**

Use the adapter to work with `ModelSerializer` when serializing or deserializing data.

##### Example: `LocalizacionModelSerializer`
```python
from rest_framework import serializers
from infrastructure.models import TLocalizacion

class LocalizacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLocalizacion
        fields = '__all__'
```

#### 3. **Use Adapter in Use Cases**

Here's how the use case interacts with the adapter and serializer:

##### Use Case Example
```python
from infrastructure.api.serializers import LocalizacionModelSerializer
from infrastructure.adapters import LocalizacionEntityAdapter
from core.entities import Localizacion

class LocalizacionUseCase:
    def create_localizacion(self, localizacion_data):
        """Create Localizacion via adapter and serializer."""
        # Convert raw data to Localizacion entity
        localizacion_entity = Localizacion(**localizacion_data)
        
        # Adapt entity to model data and serialize
        serializer = LocalizacionModelSerializer(data=LocalizacionEntityAdapter.from_entity(localizacion_entity))
        if serializer.is_valid():
            serializer.save()
            return LocalizacionEntityAdapter.to_entity(serializer.instance)
        else:
            raise ValueError(f"Invalid data: {serializer.errors}")
```

---

### Key Concepts

1. **`to_entity`**:
   Converts a model (`TLocalizacion`) to an entity (`Localizacion`).

2. **`from_entity`**:
   Converts an entity to a dictionary suitable for a model or serializer.

3. **Use in Views or Services**:
   The use case interacts with the adapters and serializers, ensuring the core layer remains decoupled from infrastructure.

---

### Full Directory Structure
```
core/
    entities/
        localizacion.py
    usecases/
        localizacion_usecase.py
infrastructure/
    models/
        tlocalizacion.py
    api/
        serializers/
            localizacion_serializer.py
    adapters/
        localizacion_entity_adapter.py
```

---

### Example Workflow

1. **Client** sends JSON to API.
2. **Serializer** validates and converts JSON to model.
3. **Adapter** converts model to entity.
4. **Use case** operates on the entity.
5. **Adapter** converts entity back for persistence via `ModelSerializer`.

---

Would you like to see a more detailed implementation for other entities or a full end-to-end example?
To implement user authentication through the API, the choice between **JWT (JSON Web Tokens)** and **Session-based Authentication** depends on your specific requirements for scalability, security, and use case. Here's a comprehensive guide to help you choose the best method and implement it.

---

### **Comparison of JWT vs Session-Based Authentication**

#### 1. **JWT Authentication**
- **How it works**:
  - The user sends credentials (e.g., username and password) to the API.
  - If valid, the server generates a JWT and returns it to the client.
  - The client includes the JWT in the `Authorization` header for subsequent API requests.
- **Token Format**:
  - Encoded as a Base64 string and contains three parts: Header, Payload, and Signature.

- **Advantages**:
  1. **Stateless**: No need to store user sessions on the server.
  2. **Scalable**: Works well in distributed systems (e.g., microservices or multi-server setups).
  3. **Cross-Origin Compatibility**: JWT can be used across different domains.

- **Disadvantages**:
  1. **No Built-in Revocation**: Tokens cannot be invalidated once issued unless additional infrastructure is implemented (e.g., a blacklist).
  2. **Security**: If the token is compromised, it can be used until it expires.

#### 2. **Session-Based Authentication**
- **How it works**:
  - The user logs in, and the server creates a session.
  - The server stores the session data, typically in a database or in-memory store (e.g., Redis).
  - The client includes the session cookie in subsequent requests.

- **Advantages**:
  1. **Secure**: Easy to revoke sessions and manage user states.
  2. **Built-In Support**: Django natively supports sessions.

- **Disadvantages**:
  1. **Stateful**: Requires server-side storage of sessions, which can become a bottleneck in highly scalable applications.
  2. **Less Suitable for APIs**: APIs are often designed to be stateless.

---

### **Choosing the Best Method**
1. **When to Use JWT**:
   - Stateless systems or microservices architecture.
   - Cross-origin requests (e.g., mobile apps, external clients).
   - High scalability requirements.

2. **When to Use Session-Based Authentication**:
   - Traditional web applications or APIs closely tied to a single frontend.
   - Security is a top priority, and you need to easily revoke sessions.
   - You’re already using Django's session middleware.

---

### **Implementation: API Authentication with Django**

#### 1. **Using JWT Authentication**
You can use the `djangorestframework-simplejwt` library to implement JWT in your Django project.

- **Installation**:
  ```bash
  pip install djangorestframework-simplejwt
  ```

- **Settings**:
  Update your `settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ),
  }
  ```

- **URLs**:
  Add the JWT authentication endpoints:
  ```python
  from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

  urlpatterns = [
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  ]
  ```

- **Usage**:
  - Obtain a token by sending a POST request to `/api/token/` with the username and password.
  - Include the token in the `Authorization` header for subsequent API requests:
    ```
    Authorization: Bearer <your_token>
    ```

---

#### 2. **Using Session-Based Authentication**
Django’s default session-based authentication can also work for APIs.

- **Settings**:
  Ensure the following in `settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework.authentication.SessionAuthentication',
      ),
  }
  ```

- **CSRF**:
  Since APIs are stateless, you may need to exempt CSRF for API endpoints:
  ```python
  from django.views.decorators.csrf import csrf_exempt

  @csrf_exempt
  def my_view(request):
      pass
  ```

- **Usage**:
  - The user logs in via `/api/login/`.
  - The client sends the session cookie with subsequent requests.

---

### **Recommendation**

- **For APIs that need to be stateless and consumed by third-party clients or mobile apps**: Use **JWT**.
- **For APIs tightly coupled with a web application or requiring strong session management**: Use **Session-Based Authentication**.

---

### **Hybrid Approach**
In some cases, you may want to combine the two:
- Use **Session Authentication** for your internal web app.
- Use **JWT Authentication** for external or third-party clients.

This approach ensures flexibility and balances security and scalability.

---

Let me know if you need further clarification or a step-by-step implementation for a specific use case!

### **Step 1: Implementing Permissions in DRF API Views**

Django REST Framework (DRF) provides robust support for permission classes to control access to views. The most common permissions include:

- **`IsAuthenticated`**: Only authenticated users can access the endpoint.
- **`IsAdminUser`**: Only admin users (staff users) can access the endpoint.
- **`AllowAny`**: The endpoint is open to all users.
- **Custom Permissions**: Define granular rules as needed.

---

#### **1.1 Applying Built-In Permissions**
Update the `permission_classes` in your views or globally in `settings.py`.

- **Globally (All Views)**:
  Update your `settings.py`:
  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.IsAuthenticated',
      ],
  }
  ```

- **Locally (Specific Views)**:
  Apply permissions directly to individual views:
  ```python
  from rest_framework.permissions import IsAuthenticated
  from rest_framework.views import APIView

  class ExampleView(APIView):
      permission_classes = [IsAuthenticated]

      def get(self, request):
          return Response({"message": "Hello, authenticated user!"})
  ```

---

#### **1.2 Custom Permissions**
You can define custom permissions for more complex rules.

Example: Allow access only if the user is in the "Editors" group.

```python
from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Editors').exists()
```

Apply the custom permission to a view:

```python
class EditorOnlyView(APIView):
    permission_classes = [IsEditor]

    def get(self, request):
        return Response({"message": "Hello, Editor!"})
```

---

### **Step 2: Testing Authentication in Postman**

To test session-based authentication in Postman:

#### **2.1 Log In and Get Session Cookie**
1. Create a `POST` request to your login endpoint (e.g., `/api/login/`).
2. Provide credentials in the body (form-data or JSON):
   ```json
   {
       "username": "user",
       "password": "password"
   }
   ```

3. On successful login, the server returns a session cookie. The response includes `Set-Cookie` headers like:
   ```
   Set-Cookie: sessionid=<your-session-id>; Path=/; HttpOnly
   ```

#### **2.2 Use the Session Cookie**
1. In subsequent requests, include the session cookie in the `Cookie` header:
   ```
   Cookie: sessionid=<your-session-id>
   ```

2. Test authenticated endpoints by adding the session cookie to the headers.

---

### **Step 3: Implementing User Management in a Next.js Web App**

Here’s how to integrate session-based authentication and user management in a Next.js app.

---

#### **3.1 Login and Manage Sessions**

**API Route for Login**:
Create a custom Next.js API route for login to handle requests from the frontend.

```javascript
// /pages/api/login.js
import axios from 'axios';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const { username, password } = req.body;

      // Send login request to Django backend
      const response = await axios.post('http://your-django-backend.com/api/login/', {
        username,
        password,
      });

      // Set the session cookie
      res.setHeader('Set-Cookie', response.headers['set-cookie']);
      res.status(200).json({ success: true });
    } catch (error) {
      res.status(error.response?.status || 500).json({ error: error.response?.data || 'Login failed' });
    }
  } else {
    res.status(405).json({ error: 'Method not allowed' });
  }
}
```

---

#### **3.2 Fetch User Information (Permissions and Groups)**

Create a helper function to fetch the user's details after login.

```javascript
// utils/fetchUser.js
import axios from 'axios';

export async function fetchUser(req) {
  try {
    const response = await axios.get('http://your-django-backend.com/api/users/me/', {
      headers: {
        Cookie: req.headers.cookie, // Pass the session cookie
      },
    });

    return response.data; // User details, groups, permissions
  } catch (error) {
    console.error('Error fetching user:', error);
    return null;
  }
}
```

---

#### **3.3 Use `fetchUser` in Next.js**

Fetch user information on the client or server side.

- **Server-Side Rendering (SSR)**:
  Use `getServerSideProps` to fetch user info and pass it to your React component.

```javascript
import { fetchUser } from '../utils/fetchUser';

export async function getServerSideProps({ req }) {
  const user = await fetchUser(req);

  if (!user) {
    return {
      redirect: {
        destination: '/login',
        permanent: false,
      },
    };
  }

  return {
    props: { user },
  };
}

export default function Dashboard({ user }) {
  return <div>Welcome, {user.username}!</div>;
}
```

- **Client-Side**:
  Use `fetch` or `axios` to retrieve user data after login and update the state.

---

#### **3.4 Send Authenticated Requests**
Include the session cookie when making authenticated requests.

```javascript
import axios from 'axios';

export async function getProtectedData(req) {
  const response = await axios.get('http://your-django-backend.com/api/protected/', {
    headers: {
      Cookie: req.headers.cookie, // Pass the session cookie
    },
  });

  return response.data;
}
```

---

### **Step 4: Add Permissions and Groups Endpoint**

If you want to fetch the user's groups and permissions, create a dedicated endpoint in Django.

Example:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "groups": [{"id": g.id, "name": g.name} for g in user.groups.all()],
            "permissions": [p.codename for p in user.user_permissions.all()],
        })
```

Add this endpoint to your URLs and fetch the data from your Next.js app.

---

### Summary

1. **Permissions in DRF**:
   - Use built-in permissions (`IsAuthenticated`, `IsAdminUser`).
   - Add custom permissions for granular control.

2. **Testing with Postman**:
   - Log in via `/api/login/` to get a session cookie.
   - Include the cookie in subsequent requests to authenticated endpoints.

3. **Next.js Integration**:
   - Login via an API route that forwards credentials to the Django backend.
   - Fetch user data and permissions via `getServerSideProps` or client-side calls.
   - Use the session cookie for authenticated requests.

Let me know if you need further details on any of these steps!

If someone steals your cookies from your browser, they could potentially impersonate you by using the stolen cookie in a session hijacking attack. Here's what could happen and how you can protect yourself:

---

### **1. Risks of Stolen Cookies**

#### **1.1 Session Hijacking**
- **Impact**: If the cookie contains a session ID or authentication token, an attacker can use it to impersonate you on a website or API until the session expires or the cookie is invalidated.
- **Example**: An attacker sends the stolen cookie in the `Cookie` or `Authorization` header of a request to gain unauthorized access to your account.

#### **1.2 Sensitive Data Exposure**
- **Impact**: If the cookie stores sensitive information (like personal data or credit card details, though this is not recommended), the attacker could extract this data.

#### **1.3 Persistent Authentication**
- **Impact**: For cookies with long lifetimes or `remember me` functionality, the attacker might retain access for a long period.

---

### **2. How Cookies Can Be Stolen**

#### **2.1 XSS (Cross-Site Scripting)**
- **Cause**: A malicious script runs in your browser and reads the cookie via `document.cookie`.
- **Example**: Visiting an attacker-controlled website that exploits a vulnerability in another site you’re logged into.

#### **2.2 Man-in-the-Middle (MitM) Attack**
- **Cause**: An attacker intercepts network traffic over an unsecured connection (e.g., HTTP) and extracts the cookie.
- **Example**: Using public Wi-Fi without HTTPS.

#### **2.3 Social Engineering or Malware**
- **Cause**: An attacker tricks you into revealing your cookies or infects your device with malware that extracts them.

---

### **3. How to Mitigate Cookie Theft**

#### **3.1 Use Secure Cookies**
Set the `Secure` flag on cookies to ensure they are only transmitted over HTTPS connections:
```python
response.set_cookie(
    'sessionid',
    value='your_value',
    httponly=True,
    secure=True,
    samesite='Lax'
)
```

#### **3.2 Use HTTPOnly Cookies**
Set the `HttpOnly` flag to prevent JavaScript from accessing cookies:
- This mitigates XSS attacks by ensuring `document.cookie` cannot expose sensitive cookies.

#### **3.3 Set SameSite Policy**
- Prevent cookies from being sent with cross-site requests by using the `SameSite` attribute:
  - **`Strict`**: Cookies are sent only with requests originating from the same site.
  - **`Lax`**: Cookies are sent with top-level navigations (e.g., clicking a link).
  - **`None`**: Allows cross-origin requests (but requires `Secure` to be set).

#### **3.4 Use Short Expiry Times**
- Limit the lifetime of cookies using `Max-Age` or `Expires`. This reduces the window of opportunity for an attacker.

#### **3.5 Regenerate Session IDs**
- Regenerate the session ID on critical actions (e.g., login, role change) to limit exposure if a cookie is stolen.

#### **3.6 Implement HTTPS Everywhere**
- Always use HTTPS to encrypt traffic and prevent MitM attacks.
- Redirect HTTP to HTTPS:
  ```python
  SECURE_SSL_REDIRECT = True
  ```
  Enable HSTS (HTTP Strict Transport Security):
  ```python
  SECURE_HSTS_SECONDS = 31536000
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_HSTS_PRELOAD = True
  ```

#### **3.7 Monitor and Revoke Sessions**
- Implement a server-side session store (if not using JWTs) to manage active sessions and allow users to revoke them.

#### **3.8 Enable CSRF Protection**
- Protect against cross-site request forgery (CSRF) attacks by validating requests with a CSRF token.

#### **3.9 User Awareness**
- Educate users about safe practices:
  - Avoid entering sensitive data on non-HTTPS sites.
  - Don’t click on suspicious links.
  - Use up-to-date antivirus software.

---

### **4. What to Do If Your Cookie is Stolen**

#### **4.1 Invalidate Sessions**
- If you suspect cookie theft, log out all active sessions for your account. In Django:
  ```python
  from django.contrib.sessions.models import Session

  Session.objects.all().delete()
  ```

#### **4.2 Rotate Keys**
- If you're using JWT tokens, rotate the secret key to invalidate all tokens.

#### **4.3 Monitor for Unauthorized Access**
- Check account activity for suspicious logins and take action (e.g., password change, multi-factor authentication).

---

### **5. Proactive Security Measures**

- **Multi-Factor Authentication (MFA)**:
  - Add an extra layer of security by requiring a one-time code or app-based authentication.

- **Regular Cookie Validation**:
  - Validate cookie contents server-side, including IP address and user agent.

- **Content Security Policy (CSP)**:
  - Mitigate XSS attacks by restricting allowed scripts on your website.

---

### Summary

If someone steals your cookies:
1. They can impersonate your session or gain unauthorized access.
2. To prevent cookie theft:
   - Use `Secure`, `HttpOnly`, and `SameSite` attributes.
   - Enable HTTPS and short cookie lifetimes.
   - Protect against XSS and CSRF attacks.
3. Invalidate stolen cookies immediately by ending the session or revoking tokens.

Let me know if you'd like guidance on implementing any of these security measures!
