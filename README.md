# Survey-App
Simple full-stack survey application

Backend:
- Python + Flask + PostgreSQL

Frontend: 
- HTML/Pure CSS

Heroku Setup:

```
heroku setup:

heroku create
heroku addons:create heroku-postgresql:hobby-dev
# use `heroku config` to see environment variables, and setup a personal .env file
# see .env.example and make a .env file. Note the database URL can be copied directly from heroku's console.
git push heroku main
heroku open
```

Hosted on heroku at <https://immense-eyrie-00146.herokuapp.com/>
