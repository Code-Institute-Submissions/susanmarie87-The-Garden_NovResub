# Gabe’s Garden #
Welcome to Gabe's garden. Fed up with America's food choices in the cafeteria's across schools nationwide, 12-year-old Gabe has set out on a mission to change the way kids eat. Gabe's idea is to have a garden that is grown, cultivated, and maintained  by the students. The harvest will then be used for delicious and nutritious recipes in the our school's cafeterias created and hopefully cooked, by the students. The goal is to inspire as many schools as possible to begin their own garden's providing **real** nutrition to our children again and not being served the normalized frankenfood which is surely contributing to the childhood chronic illness epidemic across the United States.
*[](https://.github.io/ /) 

---

## Contents ##

- [UX (User Experience)](#ux-user-experience)
  - [Project Goals](#project-goals)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
  - [Site Owner Goals](#site-owner-goals)
  - [User Requirements and Expectations](#user-requirements-and-expectations)
  - [Design Choices](#design-choices)
    - [Fonts](#fonts)
    - [Colours](#colours)
    - [Wireframes](#wireframes)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Features](#features)
  - [Features Implemented](#features-implemented)
  - [Future Features](#future-features)
  - [Considered Features](#considered-features)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Running Money Pot Locally](#running-money-pot-locally)
- [Credits](#credits)
  - [Audio](#audio)
  - [Images](#images)
  - [Colour](#colour)
  - [Image editing](#image-editing)
  - [Code Ideas](#code-ideas)
- [Acknowledgements](#acknowledgements)

---

## UX (User Experience) ##


### Project Goals ###

The **goal** 

### User Goals ###

- **Learn about the mission of Gabe's Garden** 
- **Signup on the website**
- **See what events are being offered at the garden** 
- **Sign up to volunteer their time at the garden** 
- **Contact** 

### User Stories ###
* As a user, I want to easily understand what the website is about.
* As a user, I want to easily be able to navigate the site.
* As a user, I want to see how the fruits and vegetables are being used in recipes.
* As a user, I want to be able to register as a member.
* As a user, I want a "Forgot Password" option in case I forget my password.
* As a user, I want to be able to subscribe to a newsletter.
* As a user, I want to be able to signup to volunteer.
* As a user, I want to be able to easily access the links to social media.
* As a user, I want to be able to contact the organization with questions or concerns.
* As a user, I want to be able to delete an event that I signed up for if something changes.

### Site Owner Goals ###
* As a site owner, I want to create an interactive environment for all demographics.
* As a site owner, i want to make sure people are inspired to start their own garden.
* As a site owner, I want people to be able to learn easy tips and tricks.
* As a site owner, I would like for the site visitor;s to be able to connect with social media links.
* As a site owner, I would like to inspire more schools to take action and join in on the farm to table lifestyle.

### User Requirements and Expectations ###
* The site must stand out. 
* The mission of the Garden must be easily received.
* The content needs to be relevant to all audiences.
* The visual elements should be visually appealing.
* The signup sheet must work properly
* The contact form should work properly.
* When a vegetable is clicked, it should take you to the kid-friendly recipe in the recipes section.
* The recipes section should provide 
* The event calendar should work with signup events. 

### Design Choices ###


#### Fonts ####
Big Shoulder Stencil display is the font chosen for the Title and headings. This font was chosen because it is bold, stands out, and the title looks amazing. I feel the characteristics of this font will really help bring the website to life. 

Monda was chosen the paragraphs and information throughout the site. This style was chosen as it seems that the two fonts will compliment each other nicely. They wont be too different yet both are bold and stand out. i want the font to grasp the user's attention from the moment they hit the landing page and Monda paired with Big Shoulder Stencil Family is the perfect match.

#### Colours ####

#A1DD70 This bright lime greencolor will be used for the bottom container of the website to make it stand out.
 
#E8ECD6 This will be the filler color throughout the site.  

#FDFFF0 This color will be used as the break point between the red nav and footer and the green containers. 

#A23131 This color will be used for the nav and footer.

![Color Scheme](assets/images/color-scheme.png)

[Back to Top](#table-of-contents)


---
<a></a>


## **Wireframes**

#### Landing Page Wireframes

- For the landing page, I went with a simple hero image with bold writing overlaying the top.


![Landing Page](static/img/landing.png)

---

<a></a>

## Footer and Contact Form

#### The footer is essentially a contact form. The footer also displays links to social media and copyright information.

![Contact Form](static/img/contact.png)

---

<a></a>

## Event Page 

#### The event page will feature an image but the main point of the page will be the cards that display the events seen here.

![Event Page](static/img/event.png)



## Features ##

## Existing Features
- Navbar
    - The navigation bar will display Gabe's Garden logo on the top left corner.
    - The navbar will display page links on the right side.
    - The navbar will break down into a hamburger to become mobile responsive.

    - The navbar will display the links to the pages which are:
        1. Home
        4. Events
        5. LogIn
        6. SignUp
        
- Footer
    - The footer features:
          - Contact Form
          - Social media links
          - Copyright information

### Index Page

**Hero Image**

- Gabe's Garden index page will feature an image of a group of kids excited and happy to be growing their own vegetables.

## Events

Gabe's Garden will look to host events that will inspire guests of all ages. Events will include: classes, parties, festivals, and much more. The events page will look simialr to index page with a different image and cards that will display upcoming events. The cards will display two buttons. An "add" button and a "remove" button. This way users can easily add the event to their profile so they can keep their schedules organized accordingly.

## LogIn
- The login page will be a form with two inputs. One input will be for their email and the second input will be their password. 

## SignUp
- Similar to the login page, the user will be met with a form. This will ask for basic information an email and password. 

## Profile

- Users will have a very simple profile where they can add or delete the events they have signed up for.

## Features Implemented ###

The features to be implemented will be a reminder notification to the user's email to remind them of their upcoming event.

Another feature to be implemented will  be a donation link capable of accepting donations.

- **Responsive design**

(/wireframes/)

- **User-friendly display**



(/wireframes/.jpg)

- **Dashboard for easy navigation**





- **Social media links**

The site has social media links displayed at the footer of the page, as well as a button to take them to the contact/feedback form.


- **Functional contact form**

### Future Features ###


### Considered Features ###

- **Users do not have an option to choose levels or tasks of the game**

### **Database Structure**

MongoDB was used to set the database for this project

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

#### **Events:**

Key              | Value
-----------------|-----------
_id              | ObjectId
catergory_name   | String
event_name       | String
event_description| String
event_date       | String
event_time       | String




## Technologies ##

### Languages ###

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Libraries ###

- [jQuery](https://jquery.com/)
- [Popper](https://popper.js.org/)
- [Popper JS](https://popper.js.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Font-Awesome](https://fontawesome.com/icons?d=gallery)
- [Google fonts](https://fonts.google.com/)
  
### Tools ###

- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

[Back to content](#contents)

---

<a></a>

## **TESTING**

### NAVIGATION BAR

User Story: As a user, I want to easily be able to navigate the site.
* **PLAN**
I plan to have a navbar that sticks out 
* **IMPLEMENTATION**
* **TEST**


### Registration 

User story: As a user I want to be able to register as a member.

* **PLAN**

In order for users to be able to interact with the garden, there should be a feature on the website that allows them to be able to register their account.
This way, they wil be able to add or delete events at the garden. 

* **IMPLEMENTATION**

There has been a registration page created with a form where the user must enter the basic information. Their username and password will be set up with minimum pattern requirements. Error messages will appear when the user has incorrectly entered information that does not match the correct patterns. after a successful login. The user will be greeted with a hello,(username) atop the page. The user will be able to RSVP for garden events

* **TEST**

* **RESULT**

### Sign In

* **PLAN**

The user should be able to fill out a form with their username and password. After signing in, their username will be displayed on the top and they shoud be directed to a page where they can see if they have any upcoming events. 

* **IMPLEMENTATION**

A sign in form has been created where the user fills out their username and password. This information will be verified by the database. If the wrong information is entered, there will be an error flash message sent to the user. 

* **TEST**

* **RESULT**

### Forgot Password 

* **PLAN**

I plan on adding in a "Forgot password" option in the event that a user has forgotten their password

* **IMPLEMENTATION**

* **TEST**

### RSVP for an event

User story: AS a user, I would like the option to RSVP for an event.

* **PLAN**
My plan is to give users the option to RSVP for events at the garden. 

* **IMPLEMENTATION**

To implement this, I will create

* **TEST**

### Delete event

User story: As a user, I would like the option to delete an event.

* **PLAN**
The plan is to setup an option where the usere can delete and event they had orginally signed up for in the case that they are unable to make it.
* **IMPLEMENTATION**
In order to implement this CRUD function.
* **TEST**

[Back to Top](#table-of-contents)

### BUGS

* **Bug**


* **Fix**

* **Verdict**

* **Bug**

Initially after setting up the login page and functionality the page would throw an error when clicked. The error received ws "too many redirects".

* **Fix**

The reason for  the error turned out to be a simple indentation fix. The else statement was too far back causing the the get request to contantly redirect to itself.

* **Verdict**

Indentation in Python is key.

* **Bug**

Initial Heroku deployment was succesful. Shortly after , the app crashed. The error returned was "State changed from starting to crashed" and
"Process exited with status 1."

* **Fix**

This error was caused by improper syntax in my "if os.path.exists("env.py")" statement in my env.py file. This was a minor bug and was easily fixed y adding a colon after the if statement.

* **Verdict**

Proper syntax is imperative in code.

<a></a>

## **Deployment**

### Local Deployment

I have created the Dog Health Tracker project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be ran locally by following the following steps: (
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:
  
    ```
    git clone https://github.com/susanmarie87/The-Garden.git
    ```
1. Access the folder in your terminal window and install the application's [required modules](https://github.com/Susanmarie87/The-Garden/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

    1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    * Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) gs-Garden
    * Set up the following collections: [Click here to see the exact Database Structure](#database-structure)
      

          *** Add in Mongo data structures here ***

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```

    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by MongoDB.
    Tip for your SECRET_KEY, you can use a [Password Generator](https://passwordsgenerator.net/) in order to have a secure secret key. 
    I personlly recommend a length of 24 characters and exclude Symbols.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```
    ### To deploy your project on Heroku, use the following steps: 

1. Login to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 
    

[Back to Top](#table-of-contents)

<a></a>
## Credits ##


### Images ###

Photo by Artem Beliaikin from Pexels (apple trees)

Photo by Kiana Bosman on Unsplash(future leader)

Photo by Karl Fredrickson on Unsplash(cherry trees)

Photo by Jonathan Borba on Unsplash(ambitious girl)

Hero Image- https://phys.org/news/2018-09-kids-food-gardening.html 

paige-cody-z8gKIE4Kz0Y-unsplash (3) (little boy carrying bucket)

samantha-gades-fIHozNWfcvs-unsplash (1) (outdoor party redhat)

ben-white-4K2lIP0zc_k-unsplash (Smiling boy with book)

Photo by Anna Earl on Unsplash(volunteer)

Photo by Dorota Dylka on Unsplash(yoga)

https://codepen.io/RajRajeshDn/pen/qBEGeEp(cards)

https://www.youtube.com/channel/UCbwXnUipZsLfUckBPsC7Jog(website template)


### Colour ###



### Image editing ###


### Code ideas ###

- 

[Back to content](#contents)

---

## Acknowledgements ##

I would like to recognize the people who have helped me through this project:

- My mentor [Simen Daehlin](https://github.com/Eventyret) 

- Code Institute

- The Tutors. John, Michale, Sheryl, Scott, and Alan, have all spent countless hours helping me solve the most trivial of issues. Without their support I could have never made it this far so a major shoutout to them. 


[Back to content](#contents)

---
