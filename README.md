
### Get the app up and running

Assuming you have python, pip already installed in your local machine we are going to create a virtual enviornment to run the project, so first open the Command Prompt.

If you don't have virtual enviorement already installed then run 

    $ C:\Users\MASTER>pip install virtualenv
    
If you don't have Git installed go to https://git-scm.com/downloads it's very easy intallation    

Now you need to clone the git repository to your local machine with the following command and git repository link

    $C:\Users\MASTER>git clone https://github.com/pepelisto/owlish.git 

Now that we had a new directory atomatically created with the name of the project, in this case "owlish", we type in the command

    $ C:\Users\MASTER>cd owlish

Now that we are in the project directory we create a virtual enviornment for it with the following command

    $ C:\Users\MASTER\owlish>virtualenv venv

So the virtual enviorment its created, now we activate it with:

    $ C:\Users\MASTER\owlish>venv\Scripts\activate

You can see it worked because of the "(venv)" ate the begining of the line.
So now that the repository its in your local virtual enviornment, you need to install the requirements in order to properly run the program with the following command

    $(venv) C:\Users\MASTER\owlish>pip install -r requirements.txt

Ok, so now, a very important step in the project directory we need to create a .env file (with no extension) windows does not allow you to create files with no extensions but you can do this in an IDE, in Pycharm right click on the project folder, new file and set its name to .env, this might be a bit tricky but very important because here we will set al the sensitive variables related to the project taht we dont want no body to have acces to, like Secret Key, database access codes and in this case Google Geocoding API KEY. like shown in the image bellow

         ![image](https://user-images.githubusercontent.com/54082379/120117405-6a0b9880-c163-11eb-88eb-864602d647a2.png)

In there you can set the variables:
API_KEY = Here you use your own Google Geocode API KEY
SECRET_KEY = 'django-insecure-oz_z@if#ikfth92ruuhp^-(jasj*qn@3dt=9ruk1z9bk^hi-o('

Almost there, now only run the following commmand to set up a SQLite in our local environment to have our program up-and-running in our local environment

    $(venv) C:\Users\MASTER\owlish>python manage.py migrate






    
