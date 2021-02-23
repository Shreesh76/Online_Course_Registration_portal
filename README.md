# Course-Management-system

Steps

1) Create a virtual env
2) Run : pip install -r requirement.txt
3) Move to manage.py folder

Create Database :

4) Open MonogoDB Compass
5) Create a database name cms

6) Open phpmyadmin or sqlclient
7) Create a database name cms

8) Open settings.py in cms folder and set USER and PASSWORD of the databases
9) Now, 3) step

10) Run,
    python manage.py makemigrations validate
    python manage.py migrate --database=validatedb
    
    python manage.py makemigrations contact
    python manage.py migrate --database=contactdb
    
11) python manage.py runserver
