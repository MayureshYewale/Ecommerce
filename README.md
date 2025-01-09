# E-Commerce API Project

This project is a RESTful API for an e-commerce platform, developed using **Django** and **Django REST Framework** (DRF). It provides endpoints to manage users, products, categories, orders, order items, and payments. The project aims to provide a backend service for managing the core e-commerce features required to run an online store.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Setup and Configuration](#setup-and-configuration)
5. [API Endpoints](#api-endpoints)
6. [Models](#models)
7. [Authentication](#authentication)
8. [Testing the API](#testing-the-api)
9. [Future Enhancements](#future-enhancements)
10. [Contributing](#contributing)
11. [License](#license)

---

## Features

- **User Authentication**: 
  - User registration, login, and profile management.
  - JWT-based authentication for secure API access.
- **Product Management**:
  - List, create, update, and delete products.
  - Categorization of products for easier browsing.
- **Order Management**:
  - Creation and management of customer orders.
  - Add products to orders as order items.
- **Payment Integration**:
  - Handle payment details associated with orders.
  - Store payment status and amount.
- **Category Management**:
  - CRUD operations on product categories.
- **Order Item Management**:
  - Associate products with orders via order items.

---

## Technologies Used

- **Backend**: Django (Python Web Framework)
- **Django REST Framework**: For building APIs in Django.
- **JWT (JSON Web Token)**: Used for securing endpoints and handling authentication.
- **SQLite**: The default database for development (you can configure MySQL or PostgreSQL).
- **Postman**: Used for testing and interacting with the API.
- **Docker (Optional)**: For containerization of the application.
- **GitHub**: For version control and collaboration.

---

## Installation

Follow the steps below to set up the project locally:

### Step 1: Clone the Repository

Clone the project to your local machine using Git:

'''bash'''
git clone https://github.com/YourUsername/EcommerceAPI.git
cd EcommerceAPI

Step 2: Set Up a Virtual Environment
Create a virtual environment to manage project dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Step 3: Install Dependencies
Install the required Python packages from requirements.txt:

bash
Copy code
pip install -r requirements.txt
Step 4: Set Up the Database
Run the migrations to set up the database schema:

bash
Copy code
python manage.py migrate
Step 5: Create a Superuser (Optional)
Create an admin superuser to access the Django admin panel:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the user.

Step 6: Run the Server
Start the Django development server:

bash
Copy code
python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

**Setup and Configuration**

Database Configuration
By default, the project uses SQLite for simplicity. If you want to switch to MySQL or PostgreSQL, follow the steps below:

Update DATABASES in ecommerce/settings.py to configure your preferred database.
Install the corresponding database drivers:
MySQL: pip install mysqlclient
PostgreSQL: pip install psycopg2
JWT Authentication
The project uses JWT for authenticating users. After logging in with your username and password, you will receive a token that should be included in the Authorization header for all protected endpoints:

bash
Copy code
Authorization: Bearer <your-token>
API Endpoints
The following is a list of available API endpoints:

Method	Endpoint	Description

POST	/api/users/register/	Register a new user

POST	/api/users/login/	Login user and get JWT token
GET	/api/products/	List all products
POST	/api/products/	Create a new product
GET	/api/products/<id>/	Retrieve a specific product
PUT	/api/products/<id>/	Update a product
DELETE	/api/products/<id>/	Delete a product
GET	/api/categories/	List all categories
POST	/api/categories/	Create a new category
GET	/api/orders/	List all orders
POST	/api/orders/	Create a new order
GET	/api/orders/<id>/	Retrieve a specific order
POST	/api/order-items/	Add products to an order
GET	/api/order-items/	List order items
POST	/api/payment/	Make a payment for an order
GET	/api/payment/<id>/	Retrieve payment information for an order
Models
**User Model**
Fields: username, email, password, first_name, last_name
Provides user registration, authentication, and profile management.

**Product Model**
Fields: name, description, price, stock, category, created_at
Represents products in the e-commerce store.

**Category Model**
Fields: name, description
Categorizes products for better filtering and navigation.

**Order Model**
Fields: user, status, total_price, created_at, updated_at
Represents a customer's order, including order status and total price.

**OrderItem Model**
Fields: order, product, quantity, price
Links products to orders, tracking the quantity and price of each product.

**Payment Model**
Fields: order, payment_method, amount, payment_status, payment_date
Tracks payment details for each order, including method, amount, and status.

**Authentication**
The API uses JWT (JSON Web Token) for user authentication. After a user successfully logs in, a JWT token is issued. This token must be included in the Authorization header for accessing any protected routes.

**Login Request**
bash
Copy code
POST /api/users/login/
Request Body:

json
Copy code
{
    "username": "user1",
    "password": "password123"
}
Response:

json
Copy code
{
    "token": "your-jwt-token"
}
Include this token in the Authorization header for future requests:

bash
Copy code
Authorization: Bearer <your-token>
Testing the API
You can use Postman to interact with the API endpoints. Below are a few examples of common API calls:

**User Registration**
bash
Copy code
POST /api/users/register/
Request Body:

json
Copy code
{
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123"
}
Create a Product
bash
Copy code
POST /api/products/
Request Body:

json
Copy code
{
    "name": "Product Name",
    "description": "Product Description",
    "price": 99.99,
    "stock": 10,
    "category": 1
}
Create an Order
bash
Copy code
POST /api/orders/
Request Body:

json
Copy code
{
    "user": 1,
    "status": "pending",
    "total_price": 99.99
}
Future Enhancements
Payment Gateway Integration:

Integrate a payment gateway like Stripe or PayPal for real transactions.
Order Tracking:

Add features for order tracking (shipped, delivered, etc.).
User Profile:

Add advanced user profile management (address, phone number).
Search Functionality:

Implement search functionality for products by name or category.