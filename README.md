# Doggie DayCare

Doggie Daycare is a site created for Code Institute Milestone 3.
The main purpose of the site is to provide daycare, overnight and grooming services to dogs.
A user can book any of the three services using either of the three forms (There is no need to create an account)
A user can also register an account and then they are able to Create a booking, Read their bookings, Update their bookings or Delete their bookings.
A user can also register an account and then they are able to Create a profile, Read their profile, Update their profile or Delete their profile.

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
about.html - This page provides some information about the company.
base.html - This page is the template for all other pages.
confirm.html - This is the page a user sees when they create a booking.
contact.html - This is where a user can use a contact form to email the company.
daycare.html - This page provides a booking form to book a daycare service.
editbooking.html - This is where a user can edit any of their bookings.
editprofile.html - This is where a user can edit their profile.
grooming.html - This page provides a booking form to book a grooming service.
index.html - The main page giving an outline of the purpose of the site.
login.html - This page allows a user to log in. (You don't need to create an account to make a booking)
overnight.html - This page provides a booking form to book a sleepover service.
prices.html - This page shows the prices of all services.
profile.html - This is where a user can view, edit or delete their profile.
register.html - This page provides an option to create a user account.
viewbooking.html - This is where you can view all bookings. (This page would normally not be available to it is an easy way to show CRUD)
viewprofile.html - This is where a user can view their profile after logging in.
viewprofilebooking.html - This is where a user can view/edit/delete all bookings related to their email address.


### User goals

Guest customer:

* As a customer, I want to be able to book a service without having to create an account.
* As a customer, I want to able to register an account.
* As a customer, I want to be able to view, edit or delete a booking.
* As a customer, I want to be able to contact the company.
* As a customer, I want to be able to view, update or delete my profile.
* As a customer, I want to see the service prices.


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
* The side of the form gives the address and phone number of the company.
* Contains a simple form with email address, password, first name, last name and pets name.

#### Profile

* When a user creates a profile on the register page, they are automatically logged in and forwarded to the profile page.
* The user can view, update or delete their profile.
* This page is only available to users who have created a profile and logged in.


#### Login

* Contains a simple form with email address and password inputs
* Also contains an option to register

#### Contact

* The form has the address and phone number on the side.
* The form contains three inputs; name, email and message.
* The form uses email.js.

#### Footer

* The footer contains links to about, contact, bookings, register and login.
* The footer also contains social media icon links for Facebook & Twitter.
* The icons change depening on whether a user is logged in.
* When not logged in, the footer shows the login and register icons. When logged in, the footer shows the profile and logout icons.
* The footer also contains a copyright notice.

### Future features

* I would like to add a feature to send an email to the user when a booking is made. However, this was not requried for this project.


### Tools

* 
* [GIT](https://git-scm.com/) - as a code editer and version control.
* [GitHub](https://github.com/) - to share and store code 
* [Heroku](https://heroku.com/) - for hosting the application and deployment
* [MongoDB](https://www.mongodb.com) - database for development

### Libraries and frameworks


* [Bootsrap4](https://getbootstrap.com/) - for layout and responsive design
* [FontAwesome](https://fontawesome.com/) - icons implementation
* emailJs - emailjs.com - App for the contact form.
* Datepicker - https://forum.webflow.com/t/simple-datepicker-100-working/73398 

### Languages

* HTML
* CSS
* Javascript
* Python 3.8

## Tesing

## Deployment

This application can run on Gitpod or Heroku

### Deploy to Heroku

The deployed site can be found here: <https://doggiedaycare.herokuapp.com/>

1. Login to Heroku and create a new app

1. On the Resources tab, in the Add-ons field look for Heroku Postgres, select the default Hobby Dev - Free
tier, then click the Provision button. This will provision a Postgres Database for you.

1. In Heroku, go on settings tab and click Reveal Config Vars.

1. Add the values from your env.py file to heroku:

```python
DATABASE_URL - your value
SECRET_KEY - your value




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

1. In settings.py add <https://doggiedaycare.herokuapp.com/> to Allowed Hosts

## Credits

### Media

All images are provided by www.unsplash.com and www.pexels.com

### Code

* A big part of the code was developed by following the Code Institute video lessons. Where needed, I provided credits in the comments of the code.
* [StackOverflow](https://stackoverflow.com/) where I found answers for different topics


### Acnowledgements

