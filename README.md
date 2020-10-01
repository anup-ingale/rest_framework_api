# rest_framework_api
#Ubuntu Machine setup :

Steps :

1.Install the Virtual Environment using : python3 -m venv name_of_env

2.Once done then go into it and activate using : source name_of_venv/bin/activate

3.After that using the command install all the requirements : `pip install -r requirements.txt`

4.Now , go to the project directory `python manage.py migrate`

5.The Above Commands will migrate the db with all default code .

6.Once Done run the migrations for the app as well to create the database tables .

7.By using `python manage.py makemigrations app_name` and then `python manage.py migrate app_name`

8.After that now we are good to run our project `python manage.py runserver`

9.once server get run `http://127.0.0.1:8000/api` go this url and you will the output of API.

10. Deployed url link for same output at pythonanywhere `http://anupingale.pythonanywhere.com/api/` 
