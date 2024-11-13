```bash
python manage.py setup_project
python manage.py populate_database
```

### What This Command Does:
1. **`makemigrations`**: Generates new migrations based on the changes in your models.
2. **`migrate`**: Applies the migrations to the database.
3. **Creates a superuser**:
   - Username: `admin`
   - Email: `admin@gmail.com`
   - Password: `pepe1234`
