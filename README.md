![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome charliekranz,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. The last update to this file was: **July 2, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!



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

