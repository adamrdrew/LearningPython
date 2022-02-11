# Modules
Libraries in Python are called modules. They are added to a project via the `import` keyword, along with some helpers like `from`.

The standard for the Python apps (AFAICT right now) is to keep all your libs in a directory with the app's name in the root of the app. So for an app called Labler we'd have something like this:

```bash
(Labler) [adam@ADAMPC Labler]$ tree
.
├── labler
│   ├── __init__.py
│   └── lib.py
├── Pipfile
├── Pipfile.lock
└── router.py

1 directory, 5 files
```

In the root of our app we have a `labler` directory and then under that we have our module files. Python requires you have a file named `__init__.py` in your module directory - it can be empty it just needs to be there.

Now we can import stuff but we have to resolve what we want to import. Python can have multiple members within a file in a module, unlike Ruby, so you have to resolve exactly what symbol you want to import rather than just a file name.

If this was Ruby and we had the setup above we'd do something like `import 'labler/lib'` and that would presumubly get us a class called `Lib`. In Python we can have multiple definitions in `lib.py` so it looks different.

Consider this `lib.py`:
```python
class RouteManager:
    def __init__(self) -> None:
        self.messages = Messages()

    def root(self, args):
        return self.messages.root()

class Messages:
    def __init__(self) -> None:
        pass

    def root(self):
        return "Hello from app"
```

To access `RouteManager` from our app we'd do this:

```python
from labler.lib import RouteManager
Manager = RouteManager()
```

So we're importing the class but we're doing it from the path to the file but instead of `labler/lib.py` it is written as `labler.lib`

If we wanted to access both of those modules we'd:

```python
from labler.lib import RouteManager
Manager = RouteManager()

from labler.lib import Messages
Mess = Messages()
```

And that's really it. You import symbols from files and resolve them via a dot notation representation of the project file structure.