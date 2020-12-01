# PyFleet Project 

Python/Django based app for transportation company management. 

Features:
- profile creation, authentication and authorisation profiles for employee roles
- creation and maintnance of records for employees, trucks, customers, orders, daily reports
- dashboard view of key metrics (liked with DB models)
- report costumization and generation (for ex as .cvs download)
- company news panel with blog-like articles capabilities
- Google-API based display of truck GPS monitoring
- responsive and flexible fron-end html display

## Installation

open new python project as pull from GitHub : https://github.com/Piter815/PyFleetNew.git

Activate virtual enviroment

Django commands to run before starting server:
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata fixtures.json
$ python manage.py createsuperuser

## Usage

run Django development server:

$ python manage.py runserver

Superuser - admin role, access to all features - login after creation 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate!
