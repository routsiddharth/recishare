# recishare
Recipes no know borders.

## Inspiration

recishare was built on solving 2 problems: how people rarely go out of their comfort zones and the growing obesity epidemic. 

We rarely want to try food outside of what we have already eaten, and there is a whole world of delicious food which stays out of the spotlight. With recishare, I aim to shine the spotlight on those dishes which are often ignored, and encourage others to try them. 

Obesity rates have quadrupled in the last 40 years. This is due to a variety of reasons, but it is mainly due to the rise of fast food with its unprecedented convenience. Most people abandon cooking at home in favor of convenient and cheap fast food, despite how unhealthy it may be. I hope recishare makes cooking at home easy and convenient, incentivizing people to opt out from unhealthy food.

In the immortal words of Chef Gusteau from the Pixar film Ratatouille, "Anyone can cook."

## What it does

recishare is a platform where anyone can share their recipes with the world. 

![recishare homepage](https://i.imgur.com/HccQZbT.png)

Fist, you must register for your account. Once you register, a hash of your password is stored in our database so that your passwords are stored securely. From there, you can log in and your password is checked against the hash and verified. 

![recishare register page](https://i.imgur.com/t0UDOcw.png)

The first thing you can do once you log in is that you can post a recipe. Each recipe consists of a title, introduction, recipe, image URL, and meal. Each recipe is given a randomly generated unique 10 character code so that they can be shared with friends and family easily.

![recishare post page](https://i.imgur.com/1x1oazG.png)

You can search all the recipes in our database by using keywords, the recipe's unique code, or if you don't know what you want to cook, you can choose a meal and be given a random recipe from that meal. 

![recishare search page](https://i.imgur.com/Hz1iQjH.png)

You can also rate recipes on a 10 point scale. When viewing recipes, the average of all reviews of that recipe is displayed. 

## File descriptions

### ```static/styles.css```

 - Contains all the custom CSS for the project

### ```templates/apology.html```

 - Template for error page
 - Takes 2 parameters
    - code: Error code
    - message: Custom error message

### ```templates/home.html```

 - Template for homepage
 - Takes 1 optional parameter
    - alert: Custom alert
 - Has search form (sends POST to /search)

### ```templates/layout.html```

 - Basic layout for every page
 - 2 blocks
    - main: Main content of page
    - title: Title of page (shown in head)

### ```templates/login.html```

 - Layout for login page
 - Has login form (sends POST to /login)

### ```templates/home.html```

 - Layout for new post page
 - Has new post form (sends POST to /post)

### ```templates/register.html```

 - Layout for register page
 - Has register form (sends POST to /register)

### ```templates/search.html```

 - Layout for search page
 - Has search by keyword form (sends POST to /search)
 - Has random recipe form (sends POST to /viewpost)
 - Has search by code form (sends POST to /viewpost)

### ```templates/search_results.html```

 - Layout for search results page once form is submitted to /search via POST
 - Takes 2 parameters
    - query: Search query
    - recipes: Results from query as got from ```recipes.db```
 - Has view post forms (sends POST to /viewpost) for each search result

### ```templates/viewpost.html```

 - Layout for viewing a post
 - Has review recipe form (sends POST to /review)

## What's next?

I am improving the UI of recishare and trying to make it stand out, making it unique. So far, almost all of my CSS has been built using Bootstrap, and I would like to change that.
