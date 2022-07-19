# howfullismywall
How full is my wall? 

This was a python Flask app running on google cloud app engine, google's serverless hosting platform. It used a google datastore backend. 

The flask app makes a query of the database and returns the answer as a list to the jinja template which iterates over the list.  

There is a cloudbuild trigger set to listen to commits to the master branch. When something gets committed, it automatically deploys it to app engine. 