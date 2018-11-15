## Architecture**


Models: In the models package, there is the `model.py` file which is used to 
make SQL queries to the Database using SQLAlchemy. 

### Models:

`model.py` file is used to make queries using ORM SQLAlchemy package to handle the database.

### Server 

`server.py` file contains the Flask run codes; such as routes, etc.


## DEPLOYMENT

Amazon Web Service EC2 instance running Ubuntu is used to deployed the project.

Nginx is also used as a proxy and gunicorn as the WSGI server for the app.
 
