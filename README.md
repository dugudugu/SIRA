[![Build Status](https://travis-ci.org/dugudugu/SIRA.svg?branch=master)](https://travis-ci.org/dugudugu/SIRA) 
[![Known Vulnerabilities][(https://snyk.io/test/github/dugudugu/SIRA/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dugudugu/SIRA?targetFile=requirements.txt)
<div align="center">
	<a href="http://stichting-i-respect-animals.herokuapp.com/">
	<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1583088605/Milestone4%20SIRA/hero-image_nkscwz.jpg"/></a>
</div>

<div align="center">
<h1> Stichting I Respect Animals (SIRA)</h1>

SIRA is a non-profit organization that help with the placement of resuce dogs at their forever home or foster home. SIRA works mainly with a rescue center in Spain know as [SPAC](http://spac.cat/), with the occasionally rescues in The Netherlands. With the help of the web application, you are able to *view and read information* reagarding dog adoption. You are also able to make a donation. As an administrator you will have the ability to *ADD, REMOVE and UPDATE dog entries.* 
This application has been created to provide SIRA with working web application. 
</div>

# UX
This is the fourth and last project of my Code Institute Full Stack Software Development course, specifically the Full Stack Frameworks with Django module. The objective for this project is to *"Build a full-stack site based around busniss logic used to control a centrally-owned dataset. Which includes an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service."*

I Have decided to created this web application for Stichting I Respect Animals(SIRA). SIRA is a non-profit organization that helps with fostering and/or provides forever homes for rescue dogs in Spain. When I started with my project SIRA did not have a web application, I figured that this would be a perfect opportunity to help a non-profit organization and also a great topic for my project. At the moment SIRA is starting to build a web application, but they have asked me to take that project over and manage their web application for them. They also want me to incorporate the web application that I have made into the one that they are currently making.


## User Stories
This application must be accesible for all user on a mobile device and/or desktop.
* As a (new)user user is able to do the following:
	- User is ale to go to diffrent pages of the web appliction, by clicking on the Nav-items on the Navbar
	- User is able to do a search, by clicking "Search" on the Navbar
	- User is able to make a donation, by clicking on the "Donate" lable
	- User is able to see a live summary of Facebook Post on the homepage
	- User is able to send a contact for to Stichting I Respect Animals email address

* As an administrator user is able to do the following:
	- User is able to navigate the web application as a non-administrator would
	- User is able to login into the web application
	- User is able to make changes to the "Adoptables" and "Forever Home" application.
		- Create new entrie(s)
		- Removed entrie(s)
		- Update entrie(s)
	- User is able to request a password reset

* As someone that is looking to adopt a dog or become a foster family:
	- The web application should be simple and attracts the eyes as soon as it opens
	- The web application should be easy to navigate
	- Their should be a filter for the dogs that are up for adoption
	- The web application should be able to be used on any mobile device
	- The web application should contain all information reagarding rescue dogs

* As someone that already owns a dog:
	- The web application should be simple and attracts the eyes as soon as it opens
	- The web application should be easy to navigate

	
## Wireframes
The wireframe for both desktop and mobile will have a similar layout. The General layout are displayed in the image below. The initial wireframes were created with [InVission](https://www.invisionapp.com/)
<div align="center">
	<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1583088558/Milestone4%20SIRA/General_layout_k4cbx1.png"/></a>
</div>

### Navbar
The most important part for this web application is that the donation button is always vissible in the Navbar; Users should be able to access the donation button quickly. Here atr the display for the Navbar:
	*Mobile Devices*
	<div align="center">
		<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1583086674/Milestone4%20SIRA/Navbar_Mobile_d8oxwv.png"/></a>
	</div>
	*Desktop*
	<div align="center">
		<img src="https://res.cloudinary.com/dbnahdjbc/image/upload/v1583086660/Milestone4%20SIRA/Navbar_PC_ppwwdk.png"/></a>
	</div>

# Features
## Exiciting Features
1. Navbar - Consists of the a logo which returns the user to the homepage of the app. There are also links to the "Home", "About", "Get Involved", "Adopt", "Forver Home", "Search", "Admin" and "Donate"
2. About - Consists of a dropdown menu where user can go to "Why Spain" and "SIRA team"
	* Why Spain - This page consists of 3 main sections. Fistly, is the hero image. Secondly, the user will have information on why SIRA chooses to rescue dogs that are in Spain. An lastly, the user will have a feature section, that randomly displays 6 dogs that can be adopted. The user as the option to view all the dogs that are up for adoption by clicking the "View All" button
	* SIRA team - This page consists of 3 main sections. The fist section is a hero image. The second section consists of the team members that make up the SIRA team. Lastly, there is a vacancy section, where future vacancies will be shown.
3. Get Involved - Consists of a dropdown menu where user can go to "Adopt", "Volunteer", "Guide" and "FAQs". All of this consits of 2 sections, where the first section is a hero-image
	* Adopt - The user can find the procedure that takes places when he/she wants to adopt a dog
	* Volunteer - The user will find information about how one can help the team or the dogs
	* Guide - The user is able to find information about adopting of fostering a dog; e.g. behavioral issues, background informations about the dogs and how life can be with a rescue dog
	* FAQs - The user will find answer to most frequenty asked questions
4. Adopt - The user will able to see all the dogs that are available for adoption on this page
	* Each dogs will have his/hers own card; that will have a picture, dog name, race, sex, size and a button to redirect user to a more detailed few for each dog 
	* The user is able to filter all dog entries on the page on the following classes: "sex", "size", "situation" and "location"
	* <i>When admin is logged in: he/she will be able to add new dogs to the data-base</i>
	
	** Dog detail view -  The user is able to see a more detailed view of the dog they are interested in. 
		* User will see a shorty story about the background information of the dog, images and other information about the dog e.g. "size", "sex", "age" etc...
		* <i>When admin is logged in: he/she will be able to edit details or remove the dog that the admin is currently viewing</i>
5. Forever Home - The user is able to see all the dogs that have a forever Home. Each dog will have their own card, which includes, a picture, dog name and date of adption
	* <i>When admin is logged in: he/she will be able to add new dogs to the data-base</i>
6. Search - The user will be redirected to a search page, where the user will be able to search for a dog that is either in the "Adopt" or "Forever Home" database
7. Admin - This is the administrator page, where he/she will be able to login to their account.
	* If the administrator has forgotten their password, the admin is able to ask for a password reset link, by clicking "Forgot my password". The admin is directed to a page, where he/she needs to enter email to request password. After entering the correct password the admin is redirected to the home page, and an email will be send to the admin with instructions on how to reset their password
8.Donate - The user is able to make donations on this page. The minimun amount that can be donated is 5 euro's this is to protect user from fraud, it is recommended by Stripe to add a minimun donation of 3 euro's

## Future Features
- Adding a page preloader, so that the user does not see an incompleet/empty page before the page is loaded
- Adding Captcha to login page, for extra seurity measure
- Adding all needed documents for fostering or adoption in pdf 
- Adding digital forms, where the user is able to fill in forms and sign them
- More option of making donations e.g. PayPal and Ideal
- Email subscription


# List of Technologies
## Front-end
- Cloud 9 IDE
- HTML
- CSS
- JavaScript
- jQuery
- Bulma
- Font Awesome
- Flaticon


## Back-end 
- Python
- Django
 

## Others 
- Heroku
- AWS S3 Bucket
- GitHub
- Image Converter
- Code Validators
- SVG Optimiser
- InVission
- Tailor Brands
- Cloudinary


# Testing
## Manual Testing
- This application was tested on desktop and mobile browsers to ensure cross compatibility and functionality.
- The application was tested to be responsive and to ensure it would be correctly displayed across all devices.
- The manual testing of the application covered the following:
	* Checking if all the links an buttons are working properly
	* Login and password reset for administrator are working properly
	* Addition of new dog to database for dogs in "Adopt" and "Forever Home"
	* Editing information of dogs in the detail view
	* Removing of dogs from the database
- Testing of the "Search" functionality

## Validators
- CSS Validator: [CSS Lint](http://csslint.net/#results), [Code Beautify](https://codebeautify.org/) and [Minify Code](http://minifycode.com/css-beautifier/)
- JavaScript Validator: [Validate JavaScript](https://validatejavascript.com/) and [JS Hint](https://jshint.com/)
- Run the web application on [Web Dev](https://web.dev/measure/) and here is the report [Web Dev Report](https://lighthouse-dot-webdotdevsite.appspot.com//lh/html?url=http://stichting-i-respect-animals.herokuapp.com/)

## Known Issues
### Performance
- When loading the web application it takes about 11 seconds to interactive, which means that the user will not see any content at that time

### Best Practices
- Their is 1 warning and 1 error that are begin logged into the browser
	* Warning:
		1. A cookie associated with a cross-site resource at https://stichting-i-respect-animals.herokuapp.com/:1s://walls.io/  was set without the `SameSite` attribute.
			- To fix this issue walls.io needs to fix their cookies
	* Error:
		1. Uncaught TypeError: Cannot read property 'style' of undefined at showSlides (custom.js:64); at custom.js:42
			- This error message mighe be showing because the function cannot find the ID for the function. This function is only needed on the "dog detail" page. A solution might be to load the function on the page that it is needed instead of on the base template

### CSS Code
- CSS Code in base template
	* Error
		1. Value Error: cursor Parse Error -  The using of the static png might be causing an error as it is written in an unexpected way
	* Warnings:
		1. Disallow adjoining classes - Not supported by IE6
		2. Require use of known properties - Expected (flex-start | flex-end | center | space-between | space-around) but found 'start'; .footer .buttons {justify-content: start;}
		3. The use of ID as styling selectors - 
- Custom CSS
	1. The use of box-sizing is not supported by IE6 nad IE7
	2. The use of element name("select") is overqualified

### JS Code
- The used of const for the lazy loading of images

### Django Code
- The correct use of the django built-in views, forms and models - by using more built-in features the functions that written can be shortened and simplified
- Upgrading django version from 1.11 to 3.0
- Correct ordering of django imports


## Automated Testing
- Travis CI - [Travis CI](https://travis-ci.org/) is used to check if the code is being build and deployed correctly
- Snyks - [Snyks][(https://snyk.io/test/github/dugudugu/SIRA/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/dugudugu/SIRA?targetFile=requirements.txt) is used to check if there are any vulnerability in your requirements files

### Known Issues
Altough Travis CI is showing a result of passing, Snyks is picking up a vulnerability in the version of Pillow. To resolve this Pillow needs to be upgraded from version 5.4.1 to 6.2.0; by making this upgrade Travis testing will fail, because it does not recognize version 6.2.0 of Pillow.



# Deployment
This project had been build with [Cloud9 IDE](https://aws.amazon.com/cloud9/), [Django](https://www.djangoproject.com/) and [AWS S3 Bucket](https://aws.amazon.com/s3/). For local deployment the code has been commited to Git and Pushed to [GitHub](https://github.com/). And For remote deployment the code has been commited and pushed to [Heroku](https://www.heroku.com/).

## Local Deployment
Please keep in mind that when running this project locally you have to install the following on your computer:
	* An IDE e.g. Cloud9
	* Pip
	* Python 3
	* Git
	* Django version 1.11.28

You will also need access to the following services:
	* [Stripe](https://stripe.com/en-nl)
	* [AWS](https://aws.amazon.com/) and a setup for [AWS S3 Bucket](https://aws.amazon.com/s3/)
	* [Gmail account](https://gmail.com)
	* [Heroku](https://www.heroku.com/) and [Heroku Postgres](https://www.heroku.com/postgres)

### Instructions for local depoyment:
1. To clone the Github repository please do as following:
    - Under the repository name, click **Clone or Download**
    - In the Clone with HTTPs section, copy the clone URL
    - Open Git Bash
    - Change the working directory to where the cloned directory should be
    - Type **git clone**, and then paste the URL
    - Press **Enter** and the clone will be created
2. Install the requirments from the *requirments.txt* file by:
    - pip3 install -r requirements.txt
3. Create an env.py file in the main directory and add your keys to the file. Ater saving you keys make sure to restart your enviroment to activate enviroment variables. The env.py should look as following:
	```
	import os
	
	os.environ.setdefault("SECRET_KEY", "<Enter your key here>")

	# POSTGRES KEY
	os.environ.setdefault("DATABASE_URL", "<Enter your key here>")
	
	# AWS S3 BUCKET KEYS
	os.environ.setdefault("AWS_SECRET_KEY_ID", "<Enter your key here>")
	os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "<Enter your key here>")
	
	# GMAIL MAIL KEYS (contact form)
	os.environ.setdefault("EMAIL_HOST_USER", "<Enter your key here>")
	os.environ.setdefault("EMAIL_HOST_PASSWORD", "<Enter your key here>")
	
	# STRIPE KEYS
	os.environ.setdefault("STRIPE_PUBLISHABLE", "<Enter your key here>")
	os.environ.setdefault("STRIPE_SECRET", "<Enter your key here>")
	```
* If you are using an IDE that uses bashrc file e.g. Cloud9 you must add the following code to the top of the .bashrc file which is located in the ```*Favorite Hidden Files*```
	```
	export PATH=$PATH:$HOME/.local/bin:$HOME/bin
	export AWSC9_HOST=$C9_PID".vfs.cloud9.eu-central-1.amazonaws.com"
	```
4. After restarting the enviroment, set DEBUG mode to True in ```settings.py file.``` This Should only be done in development. When you ar finished with the development Debug should be set to False
5. A Migration should be perform to create a database template; this can be done by running the following code in the terminal:
	``` ./manage.py migrate ```
6. Create a Django superuser to get access the admin panel and database by:
	```  ./manage.py createsuperuser ```
7. You are now able to run the web application locally by:
	``` ./manage.py runserver $IP:$PORT ```

8. Once the application is running locally, go to local and add ```/admin``` to the back or yhe url. Log in with you superuser account. You are now able to create instances for "Adoptable", "Forever Home" and "User Accounts". After creating these the web application will run normally.

### Remote Deployment with Heroku
This application is currently deployed on [Heroku](http://stichting-i-respect-animals.herokuapp.com/). To deploy this project to Heroku the following steps were taken:
1. Create a *requirements.txt* file so that Heroku can install the needed dependencies
    - pip3 freeze --local > requirement.txt
2. Create a *Procfile* file so tell Heroku which application is being deployed and run
	- web: gunicorn (application name).wsgi:application > Procfile
3. *git add* and *git commit* requirements and Procfile and then *git push* the project to GitHub.
4. Sign up for a free Heroku account and create a new app. By clicking on *New* in the menubar and selecting *Create new app* in the dropdown menu.
5. Set all *Enviroment Keys* in Heroku by doing the following steps:
    - In the *Settings* tab click on *Reveal Config Vars* button
    - Set the *KEY* and *VALUE* as following:
		| Key					| Value 							|
		| --------------------- | --------------------------------- |
		| DISABLE_COLLECTSTATIC | 1									|
		| SECRET_KEY			| ```<your secret key>```			|
		| DATABASE_URL  		| ```<your postgres database url>```|
		| AWS_SECRET_KEY_ID 	| ```<your secret key>``` 			|
		| AWS_SECRET_ACCESS_KEY | ```<your secret key>``` 			|
		| EMAIL_HOST_USER		| ```<your secret key>``` 			|
		| EMAIL_HOST_PASSWORD	| ```<your secret key>``` 			|
		| STRIPE_PUBLISHABLE	| ```<your secret key>``` 			|
		| STRIPE_SECRET 		| ```<your secret key>``` 			|
	- To find the ```Postgres database url``` you must first add ```Postgres``` as an Add-on in the ```Resources``` tab in Heroku. Click on the Heroku Postgres and go to Settings, ere you wil be able to find the url
6. For *Automatic Deployment* from GitHub follow the next steps:
    - In the *Deploy* tab Scroll down to *Apps connected to GitHub*
    - Search for your repository and click on *Connect* (keep in mind that you will need to give Heroku permission yo access your GitHub Repo)
    - After connection is made click on *Enable Automatic Deploys* in the Automatic Deploys section
    - Scroll down to Manual Deploy, choose the branch that you would like to deploy and click on *Deploy Branch*
7. Your application should be successfully deployed on Heroku, click *View App* to run application
8. Once the application is running locally, go to local and add ```/admin``` to the back or yhe url. Log in with you superuser account. You are now able to create instances for "Adoptable", "Forever Home" and "User Accounts". After creating these the web application will run normally.



# Credits
The design idea for this web application came from [The Tanzie Project](https://www.thetanzieproject.org/), [Rescue Paws Curacao](https://rescuepawscuracao.com/) and [Animal Shelter Colorlib Template](https://colorlib.com/preview/#animalshelter)

### Contents
For the content of the webpage the following were used:
- [The Tanzie Project](https://www.thetanzieproject.org/)
- [Rescue Paws Curacao](https://rescuepawscuracao.com/)
- [Dog Rescue Shelter in Spain](http://spac.cat/?fbclid=IwAR3VPOvzAw_6pyjN3Q4j6XjxcF2xYWestNJZDTRN17FliVS_CG1jU1q8bKcv)
- [Stichting I Respect Animals](https://www.facebook.com/Stichting-I-Respect-Animals-801743893284399/)


### Code
I would like to give credits to the following:
- Marcos Oliveira: For the [lightbox](https://codepen.io/marcosdg-com/pen/XPMpxv) functionality when viewing full-screen images
- HTML Online: For [scroll to top arrow](https://html-online.com/articles/dynamic-scroll-back-top-page-button-javascript/)
- Serdar Akarca: For the [jQuery dropdown](https://github.com/jgthms/bulma/issues/1381) function on mobile devices
- Justin Mitchel: For the [django multiple model search](https://www.codingforentrepreneurs.com/blog/a-multiple-model-django-search-engine)
- Jeff Delaney: For the [Lazy loading images](https://fireship.io/snippets/intersection-observer-lazy-load-images/)
- Jeremy Wagner: For [Using webp images](https://css-tricks.com/using-webp-images/)
- Facebook Social Wall: [Walls.io](https://walls.io/)
- Corey Schafer: [Django Tutorials](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- Dennis Ivy: [Filter Form Search](https://www.youtube.com/watch?v=G-Rct7Na0UQ&t=10s)
- Coding Entrepreneurs: [Django Emailing](https://www.youtube.com/watch?v=51mmqf5a0Ss)
- Max Goodridge: [Django Tutorials](https://www.youtube.com/watch?v=Fc2O3_2kax8&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj)



### Images
The following image sources where used on this web application:
- Custom logo creator: [Tailor Brands](https://studio.tailorbrands.com/brands/2453595420)
- For dogs in shelter, and adopted dogs: [Dog Rescue Shelter in Spain](http://spac.cat/?fbclid=IwAR3VPOvzAw_6pyjN3Q4j6XjxcF2xYWestNJZDTRN17FliVS_CG1jU1q8bKcv)
- For dogs in shelter, and adopted dogs:[Stichting I Respect Animals](https://www.facebook.com/Stichting-I-Respect-Animals-801743893284399/)
- For SVGs, user and dog icons: [Flaticon](https://www.flaticon.com/free-icon/animal-paw-print_64431)
- All hero images on this web application were provided by the following:
	- [Cambridge News](https://i2-prod.cambridge-news.co.uk/incoming/article12230696.ece/ALTERNATES/s810/Stray-dog.jpg)
	- [Dogcat](http://dogcat.com.ua/images/slide-2.jpg)
	- [Petplace](https://www.petplace.com/static/27841eff3736e0cbf46cdb7389560f4b/0979f/AdobeStock_126477978.jpg)
	- [Humane Society](https://www.humanesociety.org/sites/default/files/styles/2000x850/public/2018/08/dog-girl-440625.jpg?h=558430af&itok=R-RS3S6N)
	- [Science News](https://www.sciencenews.org/wp-content/uploads/2019/10/110919_review_feat-1028x579.jpg)
	- [Animal Compassion Team](https://www.animalcompassionteam.org/adoption-info)
	- [She Knows](https://www.sheknows.com/wp-content/uploads/2018/12/rgd9is6epctzlefftef8.jpeg?resize=695,391)
	- [Charter College](https://www.chartercollege.edu/sites/default/files/styles/banner_image_-_new/public/Charter-https://www.chartercollege.edu/news-hub/what-you-need-know-about-adopting-pet-shelter)
	- [Doggie Jogs](https://www.doggiejogs.com/about-us)


## Acknowledgements
I would like to express my special thanks of gratitude to my mentor Mr. Rahul Lakhanpal, Tutor team of Code Institute and Slack Community. They helped and provided me with his/her valuable guidance. 

I would also like to thank my partner Chris Harms. For his deep interest and encouragement provided to me during the course of this project.

And lastly, a special thanks to Stichting I Respect Animals(SIRA) and Sandra van Dijk for giving me the opportunity to create this web application.


## Disclaimer
The content of this web page is for educational purposes only. 
Contact request on this page will be send to a test email. 
Donation request are in testing fase, DO NOT use YOUR CREDIT CARD.