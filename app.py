from flask import Flask, render_template  # flask is a module and Flask is a class
app = Flask(__name__)              # It is an object of that class

#print(__name__)  this will print name

@app.route('/')     # registering a route
def hello_world():           # It is colon, we have created a function
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug = True)
