import unittest

class Testing(unittest.TestCase):
    def check_is_str(self):
        self.assertEqual("Hello world", "Hello world")
        
    def check_is_num(self):
        self.assertEqual("01101101","01101101" )  
        
    def check_is_list(self):
        self.assertEqual([0,1,0,0,1,0],[0,1,0,0,1,])  
    
    def check_items_is_numbers(self):
        for item in [0,1,0,0,1,]:
            self.assertEqual(item,int) 
            
if __name__ =="__main__":
    unittest.main()