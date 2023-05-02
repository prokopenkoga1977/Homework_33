class Developer:
    def __init__ (self, login, password, skills):
        self.login = login
        self.password = password
        self.skills = skills
        
    def say_hello (self):
        return "Hello world"
    
    def mend_something (self):
        return "01101101"
    
    def write_code (self):
        return [0,1,0,0,1,0]