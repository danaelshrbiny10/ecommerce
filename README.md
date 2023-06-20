# Ecommerce Django Project

[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=yellow&color=darkblue)](https://www.python.org) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)   [![pydocstyle](https://img.shields.io/badge/pydocstyle-enabled-brown)](http://www.pydocstyle.org/en/stable/)

This project is an ecommerce web application built using Django and Django Rest Framework. It provides functionality for user registration, authentication, product listing, cart management, order creation, and order viewing. The project utilizes PostgreSQL as the database backend and JWT authentication for user authentication. API endpoints are documented using Swagger.

## Table of Contents

- [installation](./README.md/#installation)
- [usage](./README.md/#usage)
- [API Documentation](./README.md/#api-documentation)
- [Database Backend](./README.md/#database-backend)
- [Authentication](./README.md/#jwt-authentication)
- [technologies](./README.md/#technologies)
- [License Information](./README.md/#license-information)

## Installation

To get started with the ecommerce project:

1. Clone the repository to your local machine

```bash
git clone https://github.com/danaelshrbiny10/ecommerce.git
```

2. Create a virtual environment and activate it:

```bash
# Create a virtual environment
python3 -m venv ecommerce-venv

# Activate the virtual environment
source ecommerce-venv/bin/activate

```

3. Install the project dependencies:

```bash
pip install -r requirements.txt

```

4. Configure the database backend:
   use PostgreSQL, update the DATABASES settings in `ecommerce/settings.py` with your PostgreSQL database configuration.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("db_name"),
        'USER': os.environ.get("db_user"),
        'PASSWORD': os.environ.get("db_password"),
        'HOST': os.environ.get("db_host"),
        'PORT': os.environ.get("db_port"),
    }
}

```

5. Apply the database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser (admin) account:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

The ecommerce web application should now be running locally at `http://localhost:8000/`.

## Usage
You can use this [postman collection](https://www.postman.com/science-saganist-7786711/workspace/bit68/collection/13841690-17f0b89b-493f-429a-b478-312d42d171f7?action=share&creator=13841690) to learn more about the API usage

1. User Registration:

To register a new user, send a POST request to `/api/register/` with the required user information (`username`, `password`, `email`, `phone_number`, `shipping_address`, `first_name`, and `last_name`.).

2. User Login:

To log in, send a POST request to `/api/login/` with the user credentials (`username` and `password`). This will return a JSON response containing a `JWT token`.

3. Product Listing:

To view a list of all products, send a GET request to `/api/products/`. The products will be displayed in ascending order of price.

4. Searching Products:

To search for products by name, send a GET request to `/api/products/?name=<name-query>`. Replace `<search-query>` with the name of the product you want to search for.

5. Adding Products to Cart:

To add a product to the cart, send a POST request to` /api/cart/` with the `product ID` in the request body.

6. Viewing Cart:

To view the cart, send a GET request to `/api/cart/. This will display the products currently in the cart along with the authanticated user details.

7. Creating an Order:

To create an order with the products in the cart, send a POST request to `/api/orders/`,  This will create a new order using the products in the cart and clear the cart.

8. Viewing Orders:

To view the orders placed by a user, send a GET request to `/api/orders/`.  whose orders you want to view. This will display a list of orders with their details.

## API Documentation

The API endpoints are documented using Swagger. To access the API documentation:

1. Start the development server

```bash
python manage.py runserver
```

2. Open your web browser and navigate to `http://localhost:8000/swagger/` or `http://localhost:8000/redoc/`

## Database Backend

use PostgreSQL and update the DATABASES settings in `ecommerce/settings.py` with your PostgreSQL database configuration.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("db_name"),
        'USER': os.environ.get("db_user"),
        'PASSWORD': os.environ.get("db_password"),
        'HOST': os.environ.get("db_host"),
        'PORT': os.environ.get("db_port"),
    }
}

```

## JWT Authentication

This project uses JWT (JSON Web Token) authentication for user authentication. JWT is a widely adopted standard for securing API endpoints and provides a stateless mechanism for authentication and involves the following components:

1. Token-Based Authentication: Instead of traditional session-based authentication, JWT authentication relies on tokens. When a user logs in or registers, a JWT token is generated and returned to the client.
2. Token Verification: On subsequent requests, the client includes the JWT token in the request headers to authenticate itself. The server verifies the token to authenticate and authorize the user.
3. Token Expiration: JWT tokens have an expiration time, typically set to a short duration for security reasons. Once expired, the token is no longer valid and the client needs to obtain a new token.

To authenticate requests using JWT tokens, include the token in the request headers. The token should be included in the Authorization header using the Bearer scheme

```bash
Bearer <jwt-token>
```

## Technologies

The application is built with the following technologies:

- Django
- Django Rest Framework
- Docker
- Docker Compose
- Nginx

## License Information

This project is licensed under the MIT License. For more details, see the LICENSE file.
