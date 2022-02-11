# Flask
Flask is Sinatra. Its just basically exactly Sinatra.

[Tutorial](https://pythonbasics.org/what-is-flask-python/)

```python
from flask import Flask
app = Flask( __name__ )

@app.route('/')
def index() -> None:
    return "Hello World!"

if __name__ == '__main__':
        app.run()
```

Flask defines routes with decorators on fucntions. So the function (`index()` above) is the route logic, and the route itself is defined with the `@app` decorator.

To run it in a pipenv app:
```bash
[adam@ADAMPC Labler]$ pipenv run python router.py
 * Serving Flask app 'router' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

