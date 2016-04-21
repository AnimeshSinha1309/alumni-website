# AlumniWebsite
Website for St. Thomas school almuni association.

## Programming Languages and Dependencies

Our code is prinarily written in Python using the Django framework. Django constitutes the entire back end as well as
most of the front end of the code using Django templating language. Other static files like CSS, JavaScript are also
used. We are using plain CSS and JavaScript for our codes, but plan to support supersents like SASS and TypeScript soon
Library dependencies of the code are enlisted in the requirements.txt file, please use it to maintain your dependencies.

So the languages and libraries used are:
* Python 3.5
* Django 1.9.4
* HTML 5
* CSS 3
* JavaScript
* Pillow 3.2.0
* PIP 7.1.2

We are using **Microsoft Visual Studio 2015** as our development IDE and we recommend you to do the same (Because of 
some issues regarding file encodings, if you use other IDEs, please test your generated HTML for validity before 
contributing). The Community edition can be downloaded freely from the internet. Visual Studio would need PTVS 2.2,
Microsoft Plugin - Python tools for Visla Studio to be able to work with Python code.

## Compilation and Execution

To view this website, you need to have **Python 3** installed. This can be downloaded from the 
[Python Website](http://www.python.org). Intall pip along with it and add it to path
Then install Django framework using pip. See the installation intructions on 
[Django Installation Instructions](https://docs.djangoproject.com/en/1.9/intro/install/).
`pip install django` will install the framework.

Clone the code for the website from GitHub. Command line syntax for it is:

`git clone https://github.com/AnimeshSinha1309/AlumniWebsite.git`.

Now intall or update the dependencies for it from requirements.txt. Once the entire code is ready, build and run it
in Visual Studio using `Ctrl + F5`. If you are using some other IDE or editor, view the 
[Django Tutorial](https://docs.djangoproject.com/en/1.9/intro/tutorial01/) for instructions. The process it to navigate
to the project directory using command line and run the command `python manage.py runserver`.

And now you are done, the development version server will run the website on a random port of localhost (127.0.0.1).
You can see the server log on a command promt launched by the server.

## Contribution

Any and all help with the code is appriciated. You can contribute code directly by forking and senfing a pull request,
or comment or mark issues that we need to address. Again, any and all help is highly appriciated. However, before
committing large amounts of code, please add adquate tests for it and keep the code clean, well documented and semantically
clear so that we can understand and use it.
