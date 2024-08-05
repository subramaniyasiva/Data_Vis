# Data_Vis
1.To install Django by cmd prompt using the cmd : pip install Django
2 To .install pandas : pip install pandas and to get charts install matplotlib using the command pip install matplotlib.pyplot 
3.Create a new project using the command: django-admin startproject "projectname"
4.Create a new app inside the project by: cd projectname--> python manage.py startapp "appname"
5.In the django project directory find the file "settings.py" add your installed apps in the settings
and add templates and static directories.
6.create seperate folder in the project directoty for templates and static .
7.store your html files under template directory and css,images and js in static directory.
8.url.py is used for url routing
9.views.py is the file where the actual logic is written
10.return the function form view.py which renders in the website

ABOUT:
DATA VIS is a very simple django based web applications which allow the users to upload the CSV file which in return gives the first and last 5 rows 
,summary statistics and bar plot which generated using matplotlib.pyplot library.
