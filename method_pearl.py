#method are functions that belongs to object
class student:
    College_name ="MITWPU"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
         print("welcome",self.name)
         
    def get_marks(self):
             print(self.marks)
         
s1 = student("Anjali",8.7) 
s2 = student("Bhavya",8)
s3 = student("param",8.2) 


s1.welcome() 
s2.get_marks()        



#static methods are methods that dont use self parameters (work at class level)



