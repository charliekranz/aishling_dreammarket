<img src="https://ckranz-aishling-dreamshop.s3.amazonaws.com/media/wireframes/Screen-Shot-2021-07-30-at-17.56.57.jpg">

# Aisling Dreamshop

Aisling Dreamshop is an ecommerce website for the imagination. We can't buy, sell or create customised dreams but what if we could? If we could, you might buy your Dreams from Aisling Dreamshop!

In learning how to create a ecommerce website using Python and Django I wanted to play with the idea of this technology. I felt the ethereal concepts of dreams and dream ingredients would be fun to develop and manage.

One thing I've learned in working on this project is just how much more can be done and learned within these building blocks, which I intend explore further.

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

<img src="https://ckranz-aishling-dreamshop.s3.amazonaws.com/media/wireframes/screens.jpg">

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

- I'd like to add READ MORE function to each Post and also allow Admins to administer Posts from a view within a webpage
- I'd also like to add Comment Functionality so users can respond to Posts
- Would also possibly allow logged-in users to rate products


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

## Manual Testing
This is the the manual testing undertaken while developing the site. 

### Testing undertaken on desktop

These steps were repeated on a Mac in Chrome and Safari browsers 

#### Elements

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirmed when logged out "Sign Up" and "Log in" are visible and that "My Profile" "Log out" and "Product Management" are not.
    - Log into the site, confirm that options "My Profile" and "Log out" are visible and that "Sign Up" and "Log in" are not.
    - Additionally checked that when logged in, if user is NOT a Superuser that "Product Managements" does not appear and that if user is Superuser, it does.
    - Click the individual "Products" links in the navbar, confirm that all sections of the shop are listed in the dropdown menu.
    - Add an item to the basket, confirm that the update toast message displays the correct product quantity and price.
    - Add an item to the basket, confirm that the basket icon updates with the correct price displayed.
	- Searched Products Using Product Name and Description text - confirmed results matched expectations.

#### Home Page

1. Carousel
    - Allow Carousel to auto-run, confirm that all images and text display as expected.
    - Adjust width of browser window, confirm carousel displays in an attractive way.

2. Call to action button
    - Clicked SHOP NOW and confirmed that it loaded the correct Products View

#### Products Page 

1. Breadcrumbs
    - Click Products links, confirm it loads Products

2. Sorting options
    - Select the different sorting options from the menu one by one, confirm that the products update correctly and are re-sorted/displayed in the correct method.

3. Product Details
	- Confirm the appropriate Product Detail view appears when Product Image clicked

#### Product Detail Page 
	- Keep Shopping button loaded appropriate Products page

1. Product Category
	- Check that Correct Category displayed and that it links to Category Products Page

2. Product details
    - Confirm that the listing title, price, and description match those in the database for the product.

3. Product  image
    - Confirm that the correct image is displayed.

4. Product information
    - Confirm that all information under the description is as expected. 

5. Product Sizes
	- Confirm that if sizes options are available for product, that they are displaying as expected.

6. Quantity selection
    - Quantity updates confirmed (adding additional purchase quantities)

7. Add to Basket button
    - Click the "add to basket" button. Confirm that the appropriate Quantity is added and displayed in Toast Message and Basket Page 
    - Add additional Quantity to Basket and confirmed Toast Message and Basket updated correctly

8. Admin Links
    - Confirmed Edit and Delete links appear for Superusers
    - Confirmed Edit link displays Correct Product Edit View
    - Confirmed Edit View displays orrect information
    - Confirmed Edited data updates correctly in Product View when updated
    - Confirmed Delete link Deletes Product


#### Sign Up Page

- Confirmed correct text and fields displayed
- Cofirmed Log In link linked to Login Page
- Confirmed correct alerts displayed is any required fields incorrectly submitted
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.
- Confirmed when all Sign Up steps executed properly and that Verify message appears
- Confirmed Verifcation email received and that link verified Sign Up

#### Login Page

- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to Home Page, correct Toast Message appears and that account is logged-in

#### My Profile Page

- Go to the account page of a newly created user. Confirm that te profile info form is populated with the correct data
- Fill in the form correctly, confirm that the "Your account info has been updated." message is shown to the user and that the reloaded form is now populated with the new data.
- Confirm that a user with previous orders has correct info appearing in Orders History
- Confirm that all data in the orders on the account page is accurate

#### Log Out Page

- Add a new product to the users cart. Click the "log out" link in the navigation bar. Confirm that the user is logged out and their cart has been cleared
- Click the "Log in again" link on this page, confirm that the user is taken back to the login page

#### Basket Page

- Go to the cart page when not logged in to the site, confirm that "Your Dreamshop Basket is empty" displays and the Keep Shopping button is displayed and works as expected
- Log in and go to the cart page with nothing in the cart. Confirm that the message "Your cart is empty!" displays and the Keep Shopping button is displayed and works as expected
- Add items to the cart and return to the cart page, confirm that all items in the cart are displayed correctly, with the correct amounts requested by the user
- Adjust the quantity field and click Update confirm that the shopping cart subtotal is updated to reflect the change
- Click the delete button on a listing, confirm that the cart page is reloaded with that item removed from the cart
- Delete all items from the cart, confirm that the cart page is reloaded to reflect the empty cart

#### Secure Checkout Page

- Confirm Order Summary display correct information including Product info, ISubtotal and Grand Total
- Confirm Form fields auto-populate if user logged in
- Confirm Form fields are blank if user not logged-in (Guest)
- Confirm Adjust Basket button links to Basket and allows user to correctly modify Basket Details
- Confirm all expected form validation mesures are enforced and appropriate messages display
- Confirm Complete Order button executes purchase
- Confirm Stripe Dashboard logs the purchase correctly
- Confirm Confirmation Page Displays
- Confirm Toast message appears

#### Order Confirmation Page

- Confirm the inormation displayed matched order placed
- Confiirm Top Rated Button links to Top-Rated Products Page

#### Toast Messages
- Confirm Toast Messages appear as expected and respond correclty when closed with 'x'

#### Product Management Page
- Confirm Product Management form appears as expected
- Confirm all validation requirements are endoforced and displayed as necessary
- Confirm images added without image use placeholder image

#### Updates Page

- Confirmed correct text displayed in About Section
- Confirmed Posts displaying correctly


### Testing undertaken on tablet and phone devices

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
    - Open the website on mobile, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.
    - Click the "Shop" dropdown menu, confirm that the shop sections are displayed. 
    - Add something to the cart, confirm that the user basket updates and displays correctly.

3. Shop pages
    - Confirm that the product list is displayed one on top of each other on mobile, and 3 to a row on tablet.
    - Confirm that all clicks and swipes operate as expected on touch screen.

4. Checkout pages
    - Check that the display of elements matches the expected layout for mobile and tablet devices.

5. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, menus, forms and other elements are the correct proportions and easily clickable with a finger.


### Validator Testing

- HTML
  - No fatal errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fblockbuster-charliekranz.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JS 
   - JS validated but flags undefined and unused variables. All variables are defined and used so have ignored [https://jshint.com/](https://jshint.com/)
- Python
   - Python files are PEP8 compliant (some lines too long and unused Class / Objects alerts remain)


## Debugging

- Gitpod and or the Project template seemed to have a conflict in the last week/s of development requiring me to use the unset DATABASE_URL command to run site. 

- The Heroku Database failed nearing end of development. Scott and John (CI tutors) assisted me in creating json files and refreshing DB.

- Confirmation emails seemed to experiencing delays. Igor helped me see that this was due to Heroku Development = True variable.

### Unfixed Bugs 

- PEP8 Problems on checkout/webhook_handler.py (1) blank line contains whitespace [29, 1], (2) trailing whitespace [35, 10] logged errors to the terminal when fixed. Because of this I left this code with the whitespaces.

- Heroku site was cacheing unintentionally on Chrome Desktop, forcing me to use Private Browsing to effective;y load the latest version of the site. I wouldlike to better understand why this is happening, though expect it is a Heroku-related issue

- Gitpod and or the Project template seemed to have a conflict in the last week/s of development requiring me to use the unset DATABASE_URL command to run site. Would like to better understand the issue and ensure it isn't having further ramifications to the project. 

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

11. You can now run the program locally with the following commands: 
    ```
    1. unset DATABASE_URL (If using Gitpod with Code Institute template)
    2. python manage.py runserver
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
- RandomKeygen was used for random passwords https://randomkeygen.com/

### Acknowledgements
* My mentor Chris provided some helpful insight and encouragement
* Carousel code taken and modified from Bootstrap  - https://getbootstrap.com/docs/4.0/components/carousel/
* Search Bar code taken and modified from - https://mdbootstrap.com/docs/standard/forms/search/
* Posts code adapted from The Abhijeet Blog: 
https://djangocentral.com/building-a-blog-application-with-django/
https://github.com/TheAbhijeet/Django_blog/blob/1/blog/models.py


### Media
Images Credits included below.

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






