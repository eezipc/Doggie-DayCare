# Doggie DayCare

Doggie Daycare is a site created for Code Institute Milestone 3.
The main purpose of the site is to provide daycare, overnight and grooming services to dogs.
Main technologies used are
python
html
CSS
jquery
bootstrap
MongoDB

The deployed link for the site is: <https://doggieheroku.herokuapp.com/>


## User Experience(UX)

The site has multiple pages as outlined below:
index.html - The main page giving an outline of the purpose of the site.
grooming.html - This page provides a booking form to book a grooming service.
daycare.html - This page provides a booking form to book a daycare service.
overnight.html - This page provides a booking form to book a sleepover service.
prices.html - This page shows the prices of all services.
register.html - This page provides an option to create a user account.
login.html - This page allows a user to log in. (You don't need to create an account to make a booking)
about.html - This page provides some information about the company.
confirm.html - This page provides confirmation when a user submits a booking.
viewbooking.html - This is where you can view all bookings. 
editbooking.html - This is where you can edit any booking.
profile.html - This is where a user can edit or delete their profile.
contact.html - This is where a user can use a contact form to email the company.


### User goals

Guest customer:

* As a customer, I want to be able to book a service.
* As a customer, I want to able to register an account.
* As a customer, I want to be able to edit or delete a booking.
* As a customer, I want to be able to contact the company.
* As a customer, I want to be able to update or delete my profile.
* As a customer, I want to see the service prices


### Design choices

The design is simple with clear layouts providing easy access to book a service, contact the company and view all services and prices.


### Balsamiq

Balsamiq mockups are in the folder called "Documentation".
I kept quite close to the original plans. Although the project did grow as I started to build.


## Features

### Existing features

#### Header and navigation bar

* logo on the top left with link to home page. Visible on all screens.
* Menu resizes for small devices. Menu icon for small devices is a paw.
* Menu buttons are a blue colour to go with the orange background.
* Menu buttons change depending on whether the user is logged in our out.

#### Home page

* There is a left column the explains the company purpose
* There is a right column that gives an option to book any of the services.
* There are icons on the footer that change depending on whether the user is logged in or out.

#### Daycare

* The left column provides the user the option to book a Daycare service.
* There is a right column that gives an option to book any of the services.

#### Grooming

* The left column provides the user the option to book a Grooming service.
* There is a right column that gives an option to book any of the services.

#### Overnight

* The left column provides the user the option to book a Sleepover service.
* There is a right column that gives an option to book any of the services.

##### Prices

* This page has a carousel showing prices on all three products with links to the booking forms.
* On smaller devices, the text on the carousel is hidden and a menu shows underneath the carousel.
* There are links on the carousel to the relevant section of the menu.

#### Register

* The register page has a simple form for a user to create a user profile.
* The left of the form gives the address and phone number of the company.

#### Profile

* When a user creates a profile on the register page, they are automatically logged in and forwarded to the profile page.
* The user can update their profile or delete their profile.

#### Emails

* user receives an email on the email address provided with details of his order

#### Register and login

* form for register with: email address, username, password fields
* form for login with: email address or username, password fields
* confirmation email for registering
* option to change password

#### Profile

* this is available only for registered users. It contains a form with delivery details of the user that can be updated and saved for future use and a table for order history which contains: order number, name of the products and quantity selected, date when the order was registered and total

#### Contact

* contains the contact details of the business: email and phone number
* contains a form for message

#### Footer

* contains links to about me and contact page
* contains social media icon links for Facebook, Instagram and Pinterest
* contains icons for cards accepted and payment security provider
* contains copyright

### Future features

* Product management for business owners.  The ability to add, edit, delete a product from a customized, more friendly interface. This can be done from the admin panel in the meantime.
* Update or remove an own review as a registered user.
* The ability to choose more than one filters at once. The option to disable a filter if user click on it.

## Technologies

### Tools

* [VSCode](https://code.visualstudio.com/) - as code editor
* [GIT](https://git-scm.com/) - to manage version control
* [GitHub](https://github.com/) - to share and store code remotely
* [Heroku](https://heroku.com/) - for hosting the application and deployment
* [AWS S3](https://aws.amazon.com/s3/) - cloud service for media and static files
* [Stripe](https://stripe.com/) - for managing payments
* [Sqlite3](https://www.sqlite.org/index.html) - database for development
* [PostgreSQL](https://www.postgresql.org/) - database provided by Heroku for production
* [AdobeXD](https://www.adobe.com/products/xd.html) - for creating mock-ups

### Libraries and frameworks

* [Django3](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development
* [Bootsrap4](https://getbootstrap.com/) - for layout and responsive design
* [FontAwesome](https://fontawesome.com/) - icons implementation
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - a template language for python used to bring logic into templates
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - a library that enables python code to modify AWS service

### Languages

* HTML
* CSS
* Javascript
* Python 3.8

## Tesing

## Deployment

This application can run locally or deployed to a live environment

### Local

The example provided uses VSCode as a code editor and Windows as an operating system.

1. Save a copy of the github repository located at <https://github.com/vladoprea/dream-woollies> by clicking the 'download.zip' button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command:

```python
git clone <https://github.com/maliahavlicek/ms4_challenger.git>
```

1. Set up a virtual environment via this command in the terminal session:

```python
python -m venv env
```

1. Activate the .venv with the command:

```python
\env\Scripts\activate.bat
```

1. Install all required modules with the command:

```python
pip install -r requirements.txt
```

1. Create a env.py file and add it to your .gitignore

1. Copy the following into the env.py file:

```python
import os

os.environ['SECRET_KEY'] = 'your value'
os.environ['DATABASE_URL'] = 'your value'
os.environ['STRIPE_PUBLIC_KEY'] = 'your value'
os.environ['STRIPE_SECRET_KEY'] = 'your value'
os.environ['STRIPE_WH_SECRET'] = 'your value'
os.environ['AWS_ACCESS_KEY_ID'] = 'your value'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your value'
os.environ['DEVELOPMENT'] = '1'
```

1. Set up the databases by running the following management command in your terminal:

```python
python manage.py migrate
```

1. Create the superuser so you can have access to the django admin:

```python
python manage.py createsuperuser
```

1. Start your server by running the following command in your terminal:

```python
python manage.py runserver
```

### Deploy to Heroku

The deployed site can be found here: <https://dream-woollies-ms4.herokuapp.com/>

1. Login to Heroku and create a new app

1. On the Resources tab, in the Add-ons field look for Heroku Postgres, select the default Hobby Dev - Free
tier, then click the Provision button. This will provision a Postgres Database for you.

1. In Heroku, go on settings tab and click Reveal Config Vars.

1. Add the values from your env.py file to heroku:

```python
AWS_ACCESS_KEY_ID - your value
AWS_SECRET_ACCESS_KEY - your value
DATABASE_URL - your value
EMAIL_HOST_PASS - your value
EMAIL_HOST_USER - your value
SECRET_KEY - your value
STRIPE_PUBLIC_KEY - your value
STRIPE_SECRET_KEY - your value
STRIPE_WH_SECRET - your value
USE_AWS - True
```

1. Set up the databases with the following command:

```python
python manage.py migrate
```

1. Create the superuser for the postgres database so you can have access to the django admin:

```python
python manage.py createsuperuser
```

1. Preload products and collections using following commands(the order is important):

```python
python manage.py loaddata collections.json
python manage.py loaddata products.json
```

1. Save all the requirements:

```python
pip freeze > requirements.txt
```

1. Create Procfile:

```python
echo web: gunicorn dream_woollies.wsgi:application > Procfile
```

1. Add the files and push them to Github:

```python
git add .
git commit
git push
```

1. Deploy branch in Heroku

1. In settings.py add <https://dream-woollies-ms4.herokuapp.com/> to Allowed Hosts

## Credits

### Media

All the images and texts were provided by Ioana Cucoreanu which is the rightful owner of their copyright.

### Code

* A big part of the code was developed by following the Code Institute video lessons. Where needed, I provided credits in the comments of the code.
* [StackOverflow](https://stackoverflow.com/) where I found answers for different topics
* Average rating was inspired following this video: <https://www.youtube.com/watch?v=rca4ZNFnh5M&list=PLIUezwWmVtFXaHcJ63ZM6uOJdhMrnZFFk&index=29>

### Acnowledgements

* Code Institute Slack Community for providing solutions to every question I had.
* Tutoring from Code Institute that was very patient and heplful when I was in need.

Special thanks to Maranatha Ilesanmi, my mentor, who guided me through this project and provided punctual, solid, useful feedback and very helpful input and tips
