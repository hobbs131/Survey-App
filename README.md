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
git push heroku main
heroku open
```

local setup:
```
# setup
pipenv install
pipenv shell

# create .env with datastore connection params (see .env.example)
heroku pg:psql
# run schema.sql against the DB

# run
heroku local dev
```

Hosted on heroku at <https://immense-eyrie-00146.herokuapp.com/>
