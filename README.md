# rest_framework_api
#Ubuntu Machine setup :

Steps :

Install the Virtual Environment using : python3 -m venv name_of_env

Once done then go into it and activate using : source name_of_venv/bin/activate

After that using the command install all the requirements : `pip install -r requirements.txt`

Now , go to the project directory `python manage.py migrate`

The Above Commands will migrate the db with all default code .

Once Done run the migrations for the app as well to create the database tables .

By using `python manage.py makemigrations app_name` and then `python manage.py migrate app_name`

After that now we are good to run our project `python manage.py runserver`

once server get run `http://127.0.0.1:8000/api` go this url and you will the output of API.
