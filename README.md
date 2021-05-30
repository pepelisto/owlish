

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


    
