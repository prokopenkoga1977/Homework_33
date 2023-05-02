# HOMEWORK
# 1) Install venv 
# 2) Via pip install into dependents of your project : unittest 
# 3) Create 3 class : 
# 	class User
# 		method :
# 			say_hello must to return “Hello world”
# 	class Admin
# 		method :
# 			say_hello must to return “Hello world”
# 			mend_something must to return 01101101
# 	class Developer 
# 		method :
# 			say_hello must to return “Hello world”
# 			mend_something must to return 01101101
# 			write_code must to return [0,1,0,0,1,0]

# Check :
# 	- say_hello is string
# 	- mend_something is num
# 	- write_code must is list
# 	- write_code items is numbers 


# USE : Decomposing !!! 

# USE IT ALSO : https://docs.python.org/3/library/unittest.html#


from user import User
from admin import Admin
from developer import Developer

user = User("Prokop1977", 1234567 )
print(user.say_hello())

admin = Admin("Smit80", 7777777)
print(admin.say_hello())
print(admin.mend_something())

developer = Developer("Jordan90", 111777000, "Python")
print(developer.say_hello())
print(developer.mend_something())
print(developer.write_code())

