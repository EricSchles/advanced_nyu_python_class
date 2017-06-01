# Project 1 - Github

# Projects Overview

Projects will be multi-week projects where you will code real projects, adding features overtime.

# Project Explanation

In this project you will implement a series of weekly deliverables.  

Week 1:

Write a github api.

This will be a Flask-App that you deploy.  The api should support:

* git pull - pull only pulls the last record.
* git push

Make sure you deploy this code: https://devcenter.heroku.com/articles/getting-started-with-python#introduction -- docs

In order to test your routes please use requests.  

Specifically use requests.get for pull and requests.post for push.

This is demo code that should work:

```
>>> import requests
>>> requests.post("http://localhost:5000/push/'this is the code that Im uploading'")
'success'
>>> requests.get("http://localhost:5000/pull")
this is the code that Im uploading
>>> 
```
This will allow you to download and upload all code for the current project, via a restful api.  

Note:  All code *must* be version controlled.  So you will have to be able to support pulling down a specific commit in your history as well as resetting the head to some other point in the past.  You don't need to support these functions in week one, but you should write your code in such a way that it is easy to extend to this case, which you will be doing in week 3.

Week 2:

Write a commandline interface that supports the following four functions:

* git add
* git commit
* git pull
* git push

The cli(commandline interface) will be how users interact with your deployed api.

Week 3:

* Allow for pulling down specific versions of the code base.  Also allow for resetting the head of your code base to the current version of the code.

* allow for multiple branches of your code base.

* implementing differencing between branches.

All code should have multiple tests.  And must use the py.test framework for testing.
