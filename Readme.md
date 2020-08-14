# Ecommerce

This is an Ecommerce API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

Create a virtual enviroment
```bash
python -m venv env
```

Start the virtual enviroment
```bash
source venv/Scripts/activate
```

Install the requirements
```bash
pip install -r requirements.txt
```

Handle the migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser
```bash
python manage.py createsuperuser
```

Start the aplication
```bash
python manage.py runserver
```

## Usage

The following routes for the api are:

### api/users
This route is for get all the customer registered in the API

### api/users/create
This route is for create a new customer.
You should enter a JSON for in the post, example:

```JSON
{
    "name": "NAME",
    "email": "EMAIL@DOMAIN.COM",
    "phone": "PHONE",
    "password": "PASSWORD"
}
```

### api/products
This route is for get all the products in the API, and you can create new products

### api/orders
This route is for get all the orders made in the API

