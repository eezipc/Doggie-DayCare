
## Doggie DayCare
* Doggie Daycare is a site created for Code Institute Milestone 3.
* The main purpose of the site is to provide daycare, overnight and grooming services to dogs.
* A user can book any of the three services using either of the three forms (There is no need to create an account)
* A user can also register an account and then they are able to Create a booking, Read their bookings, Update their bookings or Delete their bookings.
* A user can also register an account and then they are able to Create a profile, Read their profile, Update their profile or Delete their profile.

## Technologies
Python
HTML
CSS
jquery
bootstrap
MongoDB

## Deployment
The deployed link for the site is: <https://doggieheroku.herokuapp.com/>


## User Experience(UX)

The site has multiple pages as outlined below:
* about.html - This page provides some information about the company.
* base.html - This page is the template for all other pages.
* confirm.html - This is the page a user sees when they create a booking.
* contact.html - This is where a user can use a contact form to email the company.
* daycare.html - This page provides a booking form to book a daycare service.
* editbooking.html - This is where a user can edit any of their bookings.
* editprofile.html - This is where a user can edit their profile.
* grooming.html - This page provides a booking form to book a grooming service.
* index.html - The main page giving an outline of the purpose of the site.
* login.html - This page allows a user to log in. (You don't need to create an account to make a booking)
* overnight.html - This page provides a booking form to book a sleepover service.
* prices.html - This page shows the prices of all services.
* profile.html - This is where a user can view, edit or delete their profile.
* register.html - This page provides an option to create a user account.
* viewbooking.html - This is where you can view all bookings. (This page would normally not be available to it is an easy way to show CRUD)
* viewprofile.html - This is where a user can view their profile after logging in.
* viewprofilebooking.html - This is where a user can view/edit/delete all bookings related to their email address.


## User goals

* As a customer, I want to be able to book a service without having to create an account.
* As a customer, I want to able to register an account.
* As a customer, I want to be able to view, edit or delete a booking.
* As a customer, I want to be able to contact the company.
* As a customer, I want to be able to view, update or delete my profile.
* As a customer, I want to see the service prices.


## Design choices

The design is simple with clear layouts providing easy access to book a service, contact the company and view all services and prices.


## Balsamiq

* Balsamiq mockups are in the folder called "Documentation".
* I kept quite close to the original plans. Although the project did grow as I started to build.

## Header and navigation bar

* There is a logo on the top left with link to home page. Visible on all screens.
* Menu resizes for small devices. Menu icon for small devices is a paw.
* Menu buttons are a blue colour to go with the orange background.
* Menu buttons change depending on whether the user is logged in our out.

## Home page (index.html)

* There is a left column the explains the company purpose
* There is a right column that gives an option to book any of the services.
* There are icons on the footer that change depending on whether the user is logged in or out.

## Daycare

* The left column provides the user the option to book a Daycare service.
* There is a right column that gives an option to book any of the services.

## Grooming

* The left column provides the user the option to book a Grooming service.
* There is a right column that gives an option to book any of the services.

## Overnight

* The left column provides the user the option to book a Sleepover service.
* There is a right column that gives an option to book any of the services.

## Prices

* This page has a carousel showing prices on all three products with links to the booking forms.
* On smaller devices, the text on the carousel is hidden and a menu shows underneath the carousel.
* There are links on the carousel to the relevant section of the menu.

## Register

* The register page has a simple form for a user to create a user profile.
* The side of the form gives the address and phone number of the company.
* Contains a simple form with email address, password, first name, last name and pets name.

## Profile

* When a user creates a profile on the register page, they are automatically logged in and forwarded to the profile page.
* The user can view, update or delete their profile.
* This page is only available to users who have created a profile and logged in.


## Login

* Contains a simple form with email address and password inputs
* Also contains an option to register

## Contact

* The form has the address and phone number on the side.
* The form contains three inputs; name, email and message.
* The form uses email.js.

## About

* This page has a carousel on the centre of the page with links to all three services.
* There is also a section underneath with a little text with information on the company.

## Confirm

* This is a simple confirmation page that shows when a user books a service.

## Editbooking

* This page is similar to the booking pages except that the user can edit existing data.
* Usually, this section is only available to registered users but I have allowed it to be accessed from the link at the bottom of the page.

## Editprofile

* This is similar to the editbooking page but in this case the user can edit their profile.

## Viewbooking

* The page shows all bookings made on this site. Usually only registered users can see their own bookings but it is left open so it CRUD funtionality can be seen.

## Viewprofile

* This page allows the user view their profile and if required, the profile can be edited or deleted.

## Viewprofilebooking

* This page allows the user to view the profile associated with their registered account and if required, the profile can be edited or deleted.

## Footer

* The footer contains links to about, contact, bookings, register and login.
* The footer also contains social media icon links for Facebook & Twitter.
* The icons change depening on whether a user is logged in.
* When not logged in, the footer shows the login and register icons. When logged in, the footer shows the profile and logout icons.
* The footer also contains a copyright notice.

## Future features

* I would like to add a feature to send an email to the user when a booking is made. However, this was not requried for this project.
* I would also create a page to show all user profiles and lock both pages to admin access only.

## Tools


* Gitpod - https://gitpod.ie/ - as a code editer and version control.
* Github - https://github.com/ - to share and store code 
* Heroku - https://heroku.com/ - for hosting the application and deployment
* MongoDB https://www.mongodb.com - database for the website

## Libraries and frameworks

* Bootstrap https://getbootstrap.com/ - for layout and responsive design
* Font Awesome - https://fontawesome.com - Icons
* emailJs - emailjs.com - App for the contact form.
* Datepicker - https://forum.webflow.com/t/simple-datepicker-100-working/73398 

## Languages

* HTML
* CSS
* Javascript
* Python 3.8

## Testing

* Site was tested on Windows 10 pc, 2 x android phones, iPhone 8, iPad mini, Android 10" tablet, Dell 13" laptop, Mac 13" laptop. 
* Site was tested on Chrome, Firefox, Edge, Canary, Safari.
* Site was also tested on Browserstack: www.browserstack.com
* Site was tested with https://validator.w3.org
* Site was tested by https://jigsaw.w3.org/css-validator/
* Python code was checked by http://pep8online.com/
* There are a few errors but the code seems fine. (for example one section says it cannot find the bootstrap.min.css file but the link works.)

## Deployment

This application can run on Gitpod or Heroku

## Deploy to Heroku

1:  Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

2:   Create a Procfile with the terminal command echo web: python app.py > Procfile.

3:  Type git add and git commit the new requirements and Procfile .

4:  Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

5:  From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6:  Confirm the linking of the heroku app to the correct GitHub repository.

7:   In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8:  Set the following config vars:

Key 	Value
DEBUG 	FALSE
IP 	0.0.0.0
MONGO_URI 	mongodb+srv://<username>:<password>@doggiecluster.wtitg.mongodb.net/<dbname>?retryWrites=true&w=majority
PORT 	5000
SECRET_KEY 	<your_secret_key>

9:  In the heroku dashboard, click "Deploy".

10: In the "Manual Deployment" section, made sure the master branch is selected and then click "Deploy Branch".

11: The site is now successfully deployed.

## Credits
* Theme was taken from https://startbootstrap.com/themes/stylish-portfolio/
* Got inspiration from this video: https://www.youtube.com/watch?v=vVx1737auSE
* Got inspiration from this video: https://www.youtube.com/watch?v=3DMMPA3uxBo
* Got inspiration from this video: https://www.youtube.com/watch?v=3ZS7LEH_XBg
* I used bits of code from this site and edited it for my site. Mainly on how to register new users and update profiles. All code is on run.py. https://github.com/andreeaiosip/click-a-book
## Media

All images are provided by www.unsplash.com and www.pexels.com

## Code

* Most of the code was learnt from Youtube, Udemy, Le Wagon because the Code Institute videos were full of errors.
* Got alot of help from stackexchange https://stackexchange.com/


