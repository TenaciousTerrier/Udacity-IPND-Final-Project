# Thomas Hepner
# Udacity Intro to Programming Nanodegree
# Stage 4 Project

import os
import webapp2
import jinja2

from content import PAGES, wall_key, Post, DEFAULT_WALL

template_dir = os.path.join(os.path.dirname(__file__), 'html_templates')
jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, pages=PAGES, **kw))

class MainPage(Handler):
	def get(self):
		self.render("/main_page.html", page_name="home")

class Lesson1Handler(Handler):
	def get(self, error=False):
		self.render('lesson-1.html', page_name="lesson-1")

class Lesson2Handler(Handler):
	def get(self, error=False):
		self.render('lesson-2.html', page_name="lesson-2")

class Lesson3Handler(Handler):
	def get(self, error=False):
		self.render('lesson-3.html', page_name="lesson-3")

class Lesson4Handler(Handler):
	def get(self, error=False):
		self.render('lesson-4.html', page_name="lesson-4")

class Lesson5Handler(Handler):
	def get(self, error=False):
		self.render('lesson-5.html', page_name="lesson-5")

class CommentHandler(Handler):
	def get(self, **kwargs):
 		comment_query = Post.query().order(-Post.date)
 		comment_library = comment_query.fetch()
 		self.render('comments.html', comment_library = comment_library)

 	def post(self):
		post = Post()
		post.name = self.request.get('name')
		post.description = self.request.get('description')
		query_params = {"name": post.name, "description": post.description}
		is_valid, errors = validate_comment(post)	
		if is_valid:
			post.put()
			self.redirect('/comments')
		else:
			for k, v in errors.items():
				query_params[k] = v
				self.render('comments.html', **query_params)

def validate_comment(comment):
	valid = True
	errors = {}
	if len(comment.name) < 2:
		errors['name_error'] = "Please enter a name to display (at least 2 characters)."
		valid = False
	if len(comment.description) < 10:
		errors['description_error'] = "Please leave a comment here (at least 10 characters)"
		valid = False
	return valid, errors

	