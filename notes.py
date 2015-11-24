# Thomas Hepner
# Udacity Intro to Programming Nanodegree
# Stage 4 Project

import webapp2
from handlers import *

application = webapp2.WSGIApplication([
	('/*', MainPage),
	('/lesson-1', Lesson1Handler),
	('/lesson-2', Lesson2Handler),
	('/lesson-3', Lesson3Handler),
	('/lesson-4', Lesson4Handler),
	('/lesson-5', Lesson5Handler),
	('/comments', CommentHandler),
], debug=True)
