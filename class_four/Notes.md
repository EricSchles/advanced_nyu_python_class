
Blog post for hw:
[http://jmduke.com/posts/a-gentle-introduction-to-itertools/](http://jmduke.com/posts/a-gentle-introduction-to-itertools/)

How to catch syntax errors in your code:

* http://flake8.pycqa.org/en/latest/

* https://www.python.org/dev/peps/pep-0008/

* http://www.flycheck.org/en/latest/glossary.html#term-init-file - use for on the fly checking of flake8

Step 1)

Set up a seperate github repository for your code base - note heroku looks for remotes and won't work off of any local code.  This is known as web hooks.

Step 2)

`rm -Rf .git` - removing existing git repo references.

Step 3)

Set up a new repo on github. (or other git service).

Step 4)

Remove existing migrations locally.  Note: local migrations should never go up to github.
(Unless they are consistent with all other migrations on dev or master).

Follow steps outlined here: 

https://devcenter.heroku.com/articles/getting-started-with-python#introduction

Step 5) 

heroku login - logs you into heroku with a specific set of credentials (you can have multiple accounts)

Step 6)

heroku create - creates the repo and initializes the space for you to use on heroku's assets.

Step 7) 

git push heroku master - pushs all changes commited to your remote (github in this case) up to heroku.

What you'll need defined at this stage:

* requirements.txt (your packages and libraries)
* Procfile - how to run your server (usually gunicorn or honcho are defined here)
* runtime.txt - the version of your interpreter or compiler
* (your source code)

Step 8a)

Verify your code went up successfully - 

heroku open - launches a browser window to your web app.

Step 8b)

Make sure your app is ready for deployment.

Step 9)

Setup heroku:

`heroku addons:create heroku-postgresql`


Step 10)

`heroku run bash` - opens a bash shell on your heroku instance.

`python`

```
>>> from app import db
>>> db.create_all()
```

Step 11)

Ensure migrations work on the server.

`heroku bash run`

`python manager.py db init`

`python manager.py db migrate`

`python manager.py db upgrade`



