class student:
    name = "Bhavya"
    
S1 = student()
print(S1.name)




#___init function___(constructor function)
# all classes have a function called init function(),which is always executed 
#when the object is being initiated


class school:
    def __init__(self,fullname,roll):
        self.roll = roll
        self.name = fullname
        print("new student is being added...")
        
s1 = school("Anjali",12)
print(s1.name,s1.roll)



# attributes = data stored,variables