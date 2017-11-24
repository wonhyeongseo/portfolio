##########################################
# Project 1: Portfolio Website
# Date Started: 11/01/2017
# Date Completed: 11/23/2017
# Submitted by: Wonhyeong Seo
##########################################

######################################## Projects file ####################################################
# Description: This file stores project contents by making instances of the class Project to allow for these
#              to be used in the portfolio.py file. The contents are obtained via Google searches (for now).
########################################################################################################
'''Where projects are stored and sent to portfolio.py for the creation of the webpage.'''
import project_model
import portfolio

movie_shelf = project_model.Project(
    title="Movie Shelf",
    description="It's kind of like a bookshelf, but for movies. :) [yay!]",
    open_datetime="November 2nd 12017",
    genre="Website",
    youtube_url="https://www.youtube.com/watch?v=FM7MFYoylVs",
    img_url="http://all-that-is-interesting.com/wordpress/wp-content/uploads/2012/08/great-libraries-bibliotheque2.jpg"
)

won_lab = project_model.Project(
    title="Won's laboratory",
    description="Just making something very... Terrestrial :D",
    open_datetime="November 23rd 12017",
    genre="Website",
    youtube_url="https://www.youtube.com/watch?v=bbNqtsN-lV0",
    img_url="https://d85wutc1n854v.cloudfront.net/live/products/600x375/WB074R2BS.png?v=1.0"
)

portfolio.open_projects_page([
    movie_shelf,
    won_lab,
])
