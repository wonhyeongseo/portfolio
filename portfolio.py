##########################################
# Project 3: Portfolio Website
# Date Started: 10/01/2017
# Date Completed: 10/02/2017
# Submitted by: Wonhyeong Seo
##########################################

######################################## Movie_shelf File ####################################################
# Description: This file creates creates an html file containing all of the desired movies from the
#              entertainment.py file.
########################################################################################################
'''A module that creates an html file containing all of the desired movies.'''
import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        <title>Won's Laboratory</title>

         <!-- Bootstrap CSS CDN -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <!-- Our Custom CSS -->
        <link rel="stylesheet" href="css\style.css" media="screen"/>
        <!-- jQuery CDN -->
         <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
         <!-- Bootstrap Js CDN -->
         <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
         <!-- jQuery Nicescroll CDN -->
         <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.nicescroll/3.6.8-fix/jquery.nicescroll.min.js"></script>

         <script type="text/javascript" src="js/script.js"></script>
    </head>
'''

# The main page layout and title bar
main_page_content = '''
    <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"
                             alt="Close button"/>
                    </a>
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                </div>
            </div>
        </div>

        <div class="wrapper">
            <!-- Sidebar Holder -->
            <nav id="sidebar">
                <div class="sidebar-header">
                    <h3>W <span class="glyphicon glyphicon-hd-video"></span> n's Lab</h3>
                </div>

                <ul class="list-unstyled components">
                    <li class="active">
                        <a href="#sortSubmenu" data-toggle="collapse" aria-expanded="false">Portfolio</a>
                        <ul class="collapse list-unstyled" id="sortSubmenu">
                            <li><a href="https://github.com/wonhyeongseo/movie_shelf">Movie Shelf</a></li>
                            <li><a href="#">This portfolio</a></li>
                        </ul>
                    </li>
                    <li>
                        <a href="#about">About</a>
                    </li>
                    <li>
                        <a href="#">Contact</a>
                    </li>
                </ul>
            </nav>

            <!-- Page Content Holder -->
            <div id="content">
                <nav class="navbar navbar-default">
                    <div class="container-fluid">

                        <div class="navbar-header">
                            <button type="button" id="sidebarCollapse" class="btn btn-info navbar-btn">
                                <i class="glyphicon glyphicon-align-left"></i>
                                <span>Toggle Sidebar</span>
                            </button>
                        </div>

                        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul class="nav navbar-nav navbar-right">
                                <li>
                                    <a href="#showInTiles"><span class="glyphicon glyphicon-th"></span></a>
                                </li>
                                <li>
                                    <a href="#showInList">
                                        <span class="glyphicon glyphicon-th-list"></span>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>
                <div class="row">
                {project_tiles}
                </div>
            </div>
        </div>
    </body>
</html>
'''

# A single movie entry html template
project_content = '''
                    <div class="col-md-6 col-lg-4 movie-tile text-center"
                         data-trailer-youtube-id="{trailer_youtube_id}"
                         data-toggle="modal"
                         data-target="#trailer">
                        <img src="{poster_image_url}">
                        <h2>{project_title}</h2>
                        <span>
                            <strong>Title: </strong>{project_title} <br>
                            <strong>Description: </strong>{project_desc} <br>
                            <strong>Genre: </strong>{project_genre} <br>
                            <strong>Open Datetime: </strong>{project_time} <br>
                            Click to see the intro!
                        </span>
                    </div>
'''

def create_projects_content(projects):
    # The HTML content for this section of the page
    content = ''
    for project in projects:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', project.youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', project.youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the project with its content filled in
        content += project_content.format(
            project_title=project.title,
            project_desc=project.description,
            project_genre=project.genre,
            project_time=project.open_datetime,
            poster_image_url=project.img_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_projects_page(projects):
    # Create or overwrite the output file
    output_file = open('portfolio.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        project_tiles=create_projects_content(projects))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
