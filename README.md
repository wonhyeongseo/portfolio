#Portfolio README
Source code for a Portfolio website.

This code may be downloaded from: https://github.com/wonhyeongseo/portfolio

How to use: 
1. Write your favorite movies on projects.py like the given format.
2. Run projects.py by double clicking it. 

File docstrings:
- project_model.py is a constructor module for various media- although right now there is only a project constructor.

- portfolio.py creates an html file containing all of the desired projects from projects.py. I wish to add a local database (sqlite?) for the user to add, edit, and delete movies from their own machine. Right now I don't know how to set up a local webserver to process the GET and POST of the forms.

- projects.py is where projects are stored and sent to portfolio.py for the creation of the webpage.   This is where want I to create the database. But I'm not sure if it's the correct way.

Sources: design is derived from https://bootstrapious.com/p/bootstrap-sidebar
         Python source code is derived from Udacity's Full Stack Web Developer Program's python lessons.
"# portfolio" 