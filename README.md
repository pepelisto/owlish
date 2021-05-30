

First we need to create a virtual enviroment in our local machine, to do so open your Command Promt.
You will need to have python installed, you can check that typing:


    $ python --version


The output should be something like this:

    $ python 3.7.3




    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>

