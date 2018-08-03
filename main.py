import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template("templates/start.html")
        self.response.write(template.render()) #the response

class Jumpin(webapp2.RequestHandler):
    def get(self): #for a get request
        template = env.get_template("templates/jumpin.html")
        self.response.write(template.render()) #the response

class Run(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class Contact(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/contact.html")
        self.response.write(template.render())

class Ignore(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/ignore.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/jumpin', Jumpin),
    ('/run', Run),
    ('/contact', Contact),
    ('/ignore', Ignore)

], debug=True)
