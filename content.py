# Thomas Hepner
# Udacity Intro to Programming Nanodegree
# Stage 4 Project

from google.appengine.ext import ndb

DEFAULT_WALL = 'Public'

PAGES = [
	{"title"     : "Comments",
	 "href"      : "comments",
	 "nav_title":"Comments",
	}, 
	{"title"     : "Lesson 5: Choose Your Next Steps",
	 "href"      : "lesson-5",
	 "nav_title":"Lesson 5",
	},
	{"title"     : "Lesson 4: Allow Comments",
	 "href"      : "lesson-4",
	 "nav_title":"Lesson 4",
	},
	{"title"     : "Lesson 3: Create a Movie Website",
	 "href"      : "lesson-3",
	 "nav_title":"Lesson 3",
	},
	{"title"     : "Lesson 2: Build a Mab Libs Game",
	 "href"      : "lesson-2",
	 "nav_title":"Lesson 2",
	},
	{"title"     : "Lesson 1: Introduction to Making a Web Page",
	 "href"      : "lesson-1",
	 "nav_title":"Lesson 1",
	}]

def wall_key(wall_name=DEFAULT_WALL):
	"""Constructs a Datastore key for a Wall entity. We use wall_name as the key.
	"""
	return ndb.Key('name', name, 'description', description)

class Post(ndb.Model):
	"""A main model for representing an individual Guestbook entry."""
	name = ndb.StringProperty(indexed=False, required=True)
	description = ndb.StringProperty(indexed=False, required=True)
	date = ndb.DateTimeProperty(auto_now_add=True)


