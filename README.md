# Django E-commerce Project

This is a Django-based e-commerce application with four main components: home, users, cart, and order. The project includes functionality for user registration and login, product browsing, adding items to a shopping cart, and placing orders.

## Features

### Home App
- **Product Listing**: Displays a list of products with pagination.
- **Product Detail**: Shows detailed information about a specific product.
- **Product Search**: Allows users to search for products by name.
- **Product Category**: Filters products by category.

### Users App
- **User Registration**: Allows new users to register with a profile.
- **User Login/Logout**: Enables users to log in and log out.
- **User Profile**: Displays user profile information.
- **Edit Profile**: Allows users to edit their profile information.

### Cart App
- **Cart Detail**: Displays the current user's cart with all the items and the total price.
- **Add to Cart**: Adds a product to the user's cart.
- **Remove from Cart**: Removes a product from the user's cart.
- **Update Cart Quantity**: Increases or decreases the quantity of a product in the user's cart.

### Order App
- **Checkout**: Allows users to place an order for the items in their cart.
- **Order Detail**: Displays the details of the user's past orders with pagination.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

```plaintext
my_django_project/
├── .gitignore
├── .venv/
├── manage.py
├── home/
│   ├── migrations/
│   ├── templates/
│   │   └── home/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── cart/
│   ├── migrations/
│   ├── templates/
│   │   └── cart/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── order/
│   ├── migrations/
│   ├── templates/
│   │   └── order/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── my_django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── requirements.txt
