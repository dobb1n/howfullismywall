# howfullismywall
How full is my wall? 

This is a python Flask app running on google cloud app engine, google's serverless hosting platform. It uses a google datastore backend. 

The flask app makes a query of the database and returns the answer as a list to the jinja template which iterates over the list. This wasnt meant to be pretty, but it is functional. If you want to style it - submit a pull request. 

There is a cloudbuild trigger set to listen to commits to the master branch. When something gets committed, it automatically deploys it to app engine. 