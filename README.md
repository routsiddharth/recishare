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

## How I built it

I built recishare over a period of 28 hours, using Python and the skills I learnt from online courses. In addition to vanilla Python, I used Flask for the UI and SQL for the backend. To connect the database to my program, I used cs50's inbuilt sqlite3 library. The UI was the first thing I built, followed by the backend and finally, I connected both together.

## Challenges I ran into

I had never used SQL in conjunction with full-fledged Python application before, so a lot of my time was spent learning how to use it. I also did not have any experience with password management, so I had to learn how to safely deal with them and not compromise the security of users who sign up. Additionally, due to the scale of the project, there was a lot of data that needed to be stored in a format where they could reference one another and be linked to one another, so a lot of time was spent drawing out tables in a notebook.

As for problems, generating unique URLs for each recipe was an extremely challenging task, as I required JavaScript for that. To solve this, I gave each recipe a unique sharable code which could be shared among friends and family much more easily than a URL.

## Accomplishments that I'm proud of

In the end, I managed to build a fully functioning recipe sharing application, where you can post, search for, and view recipes. The backend links to the frontend perfectly, and the entire project maintains a consistent theme. I am also proud of the UI which was partially built using Bootstrap, and I am amazed at how beautiful the application looks with it. This is by far the largest project I have built, and I hope that I can continue this golden streak.

## What I learned

In this project, I had to learn various different languages, frameworks and concepts, including Bootstrap, SQL, sqlite3, and password management. These were applied at a relatively basic level for this project, and I hope to use them further in future projects. Additionally, I learnt to solve problems creatively, like the aforementioned problem with the URLs and the (unconventional) solution I implemented.

## What's next for recishare

I aim to improve the UI of recishare next, and implement a markdown system into posting recipes so that formatting recipes becomes possible. Furthermore, I would like to implement reviews into recipes, so that people can leave deeper and more specific comments on the recipes.
