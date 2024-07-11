from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def about():
   return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
   return 'Page not found', 404

@app.errorhandler(500)
def internal_server_error(error):
   return 'Internal server error', 500
