class RouteManager:
    def __init__(self) -> None:
        self.messages = Messages()

    def root(self, args):
        return self.messages.root()

    def greet(self, name):
        return self.messages.greet(name)

class Messages:
    def __init__(self) -> None:
        pass

    def root(self):
        return "Hello from app"

    def greet(self, name):
        return "Hi " + name + " good to meet you!"