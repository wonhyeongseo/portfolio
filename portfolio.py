##########################################
# Project 3: Movie Website
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
        <style type="text/css" media="screen">
            /*
            DEMO STYLE
            */
            @import "https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700";


            body {
                font-family: 'Poppins', sans-serif;
                background: #fafafa;
            }

            p {
                font-family: 'Poppins', sans-serif;
                font-size: 1.1em;
                font-weight: 300;
                line-height: 1.7em;
                color: #999;
            }

            a, a:hover, a:focus {
                color: inherit;
                text-decoration: none;
                transition: all 0.3s;
            }

            .navbar {
                padding: 15px 10px;
                background: #fff;
                border: none;
                border-radius: 0;
                margin-bottom: 40px;
                box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
            }

            .navbar-btn {
                box-shadow: none;
                outline: none !important;
                border: none;
            }

            .line {
                width: 100%;
                height: 1px;
                border-bottom: 1px dashed #ddd;
                margin: 40px 0;
            }

            /* ---------------------------------------------------
                SIDEBAR STYLE
            ----------------------------------------------------- */
            #sidebar {
                width: 250px;
                position: fixed;
                top: 0;
                left: 0;
                height: 100vh;
                z-index: 999;
                background: #7386D5;
                color: #fff;
                transition: all 0.3s;
            }

            #sidebar.active {
                margin-left: -250px;
            }

            #sidebar .sidebar-header {
                padding: 20px;
                background: #6d7fcc;
            }

            #sidebar ul.components {
                padding: 20px 0;
                border-bottom: 1px solid #47748b;
            }

            #sidebar ul input{
                padding: 10px;
            }

            #add {
                margin-left: 10px;
            }
            #sidebar ul button{
                margin: auto;
                width: 30%;
            }

            #sidebar ul li a {
                padding: 10px;
                font-size: 1.1em;
                display: block;
            }
            #sidebar ul li a:hover {
                color: #7386D5;
                background: #fff;
            }

            #sidebar ul li.active > a, a[aria-expanded="true"] {
                color: #fff;
                background: #6d7fcc;
            }


            a[data-toggle="collapse"] {
                position: relative;
            }

            a[aria-expanded="false"]::before, a[aria-expanded="true"]::before {
                content: '\e259';
                display: block;
                position: absolute;
                right: 20px;
                font-family: 'Glyphicons Halflings';
                font-size: 0.6em;
            }
            a[aria-expanded="true"]::before {
                content: '\e260';
            }


            ul ul a {
                font-size: 0.9em !important;
                padding-left: 30px !important;
                background: #6d7fcc;
            }

            a.article, a.article:hover {
                background: #6d7fcc !important;
                color: #fff !important;
            }


            /* ---------------------------------------------------
                CONTENT STYLE
            ----------------------------------------------------- */
            #content {
                width: calc(100% - 250px);
                padding: 40px;
                min-height: 100vh;
                transition: all 0.3s;
                position: absolute;
                top: 0;
                right: 0;
            }
            #content.active {
                width: 100%;
            }

            #trailer .modal-dialog {
                margin-top: 5%;
                width: 50%;
                height: 50%;
            }
            .hanging-close {
                position: absolute;
                top: -12px;
                right: -12px;
                z-index: 9001;
            }
            #trailer-video {
                width: 100%;
                height: 100%;
            }
            .movie-tile {
                margin-bottom:20px;
                padding-top: 20px;
                position: relative;
            }
            .movie-tile:hover {
                background-color: #EEE;
                cursor: pointer;
            }
            .movie-tile span {
                display:none;
            }
            .movie-tile:hover > span {
                display:block;
                z-index: 9;
                background-color: #fff2e6;
                border: 1px solid black;
                max-width: 384px;
                max-height: 216px;
                position: fixed;
                overflow: hidden;
            }
            .scale-media {
                padding-bottom: 56.25%;
                position: relative;
            }
            .scale-media iframe {
                border: none;
                height: 100%;
                position: absolute;
                width: 100%;
                left: 0;
                top: 0;
                background-color: white;
            }

            /* ---------------------------------------------------
                MEDIAQUERIES
            ----------------------------------------------------- */
            @media (max-width: 768px) {
                #sidebar {
                    margin-left: -250px;
                }
                #sidebar.active {
                    margin-left: 0;
                }
                #content {
                    width: 100%;
                }
                #content.active {
                    width: calc(100% - 250px);
                }
                #sidebarCollapse span {
                    display: none;
                }
            }
        </style>
        <!-- jQuery CDN -->
         <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
         <!-- Bootstrap Js CDN -->
         <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
         <!-- jQuery Nicescroll CDN -->
         <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.nicescroll/3.6.8-fix/jquery.nicescroll.min.js"></script>

         <script type="text/javascript">
            // Pause the video when the modal is closed
            $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
                // Remove the src so the player itself gets removed, as this is the only
                // reliable way to ensure the video stops playing in IE
                $("#trailer-video-container").empty();
            });
            // Start playing the video whenever the trailer modal is opened
            $(document).on('click', '.movie-tile', function (event) {
                var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
                var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0
                }));
            });
            function spanFollowMouse(){
                // Make .movie-tile span follow mouse when hovered.
                var tooltips = document.querySelectorAll('.movie-tile span');
            
                window.onmousemove = function (e) {
                    var x = (e.clientX + 0) + 'px',
                        y = (e.clientY + 0) + 'px';
                    for (var i = 0; i < tooltips.length; i++) {
                        tooltips[i].style.top = y;
                        tooltips[i].style.left = x;
                    }
                };
            }        
            //Animate in the movies when the page loads.    
             $(document).ready(function () {
                $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
                });
                //Make movie description hover over movie_tile
                spanFollowMouse();
                $("body").niceScroll({
                    cursorcolor:"#7386D5",
                    cursorwidth:"16px"
                });
                $("#sidebar").niceScroll({
                    cursorcolor:"#fff",
                    cursorwidth:"4px"
                })
                $('#sidebarCollapse').on('click', function () {
                    $('#sidebar, #content').toggleClass('active');
                    $('.collapse.in').toggleClass('in');
                    $('a[aria-expanded=true]').attr('aria-expanded', 'false');
                });
             });
         </script>
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
                        <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
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
                {project_tiles}
            </div>
        </div>
    </body>
</html>
'''

# A single movie entry html template
project_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
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
