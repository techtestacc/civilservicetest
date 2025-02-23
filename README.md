Steps to install and run the application:
- Clone the repo and open the root folder in VS Code.
- You may need to create a virtual environment with Django installed. Instructions for VS Code here: https://code.visualstudio.com/docs/python/tutorial-django
- To run the application, write python manage.py runserver in the terminal.
- You may need to run python manage.py makemigrations and then python manage.py migrate to initialise the database.
I would use an Azure CI/CD YAML pipeline with one step to build, test and deploy the Django project to an AWS cluster. SQLite is file based so not suitable for a production environment.
I think it woule be better to migrate the DB to PostgreSQL or similar if it were to be deployed.
