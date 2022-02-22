
# Recipeasy - Milestone 3 Project 

"Recipeasy" is a commmunity focused website, where users can create and search for recipe ideas.

The site is created to engage users of all ages, backgrounds and tastes, and so it was created with a clean, neutral style. 

The site was created using HTML, CSS, JavaScript and Python, ensuring it is fully responsive across chosen devices. 


## UX

### User Stories

#### First Time User Goals

i. As a first time user, I want to easily understand the main goal of the site.

ii. As a first time user, I want to be able to naviagte through the site easily.

iii. As a first time user, I want to be able to register as a user of the site. 


### Returning Users Goals

i. As a returning user, I want to be able to log in to my created account. 

ii. As a returning user, I want to be able to log out of my created account. 

iii. As a returning visitor, I want to be able to add a recipe.

iv. As a returning user, I want to be able to edit a recipe I have added. 

v. As a returning user, I want to be able to delete a recipe I have added.

### Admin Goals

i. As an Admin of the site. I want to see all recipes. 

ii. As an Admin of the site, I want to see all users.

iii. As an Admin of the site, I want to be able to edit all recipes.

iv. As an Admin of the site, I want to be able to delete all recipes.

v. As an Admin of the site, I want to be able to delete all users. 


## Design

### Strategy Plane

Recipeasy aims to provide users with a site that will provide a recipe hub for users to browse through and add to. 

The objective of the project is to give users the ability to navigate through the site, create, log in to and log out of an account. 

It also aims to provide users the ability to add recipes, and to edit and delete recipes that they have created. 

### Scope Plane 

The project aims to provide an interactive website experience to the user. 

The developer has used the following technologies; HTML, CSS, Flask, JavaScript and Python to create a user centric website. 

### Structure Plane

As the aim of the site is to provide an interactive website to the users. The site was developed to be a multi-page site. The User has access to navigation in the top right of the page.

The user has the ability to navigation to the Home page, their profile page and login or out from the top right of the page and from the slide out menu on Mobile.

Please see wireframes in static/images for initial plan for structure. 

### Skeleton Plane

Please see static folder -> images folder - wireframes folder for initial design theories for this site. These wireframes acted as guidelines for the main structure of the site.

### Surface Plane 

#### Colour Scheme 

The colour scheme used for this website aimed to create a bright, clean, neutral and inviting visual experience for users. 

Light Blues, White and Orange tones were used to provide contrast between menu items and buttons.


#### Typography 

I decided to use Google Fonts Popppins for this site. Poppins is extremely adaptable to most sites and there are a number of font weights and styles available should a developer so choose. It is also an extremely neat and easily readable font, which can be used for both headings and paragraph text, and lends itself to the main goal of the site which is to be useable for all ages. 


## Features

### Existing Features 

- Header with Navbar for users to navigate to different areas of the site from. 
- Footer 
- Registration page with form for users to complete for sign up
- Log in page for registered users to log in
- Log out button in Navbar which returns users to the log in page



## Languages and Frameworks

i. [HTML](https://en.wikipedia.org/wiki/HTML)

ii. [CSS](https://en.wikipedia.org/wiki/CSS)

iii. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

iv. [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

v. [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))

vi. [Google Fonts](https://en.wikipedia.org/wiki/Google_Fonts)


## Deployment

### Database Deployment

### Application Hosting - Heroku 

The site is hosted using [Heroku]("https://en.wikipedia.org/wiki/Heroku"), deployed directly from the main branh of the GitHub repository. The deployed site will update automatically as new commits are pushed to the main branch.

#### Creating a Heroku Application

Sign up for and Log in to [Heroku]("https://dashboard.heroku.com/")

- Navigate to the Heroku dashboard.
- Select "New"
- Select "Create new app"
- Add new app details to form:
    - Add app name (must be unique)
    - Select region
    - Click "create app"

#### Setting Environmental Variables 

- From the Heroku dashboard:
    - Select your created app from the list

- Select "settings" from the top menu:
    - Under "config vars", select "reveal config vars"
    - Add variables in key-value pairs, click "add" if more pairs are needed. 

#### Deployment 

- Create files necessary for deployment in the GitHub repository:
    - requirements.txt
        -  In your IDE termninal, type pip freeze > requirements.txt
            - This lists the required python modules for Heroku to install.
    
    - Procfile
        - This tells Heroku the command to launch the app. 
            - In your IDE terminal, type python app.py > Procfile

    - gitignore (optional but best practise)
        - This file lists files and directories which should not be made public when pushing to GitHub for security reasons. 
            - In your IDE terminal, type touch .gitignore
            - As mentioned above, within this file, list files and directories to be excluded from live deployment.
            - Save in your repository.

- From the application menu in Heroku: 
    - Select "Deploy"
    - Choose deployment method:

        - Github:
            - Select the correct Github account
            - Type and select the repository you wish to deploy. 
            - Select "connect"

        - Manual Deployment:
            - Choose the correct branch to deploy from the drop down menu.
            - Select "deploy branch"
            - Unless there is an error within your code, Heroku will return "Your app has successfully deployed"

        - Automatic Deployment: 
            - From the application menu on Heroku:
                - Select "deploy"
                - Confirm that app is connected to the repository
                - In the "automatic deployment" section, select "enable automatic deployment".

### Forking the GitHub Repository 

The GitHub Repository can be forked to make a copy of the original repository on the GitHub account to view and/or make changes without affecting the original repository in the following way.

- By logging in to GitHub and locating the GitHub Repository.
- Selecting the "Fork" button at the top of the Repository (it is located at the top right of the page under the profile image).
- There should then be a copy of the original repository in your GitHub account.

### Making a Local Clone 

The GitHub Repository can be cloned in the following way:

- By logging in to GitHub and locating the GitHub Repository.
- Under the repository name, clicking the dropdown button marked “Code” and then selecting "Clone or download".
- Copying the link under "Clone with HTTPS", to clone the repository using HTTPS.
- Opening Git Bash.
- Changing the current working directory to the location where you want the cloned directory to be made.
- Typing git clone, and pasting the URL copied in Step 3.
- Pressing Enter to create the local clone.



## Credits

### Research 

Inspiration for this project was taken from the Code Institute Task Manager mini project, as well as inspiration from the community slack channel.

- In particular, [Plum Recipes]("https://plum-recipes.herokuapp.com/") by Sean Young and [Wanderlust Recipes]("https://wanderlust-recipes.herokuapp.com/") by Russ Oakham, both of which were excellent exmaples of the end goal of this project. 

## Content

Images used for this project on the developers side are taken from [Unsplash]("https://unsplash.com/")

## Acknowledgements

I would like to thank the staff at Code Institute for their help and communication during the creation of this project. 

I would also like to thank my mentor Dick Vlaanderen for his guidance and my family for their support. 
