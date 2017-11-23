##########################################
# Project 0: Portfolio Website
# Date Started: 11/01/2017
# Date Completed: 11/23/2017
# Submitted by: Wonhyeong Seo
##########################################

######################################## Project_model File ####################################################
# Description: This file creates the class Project to allow for instances of this class to be used in the
#              Projects.py file. This definition of the class Project was obtained through the Movie Shelf
#              project.
########################################################################################################
"""A constructor module for various projects"""
import webbrowser


class Project:
    '''A constructor class for various projects'''
    def __init__(self, title, description, open_datetime, genre, youtube_url, img_url):
        self.title = title
        self.description = description
        self.open_datetime = open_datetime
        self.genre = genre
        self.youtube_url = youtube_url
        self.img_url = img_url

    def show_trailer(self):
        webbrowser.open(self.youtube_url, new=2)