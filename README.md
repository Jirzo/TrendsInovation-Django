<h1 align="center">DJANGO</h1>

## 🏁 Getting Started <a name = "getting_started"></a>
Hi! These steps will guide you through setting up your Django environment.
\
First, clone the repository from GitHub and navigate to the newly created directory:

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [VSCODE](https://code.visualstudio.com/download) - ( Only if you want )



## Virtual enviroment


To initialize the virtual environment for your project, first navigate to the project's root directory. Use the command <br> `python -m venv venv` to create a virtual environment. This action will generate a venv folder within the project directory. Afterward, open the command prompt with elevated privileges (as an administrator), move to the project directory, and activate the virtual environment by executing ``.\venv\Scripts\activate.`` Press Enter to confirm the activation.

## Install requirements

After activating the virtual environment, install the project's dependencies by running the command <br> `pip install -r ./requirements/base.txt`. This will automatically install all the required packages specified <br> in the `requirements` file. Wait for the installation process to complete before proceeding.

## Run server

Before starting the server, two commands must be executed:

- First: `python manage.py makemigrations`, which generates migration files based on the changes made to your models.
- Second: `python manage.py migrate`, responsible for applying or rolling back migrations as required.

These steps will create the necessary tables for Django’s internal use, along with the four custom tables required for your project.

These commands will add additional tables to the database, further solidifying the integration between Django and MariaDB.

To start the server, simply run `python manage.py runserver`. After the server is up and running, navigate to `http://127.0.0.1:8000/category/` in your browser. If everything is configured correctly, the expected page will be displayed.

![Django REST framework image](https://imgur.com/1VlORiB.png)

There are two accessible paths:

- `http://127.0.0.1:8000/admin/`: This requires authentication using a username and password. Use the following credentials: `Username: root` and `Password: admin`. If these credentials don't work, you can create a superuser by running the command `python manage.py createsuperuser`.
- `http://127.0.0.1:8000/docs`: This will provide access to documentation outlining the available HTTP request methods.
<hr/>
