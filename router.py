from flask import Flask
app = Flask( __name__ )

from labler.lib import RouteManager
Manager = RouteManager()

from labler.lib import Messages
Mess = Messages()

@app.route('/')
def root():
    return Manager.root('/')

@app.route('/greet/<name>')
def greet(name):
    return Manager.greet(name)

if __name__ == '__main__':
        app.run()
