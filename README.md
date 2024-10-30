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



python manage.py loaddata infrastructure/fixtures/persona.json --app runna.persona
python manage.py loaddata infrastructure/fixtures/nnya.json --app runna.nnya
python manage.py loaddata infrastructure/fixtures/institucion_sanitaria.json --app runna.institucion_sanitaria
python manage.py loaddata infrastructure/fixtures/demanda.json --app runna.demanda
python manage.py loaddata infrastructure/fixtures/actividad.json --app runna.actividad
python manage.py loaddata infrastructure/fixtures/acciones_necesarias.json --app runna.acciones_necesarias
