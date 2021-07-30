<img src="https://ckranz-aishling-dreamshop.s3.amazonaws.com/media/wireframes/Screen-Shot-2021-07-30-at-17.56.57.jpg">

# Aisling Dreamshop

Aisling Dreamshop is an ecommerce website for the imagination. We can't buy, sell or create customised dreams but what if we could? If we could, you might buy your Dreams from Aisling Dreamshop!

In learning how to create a ecommerce website using Python and Django I wanted to play with the idea of this technology. I felt the ethereal concepts of dreams and ingredients would be fun to develop and manage.

One thing I've learned in working on this project is just how much more can be done and learned within these building blocks.

***

## UX (User Experience)

### User Stories
- #### First Time Visitor Goals
    1. As a First Time Visitor, I want to clearly understand the features and functionality of the website.
    2. As a First Time Visitor, I want to be able to quickly view Products and Categories.
    3. As a First Time Visitor, I want to be able to easily register, login and logout.
    5. As a First Time Visitor, I want to be able to search and sort Products and Categories.
    6. As a First Time Visitor, I want to be able to make secure transactions.

 - #### Returning Visitor Goals
    1. As a Returning Visitor, I want to be able to edit or update my profile.
    2. As a returning Visitor I want to check updates and news regarding products and offerings.

- #### Frequent User Goals
    1. As a Frequent User, I want to be able to return to Aisling Dreamshop and search/purchase products.

- #### Superuser Goals
    1. As a Superuser, I want to be able to easily add or edit Products and Categories.
    2. As a Superuser, I want to be able to easily add and edit Posts.

- #### Wireframes
    - Wireframes: [View](https://ckranz-aishling-dreamshop.s3.amazonaws.com/media/wireframes/Ms4-AD-wireframe-charlieKranz.pdf)

## Design

- ### Branding 
    - The Aisling name derived from the Irish word for dream - "Aisling"
    - The tagline helps reinforce the premise, that we live in a world where dreams can be manufactured, sold and shared
    - Clear iconography used for key features and functions, to reinforce utility

- ### Colours
    - Using midnight blue and gold schematic to confer ideas of "night time" and "prestige"
    - Additional colour variations to highlight functions based on Bootstrap model

- ### UI
    - Clean, simple UI
    - Larger screens allow for some 3-4 column layouts
    - Smaller screens use 1-2 column layout and some font-size reduction

- #### Typography
    - Nunito font for headlines, body and smaller text
    - Work Sans font for thicker headlines
    - Kaushan Script font for some featured headlines

## Features

### Existing Features

- __Brand and Navigation Bar__

  - The brand and navigation bar displays the site name and gives users the ability to search, sort and navigate throughout the site
  - The navigation bar displays navigation options based on the users's current state 
  - Logged-in Users will see the My Profile, Product Management and Logout Options under My Account tab (Login and Register options will be hidden)
  - Logged-out Users will see the Signup and Login options under Account tab (Logout, My Profile and Product Management will be hidden)
  - The Shop Basket will show any items added and Current Total Cost of those items
  - The Toats Messages (Alerts) Appear in the Upper right hand section of screen

- __Home Page__

  - The Homepage welcomes the user and highlights some Dream Products via the carousel
  - It allows users to immediately engage with Shop via Shop Now button

- __Dreams Page__

  - Lists all Dream Products and allows for sub-category sorting
  - Category and Rating information is presented
  - Each Product has a Product Detail View allowing user to add a specific quantity to Basket
  - Superusers can Edit or Delete Products

- __Ingredients Page__

  - Lists all Ingredient Products and allows for sub-category sorting
  - Category and Rating information is presented
  - Each Product has a Product Detail View allowing user to add a specific quantity to Basket
  - Superusers can Edit or Delete Products

- __Equipment Page__

  - Lists all Equipment Products and allows for sub-category sorting
  - Category and Rating information is presented
  - Each Product has a Product Detail View allowing user to add a specific quantity to Basket
  - Superusers can Edit or Delete Products

- __Everything Page__

  - Lists all Products and allows for sub-category sorting (Price, Rating and Category)
  - Category and Rating information is presented
  - Each Product has a Product Detail View allowing user to add a specific quantity to Basket
  - Superusers can Edit or Delete Products

- __Updates Page__

  - Includes About information
  - Includes Updates / Posts section

- __Admin Page__

  - Allowes superusers to administer:
    - Products
    - Categories
    - Users 
    - Posts
    - Email Addresses
    - Comments

### Features Left to Implement

- I'd like to add READ MORE function to Posts and allow Admins to administer Posts from a view within the website itself
- I'd also like to add Comment Functionality so users can respond to Posts
- Would alos like to allow logged-in users to rate products

## Technologies used 

* HTML and CSS programming languages
* [Balsamiq](https://balsamiq.com/) - wireframing tool
* [Slack](https://slack.com/) - networking and communications
* [GitHub](https://github.com/) - code repository
* [GitPod](https://www.gitpod.io/) - cloud dev environment
* [Bootstrap](https://getbootstrap.com/) - responsive sourcetoolkit with components and Javascipt plugins
* [fontawesome](https://fontawesome.com/v4.7.0/) - vector icons customisable through CSS
* [Google Fonts](https://fonts.google.com/) - open source web font collection
* [jQuery](https://jquery.com/) - add state to button
* [MongoDB](https://www.mongodb.com/) - database and collections
* [Heroku](https://dashboard.heroku.com/apps) - Cloud Applications
* [Stripe] (https://stripe.com/en-ie) - Payment Platform
* [Amazon AWS] (https://aws.amazon.com/) - Web Storage

## Testing 



- Navbar

    - Tested that navigation links linked to appropriate pages
    - Tested that nav links which should be visible were visible based on user session state
    - Tested that nav links which should be hidden were hidden based on user session state

- Homepage
    - Tested that buttons which should be visible were visible based on user session state
    - Tested that buttons which should be hidden were hidden based on user session state

- Register
    - Tested that Registrations were confined to the appropriate restrictions
    - Those restrictions being alpha/numeric characers only, and following the min-max count 

- Login 
    - Tested that Login always functioned properly, allowing only valid logins

- Logout 
    - Tested that logout always successfully logged-out users

- Build
    - Tested that all appropriate restrictions were enforced, namely
        - Stories must have all 4 parts selected
        - Randomization worked across all 4 story parts
        - Titles had to be eneterd with strict min/max values
        - A Genre had to be explicitly chosen
        - Cast had to have at least one person and no more than 3
    - If any of the above conditions were not met, tested that the approprite prompt appeared
        - Prompts included Modals for Min/Max cast
    - Tested that Publish button did correctly save to database

- Edit 
    - Tested that all the same Build functions were present as well as:
        - Cancel to reload the Blockbusters page
        - Update to save changes to database
        - Delete did delete Blockbuster with the defensive Modal to check before deleting

- Browse
    - Tested that Blockbusters from database did populate the Browse page
    - Tested that Blockbusters did appear in accordion card when clicked
    - Tested Search function for all indexes

- MyBB 
    - Tested that all user's own BlockBusters (and only theirs) were displayed

- About 
    - Tested that links to amazon.co.uk worked 
     

## TESTED on the Following:
    * Responsive devices on Google Developer Tools
    * iPhone 7, iPad Pro
    * OSX Browsers: Chrome, Safari


### Validator Testing

- HTML
  - No fatal errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fblockbuster-charliekranz.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JS 
   - JS validated but flags undefined and unused variables. All variables are defined and used so have ignored [https://jshint.com/](https://jshint.com/)
- Python
   - App.py is PEP8 compliant [Pep8 online](http://pep8online.com/)


## Debugging

- Accordion on blockbusters page were initially unable to target stories properly. Titles with spaces and/or a number at the start of title_name caused issues. Fixed by using ObjectId instead and adding a character to the start (BB).

- The selected casts weren't appearing as selected in the edit template. Using cast-checkbox class on edit template so that the selected cast appear chosen (thanks to Ronan for spotting that in particular)

- Edit template Updates were not sending cast selection changes. Changed Edit App Route from "cast_members": request.form.getlist("cast_members") to "cast_members": cast_members as request.form did not apply in this case. (Thanks to Ronan for spotting this)

- Caught missing else condition in edit_story.html which as preventing the Genre selection from properly displaying on edit.

### Unfixed Bugs 

- Register function delays after username chosen before password field can be accessed when using Safari for iOS

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    - [emailjs](https://www.emailjs.com/)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

### Instructions
1. Save a copy of the github repository located at https://github.com/charliekranz/aishling_dreammarket by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
    ```
    git clone https://github.com/charliekranz/aishling_dreammarket
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

    - If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

    ```json
    "terminal.integrated.env.windows": {
        "HOSTNAME": "<enter hostname here>",
        "DEV": "1",
        "SECRET_KEY": "<enter key here>",
        "STRIPE_PUBLISHABLE": "<enter key here>",
        "STRIPE_SECRET": "<enter key here>",
        "EMAILJS_USER_ID": "<enter key here>",
        "STRIPE_SUCCESS_URL": "<enter url here>",
        "STRIPE_CANCEL_URL": "<enter url here>",
        "AWS_ACCESS_KEY_ID": "<enter key here>",
        "AWS_SECRET_ACCESS_KEY": "<enter key here>",
        "AWS_STORAGE_BUCKET_NAME": "<enter bucket name here>",
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

11. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the ur. Here log in with your superuser account and create instances of ShippingDestination and Product within the new database.

13. Once instances of these items exist in your database your local site will run as expected.


## Heroku Deployment

To deploy Aisling Dreamshop to Heroku, do the following:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<your secret key>`
AWS_SECRET_ACCESS_KEY | `<your secret key>`
DATABASE_URL | `<your postgres database url>`
EMAIL_HOST_PASS | `<your secret key>`
EMAIL_HOST_USER | `<your heroku app hostname>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY| `<your secret key>`
STRIPE_SECRET_KEY | `<your secret key>`
STRIPE_WH_SECRET | `<your secret key>`
USE_AWS | `True`

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account and create instances of ShippingDestination and Product within the new database.

12. Once instances of these items exist in your database your heroku site will run as expected.


## Credits 

### Content 

- This project was based on the Boutique Ado from Code Institute Course

- Deployment and Testing steps taken (and lightly modified) from AJGreaves Django Github Project (https://github.com/AJGreaves/thehouseofmouse/blob/master/README.md)
- Icons used throughout the website are from [Font Awesome](https://fontawesome.com/)
- Basic Randomize code (with some of own additional tweaks) - https://jsfiddle.net/aqpwcoju/1/
- RandomKeygen was used for random passwords https://randomkeygen.com/
- Getlist fix (partial ) found at https://stackoverflow.com/questions/53344797/how-create-an-array-with-checkboxes-in-flask


### Acknowledgements
* My mentor Ignatius provided some very valuable planning insight, in particular with regard to setting-up my collections
* My mentor Chris provided excellent insight and encouragement at the mid and finalisation steps
* My friend Ronan offered real insight and suggestions on implementing code across both Python and Javascript


### Media
Images of a All links included below.


images used -

cosmos
https://pxhere.com/en/photo/1268143

fear
https://pxhere.com/en/photo/846223

adventure
https://pxhere.com/en/photo/1327741

scary night
https://pxhere.com/en/photo/656399

fallen kingdom
https://pxhere.com/en/photo/1460325

defending the kingdom
https://pxhere.com/en/photo/1413030

stardom
https://pxhere.com/en/photo/868620

flight
https://pxhere.com/en/photo/1625

the edge
https://pxhere.com/en/photo/1096270

microscopic
https://pxhere.com/en/photo/1582745

Natural Survival
https://pxhere.com/en/photo/1180528

the maze
https://pxhere.com/en/photo/398

calm rocks
https://pxhere.com/en/photo/1127997

cosmic energy
https://pxhere.com/en/photo/836648

Bubble Trouble
https://pxhere.com/en/photo/1022747

Crash Landing
https://pxhere.com/en/photo/629937

Station Orbit
https://pxhere.com/en/photo/22859

Hairnet
https://dlpng.com/png/6966725

Recorder / Replay
https://dlpng.com/png/7450753

Shareware Cable
https://www.mln.com.au/img/uploads/images/products/Huntkey-Black_cable_with_lightning.jpg

Tablet:
https://pxhere.com/en/photo/1349726

ReREM:
https://dlpng.com/png/7500379

Swirl:
https://pxhere.com/en/photo/1291377

### Disclaimer
This website was created for educational purposes only. 

<hr>

Code: Carousel
https://getbootstrap.com/docs/4.0/components/carousel/

Search Bar
https://mdbootstrap.com/docs/standard/forms/search/

Comments
https://djangocentral.com/creating-comments-system-with-django/
https://djangocentral.com/building-a-blog-application-with-django/
https://github.com/TheAbhijeet/Django_blog/blob/1/blog/models.py



