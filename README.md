# Oowlish Django Challenge

The challenge consists of creating a simple REST API that provides information about customers, design and create the proper database models, develop a single command to populate the database from a given csv file and get coordinates for the cities of each customer with Google maps API.

## Requirements

This instructions on how to get up-and-running and how to use are based on a windows 10 system so it might not work in other operating systems.

The project runs on Python 3.7.3 and uses the following packages

Django 3.2.3 <br>
googlemaps 4.4.5 <br>
python-decouple 3.4 <br>
pytz 2021.1 <br> 
requests 2.25.1 <br>
sqlparse 0.4.1 <br>
typing-extensions 3.10.0.0 <br>
urllib3 1.26.5 <br>

There is a requierments.txt file on the repository so following the instructions you will have them installed automatically.

## Get the app up-and-running

Assuming you have python and pip already installed in your local machine we are going to create a virtual environment to run the project, so first open the Command Prompt.

If you don't have virtual environment already installed then run 

     C:\Users\MASTER>pip install virtualenv

Now you need to clone the git repository to your local machine with the following command and git repository link (If you don't have Git installed go to https://git-scm.com/downloads it's very easy installation)

     C:\Users\MASTER>git clone https://github.com/pepelisto/owlish.git 

Now that we had a new directory atomatically created with the name of the project, in this case "owlish", we type in the command

     C:\Users\MASTER>cd owlish

Now that we are in the project directory we create a virtual environment  for it with the following command

     C:\Users\MASTER\owlish>virtualenv venv

So the virtual environment  its created, now we activate it with:

     C:\Users\MASTER\owlish>venv\Scripts\activate

You can see it worked because of the "(venv)" ate the beginning  of the line.
So now that the repository its in your local virtual environment, you need to install the requirements in order to properly run the program with the following command

     (venv) C:\Users\MASTER\owlish>pip install -r requirements.txt

Ok, so now, a very important step in the project directory we need to create a .env file (with no extension), windows does not allow you to create files with no extensions but you can do this in an IDE, in Pycharm right click on the project folder, new file and set its name to .env, this might be a bit tricky but very important because here we will set al the sensitive variables related to the project that we don't want nobody to have access to, like Secret Key, database access codes and in this case Google Geocoding API KEY. like shown in the image below

![image](https://user-images.githubusercontent.com/54082379/120118144-7a257700-c167-11eb-9bb1-a3cc39d1514f.png)

In there you can set the variables:

API_KEY = Here you use your own Google Geocode API KEY
SECRET_KEY = 'django-insecure-oz_z@if#ikfth92ruuhp^-(jasj*qn@3dt=9ruk1z9bk^hi-o('

Almost there, now only run the following command to set up a SQLite in our local environment to have our program up-and-running 

     (venv) C:\Users\MASTER\owlish>python manage.py migrate


## How to use it

Now that we are all set up, we are going to get all the customers from the csv file in the directory straight to our database, adding latitude and longitude from google maps API with a single command:

     (venv) C:\Users\MASTER\owlish>python manage.py add_customers

This might take a few minutes since they are many, if the user is created it will show 

     Customer succesfully created
    
Otherways, if the customer is in our database already, it will not create it again and will show the message    
    
     Customer was already created

So, now that our database its populated we can run the server with the command:

     (venv) C:\Users\MASTER\owlish>python manage.py runserver
    
we will get:


    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    May 30, 2021 - 16:47:07
    Django version 3.2.3, using settings 'owlish.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK

Now we can go to the url http://127.0.0.1:8000/customers_list/ to get the list with all the customers in our database(see image bellow)

![image](https://user-images.githubusercontent.com/54082379/120118155-8c9fb080-c167-11eb-9b3e-edab5cf8de28.png)

Clicking in any name we can have that customer details, or alternatively going to the url http://127.0.0.1:8000/customer_detail/Customer_ID_here/ and get

![image](https://user-images.githubusercontent.com/54082379/120118242-e6a07600-c167-11eb-8b61-26f848721d63.png)

## Running tests

To run the automated tests, simple type in the command:

     (venv) C:\Users\MASTER\owlish>python manage.py test

This will test automatically the URL's HTTP responses status codes and if the views that django returns are the correct views for the requested url's.







