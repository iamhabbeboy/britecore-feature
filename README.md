**Architecture**

Source File Explanations
Models: In the models package, there is the `model.py` file which is used to 
make SQL queries to the Database using SQLAlchemy. 

The `server.py` file is the main file which makes Flask to run. The initialization of 
the core features of Flask, SQLAlchemy and the addition of the routes and route functions are done in this file

`MODEL.PY`
________________

The `model.py` file has a couple of functions to help make Database queries using SQLAlchemy so much more easier

The `save` function which is used to save an instance of a feature request into the database

The `return_json` function which is used to convert a feature Request instance into a dict

The `find_by_name` function which is used to query the Database table using the Client's name

The `find_by_product` function which is used to query the Database table using the Product Areas

The `return_all` function which returns all the feature request in the Database

DEPLOYMENT

The web application is deployed on an Amazon Web Service (AWS) EC2 instance running Ubuntu 18.04.1 LTS (GNU/Linux 4.15.0-1021-aws x86_64). The app is deployed using Nginx as a reverse proxy and gunicorn as the WSGI server.
A service called `britcore.service` has been created which enables the service to start at boot. 