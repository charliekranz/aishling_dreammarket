<img src="https://ckranz-aishling-dreamshop.s3.amazonaws.com/media/water-nature-horizon-sky-air-lake-1327741-pxhere.com_TkExcn8.jpg">

# Aisling Dreamshop

Overview

***

## UX (User Experience)

### User Stories
- #### First Time Visitor Goals
    1. As a First Time Visitor, I want to clearly understand the features and functionality of the website.
    2. As a First Time Visitor, I want to be able to quickly view Products.
    3. As a First Time Visitor, I want to be able to easily register, login and logout.
    5. As a First Time Visitor, I want to be able to search and sort Products.
    6. As a First Time Visitor, I want to be able to make secure transactions.

 - #### Returning Visitor Goals
    1. As a Returning Visitor, I want to be able to edit or update my profile.

- #### Frequent User Goals
    1. As a Frequent User, I want to be able to return to Aisling Dreamshop and search/purchase products.

- #### Superuser Goals
    1. As a Superuser, I want to be able to easily add or edit Products.

- #### Wireframes
    - Wireframes: [View](ttps://ckranz-aishling-dreamshop.s3.amazonaws.com/media/water-nature-horizon-sky-air-lake-1327741-pxhere.com_TkExcn8.jpg)

## Design

- ### Branding 
    - The Aisling name derived from the Irish word for dream - "Aisling"
    - Dreamshop 
    - The tagline helps reinforce the premise, that we live in a world where dreams can be manufactured, sold and shared
    - Clear iconography for key features and functions

- ### Colours
    - Using a simple midnight blue and gold schematic
    - Additional colour variations to highlight functions based on Bootstrap model

- ### UI
    - Clean, simple UI
    - Larger screens allow for some 3-4 column layouts
    - Smaller screens use 1-2 column layout throughout and some font-size reduction

- #### Typography
    - Anton font for more compressed Block+Buster+Builder branded text
    - PT Mono monospace font for some featured text sections - to evoke the typewriter feel of a screenplay writer
    - Sans Serif for body and smaller text


## Features

### Existing Features

- __Brand and Navigation Bar__

  - The brand and navigation bar displays the site name and gives users the ability to navigate throughout the site
  - The navigation bar displays navigation options based on the uswers's current state 
    - Logged-in Users will see the Build and Logout Options (Login and Register options will be hidden)
    - Logged-out Users will see the Login and Register options (Logout and Build will be hidden)


- __Home Page__

  - The Homepage established the basic concept of Block+Buster+Builder
  - It allows user to Browse current content or to Build their own (after login/registration)


- __Browse Page__

  - Displays all current Block+Buster Content 
  - Allows user to search by Title, Story or Cast 


- __MyBB Page__

  - Displays all user's own current Block+Buster Content  


- __Build Page__

  - Allows user to create Block+Busters 
  - In particular the Randomize Story Feature is a key fun aspect

<img src="https://blockbuster-charliekranz.herokuapp.com/static/MS3-project-files/build.jpg">


- __Edit Page__

  - Allows user to edit any aspect of their Block+Buster Content
  - Allows User to Delete their Content entirely 


### Features Left to Implement

- Allow users to recover password
- Paginate - would like to Paginate every 30 Blockbusters
- Re-index db to include username which would allow users to search by usernames
- Username search functionality would also allow me to use Jinga templating to give users a "Share your BBs" link atop MyBB page
- My friend Ronan mentioned a Python library that allows for pluralisation of text, which I'd like to invstigate. Failing that some more complex programming to use appropriate singular and/or plural string for story sections.
- Possibly add option for people to suggest Block+Buster story content, movies to use as inspiration or new actors to cast section
- An age-range sort function for actors
- Twitter and Facebook share options (possibly)
- Would like to add a disclaimer about removing old BB content occassionally
- Might allow for longer titles and force linebreak/wrap if no space before end of BB accordion


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

* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - web application library
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - templating engine

## Testing 


- Navbar

I will add a link to XLS sheet for testing similar to Chris's

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

- Deployment steps taken (and lightly modified) from AJGreaves Django Github Project (https://github.com/AJGreaves/thehouseofmouse/blob/master/README.md#deployment)
- Icons used throughout the website are from [Font Awesome](https://fontawesome.com/)
- Basic Randomize code (with some of own additional tweaks) - https://jsfiddle.net/aqpwcoju/1/
- RandomKeygen was used for random passwords https://randomkeygen.com/
- Getlist fix (partial ) found at https://stackoverflow.com/questions/53344797/how-create-an-array-with-checkboxes-in-flask


### Acknowledgements
* My mentor Ignatius provided some very valuable planning insight, in particular with regard to setting-up my collections
* My mentor Chris provided excellent insight and encouragement at the mid and finalisation steps
* My friend Ronan offered real insight and suggestions on implementing code across both Python and Javascript


### Media
Images of actors were mostly pulled from Wikipedia.. All links included below.
- Charlize Theron https://en.wikipedia.org/wiki/Charlize_Theron#/media/File:Charlize-theron-IMG_6045.jpg
- Judi Dench - https://en.wikipedia.org/wiki/Judi_Dench#/media/File:Judi_Dench_at_the_BAFTAs_2007_(cropped).jpg
- Tilda Swinton - https://en.wikipedia.org/wiki/Tilda_Swinton#/media/File:Tilda_Swinton_by_Gage_Skidmore_(cropped).jpg
- Sandra Oh - https://m.media-amazon.com/images/M/MV5BMTMyNzYyNDE4MV5BMl5BanBnXkFtZTcwOTkxMDQ2NA@@._V1_.jpg
- Dwayne Johnson https://en.wikipedia.org/wiki/Dwayne_Johnson#/media/File:Dwayne_Johnson_Hercules_2014_(cropped).jpg
- Jackie Chan - https://upload.wikimedia.org/wikipedia/commons/8/8b/Jackie_Chan_July_2016.jpg
- Will Smith https://en.wikipedia.org/wiki/Will_Smith#/media/File:TechCrunch_Disrupt_2019_(48834434641)_(cropped).jpg
- Lin-Manuel Miranda https://en.wikipedia.org/wiki/Lin-Manuel_Miranda#/media/File:Lin-Manuel_Miranda_by_Gage_Skidmore.jpg
- Samuel L. Jackson https://en.wikipedia.org/wiki/Samuel_L._Jackson#/media/File:Samuel_L._Jackson_2019_by_Glenn_Francis.jpg
- Viola Davis - https://en.wikipedia.org/wiki/Viola_Davis#/media/File:Viola_Davis_by_Gage_Skidmore.jpg
- Meryl Streep - https://en.wikipedia.org/wiki/Meryl_Streep#/media/File:Meryl_Streep_December_2018.jpg
- Melissa McCarthy - https://en.wikipedia.org/wiki/Melissa_McCarthy#/media/File:Melissa_McCarthy_in_2018_(cropped).jpg
- Elliot Page - https://media.vanityfair.com/photos/60884831301e0fee4a0c978d/master/w_2560%2Cc_limit/elliot-page-interview-lede.jpg
- Denzel Washington - https://www.thextraordinary.org/media/k2/items/cache/2e2c1711fe12b24ae23d95c35bfd21c2_L.jpg
- Leonardo DiCaprio - https://media.vanityfair.com/photos/60255707b9f9b86e12a6600a/2:3/w_2185,h_3278,c_limit/1205143953
- Amy Adams - https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Amy_Adams_UK_Nocturnal_Animals_Premiere_%28cropped%29.jpg/440px-Amy_Adams_UK_Nocturnal_Animals_Premiere_%28cropped%29.jpg
- Joaquin Phoenix - https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Joaquin_Phoenix_at_the_2018_Berlin_Film_Festival.jpg/440px-Joaquin_Phoenix_at_the_2018_Berlin_Film_Festival.jpg
- Ryan Gosling - https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Ryan_Gosling_in_2018.jpg/440px-Ryan_Gosling_in_2018.jpg
- Emma Stone - https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Emma_Stone_at_the_39th_Mill_Valley_Film_Festival_%28cropped%29.jpg/440px-Emma_Stone_at_the_39th_Mill_Valley_Film_Festival_%28cropped%29.jpg
- Saoirse Ronan - https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Saoirse_Ronan_at_BAFTA_2016_%281%29_%28cropped%29.jpg/440px-Saoirse_Ronan_at_BAFTA_2016_%281%29_%28cropped%29.jpg 
- Idris Elba - https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Idris_Elba-4580_%28cropped%29.jpg/440px-Idris_Elba-4580_%28cropped%29.jpg
- Michael B. Jordan - https://en.wikipedia.org/wiki/Michael_B._Jordan
- Ralph Fiennes - https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Ralph_Fiennes_from_%22The_White_Crow%22_at_Opening_Ceremony_of_the_Tokyo_International_Film_Festival_2018_%2831747095048%29.jpg/440px-Ralph_Fiennes_from_%22The_White_Crow%22_at_Opening_Ceremony_of_the_Tokyo_International_Film_Festival_2018_%2831747095048%29.jpg
- Margot Robbie - https://en.wikipedia.org/wiki/Margot_Robbie_filmography
- Letitia Wright - https://en.wikipedia.org/wiki/Letitia_Wright
- Peter Dinklage - https://media.newyorker.com/photos/5de59f9310863b0009e9d541/2:2/w_2178,h_2178,c_limit/Schulman-PeterDinklage.jpg
- Catherine Keener - https://m.media-amazon.com/images/M/MV5BMjIwMzQ1Mzg1MF5BMl5BanBnXkFtZTcwNTE4MTU5MQ@@._V1_.jpg 
- Regina King - https://media.vanityfair.com/photos/5c61e52f50f462477e50ddb6/2:3/w_1332,h_1998,c_limit/t-regina-king-cover-oscar-issue.png
- Steve Buscemi - https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Steve_Buscemi_crop.jpg/440px-Steve_Buscemi_crop.jpg
- Cate Blanchett - https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Cate_Blanchett_Cannes_2018_2_%28cropped%29.jpg/


### Disclaimer
This website was created for educational purposes only. 




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

rock icon
https://pxhere.com/en/photo/726703

head icon
https://pxhere.com/en/photo/1640137

<hr>

Code: Carousel
https://getbootstrap.com/docs/4.0/components/carousel/

Search Bar
https://mdbootstrap.com/docs/standard/forms/search/


DEPLOYMENT - from John)Lynch_alumnus post on Slack: https://code-institute-room.slack.com/archives/C0L316Z96/p1571912291489200

# Deployment

- The project's git repository is hosted at [Github][14] and a push to this remote origin triggers a subsequent push and new build on [Heroku][8], where the project is hosted on the Heroku free tier.
- For security, all secret keys (Django, Amazon, Snipcart) are stored in Heroku config variables (environment variables).
- The database used is Heroku's own Postgresql database.
- The project uses [Amazon S3 free tier][6] for non-volatile static and media files, like CSS, icons, uploaded user profile pictures and the actual images displayed on the site.
- The project uses [Snipcart][7] to handle user purchase orders, shopping cart, payments and backend notifications
- The deployed site can be accessed with a web browser at [Teraspora Fractals][15]

### Deployment Procedure

    The project is called `trif`, and contains two non-system apps, `fract` and `users`.

    1. Clone the repository into a clean directory on your local machine.
    
    2. Create an account at Heroku and create an app.
    
    3. Create a PostgreSQL database as a Heroku addon for the app.
    
    4. Set up a 'bucket' on Amazon S3 for static and media file storage.
    
    5. Upload appropriately-named images to S3 and adjust settings in `settings.py`.   The image naming schema is demonstrated in the comments in fract/img_params.py.
    
    6. Store Django secret key, AWS secrets, Database keys etc. as Heroku 'Config Vars', or environment variables:
        - AWS_ACCESS_KEY_ID
        - AWS_SECRET_ACCESS_KEY
            These two from Amazon S3 account
        - DATABASE_URL
            From Heroku
        - EMAIL_USER
            Email address to send password reset links from
        - EMAIL_PASS
            Special app password for above address
        - SECRET_KEY
            Django secret key

    7. Set up a Gmail account, enable app access for the project, enter the address and special app-enabled password in the two EMAIL_* vars above.
    
    8. Push the code to Heroku, either directly or via Github.

    9. Make and run migrations on Heroku.

    10. Create a superuser on the PostgreSQL database in order to access Django's Admin interface.
    
    11. `DEBUG` is set to `True` in `settings.py` only if `DEVELOPMENT` is set as an environment variable, so be sure not to set any config var with this name on the Heroku server as doing so risks exposing secrets in error messages.

    12. When all seems to be working, run the app on Heroku (`heroku open -a <your Heroku App Name>`).

    13. To run the project for real ecommerce disable the testing mode in Snipcart's dashboard.

