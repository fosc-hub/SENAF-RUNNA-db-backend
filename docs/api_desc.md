### **How Pagination Works**
- By default, the API will return **10 items per page**.
- Clients can pass `?page=2` in the URL to navigate to page 2.
- Clients can override `page_size` using `?page_size=20`, but it will be capped at **max_page_size = 100**.

---
### **How Sorting Works**
- The API will now support sorting using query parameters:
  - `?ordering=fecha_creacion` → Sort by `fecha_creacion` ascending.
  - `?ordering=-fecha_creacion` → Sort by `fecha_creacion` descending.
  - `?ordering=estado` → Sort by `estado`.

---

## **Final API URL Examples**
1. **Paginated Request**
   ```
   GET /mesa-de-entrada/?page=2
   ```

2. **Change Page Size**
   ```
   GET /mesa-de-entrada/?page=1&page_size=20
   ```

3. **Sort by Date (Ascending)**
   ```
   GET /mesa-de-entrada/?ordering=fecha_creacion
   ```

4. **Sort by Date (Descending)**
   ```
   GET /mesa-de-entrada/?ordering=-fecha_creacion
   ```

5. **Sort by State and Paginate**
   ```
   GET /mesa-de-entrada/?ordering=estado&page=1&page_size=15
   ```

---