class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

# Object A is the calling environment
class CallingEnvironment:
    def __init__(self, greeter):
        self.greeter = greeter

    def execute_greeting(self):
        # Sending a message to object B (Greeter) to invoke the 'greet' method
        message = self.greeter.greet()
        print(message)

# Creating instances (objects) of the classes
greeter = Greeter("World")
caller = CallingEnvironment(greeter)

# Object A (caller) sends a message to object B (greeter)
caller.execute_greeting()