class Admin:
    def __init__ (self, login, password):
        self.login = login
        self.password = password
    
    def say_hello(self):
        return "Hello world"
    
    def mend_something(self):
        return "mend_something"