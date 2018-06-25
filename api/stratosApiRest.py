import os
from flask import Flask, render_template, request


app = Flask(__name__)


#method that gets the URI parameters
def getParams():
	try:
			os.system("clear")
			params = request.form["params"]
	except:
			params = ""

	return (params)


#main web site
@app.route('/')
def startPage():
    return(render_template('start.html'))


#docs web site
@app.route('/docs')
def docsPage():
    return(render_template('docs.html'))


#parametes explanation web site
@app.route('/about')
def aboutPage():
    return(render_template('about.html'))


#exampels web site
@app.route('/contact')
def contactPage():
    return(render_template('contact.html'))


#search method
#@app.route('/examples')
#def examplesPage():
#    return(render_template('examples.html'))


#main method
if __name__ == '__main__':

	app.run(debug = True, host = '0.0.0.0')
