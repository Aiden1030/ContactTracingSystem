#Aiden Sanghyeop Hyun
#260974945
 
class Student:
    ''' This type contains Mcgill ID, student name
and whethere or not the student is sick
 
Attributes: student_id, name, is_sick'''
    
    def __init__(self, student_id, name, is_sick = False ):
        '''(self,str,str,bool) -> self
 
initates the class and create an object with the given input
 
>>>a = Student('260123456','Jack')
 
>>>print(a.student_id)
 
'260123456'
 
>>>print(a.name)
 
'Jack'
 
>>>b = Student('160123456','Bobby')
 
raise ValueError('The student ID '+ student_id + ' is not a valid ID')
 
ValueError: The student ID 160123456 is not a valid ID
 
>>> b = Student('260915253','Billy')
 
>>> print(b.name)
 
Billy
 
>>> print(b.student_id)
 
260915253
 
'''
        #if student_id not valid
        
        #raise value error
    
        self.student_id = student_id
        
        if not Student.is_valid_id(student_id):
            
            raise ValueError('The student ID '+ student_id + ' is not a valid ID')
        
            
        
        self.name = name
        
        self.is_sick = is_sick
    
    def __str__(self):
        '''(self) -> None
 
prints student object in "self.name (student_id)" format
 
>>> b = Student('260915253','Billy')
 
>>> print(b)
 
Billy (260915253)
 
>>> print(a)
 
Jane (260765321)
 
>>> c = Student('260987654','Bill')
 
>>> print(c)
 
Bill (260987654)
'''
        #format "name (student_id)"
        
        return self.name + ' '+ '('+self.student_id+')'
    
    
    def __repr__(self):
        ''' (self) -> Student
 
returns a student object to 'self' after building a  "self.name
(student_id)" format
 
larry = Student('260123456','Larry')
 
repr(larry)
'Larry (260123456)'
 
larry
Larry (260123456)
 
jhon = Student('260198178','Jhon')
 
repr(jhon)
'Jhon (260198178)'
 
jhon
Jhon (260198178)
 
ben = Student('260796869','Ben')
 
repr(ben)
'Ben (260796869)'
 
ben
Ben (260796869)
'''
        #format "name (student_id)" return self
        
        self = self.name + ' '+ '('+self.student_id+')'
        
        return self
    
    @staticmethod
    def is_valid_id(num):
        ''' (str)-> bool
 
Checks whether the student_id is valid.
An ID string is valid if it is a has 9 digits where the
first three digits are 260.
 
>>> Student.is_valid_id('260745567')
True
 
>>> Student.is_valid_id('26074')
False
 
>>> Student.is_valid_id('26074e5567')
False
 
>>> Student.is_valid_id('210745567')
False
 
'''
 
 
        
        
        
        num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        
        #checks if the student id starts with 260 and has
        
        #9 numbers and only numbers
        
        if num[0:3] == '260' and len(num) == 9:
            
            for i in num:
                
                if i not in num_list:
                    
                    return False
            return True
                    
        
        return False
    
    @classmethod
    def from_JSON(cls,dict_str):
        '''(cls,str)-> Student
 
constructs and return a Student object
from the input parameter string
that has the data of the student in JSON
 
>>> larry = Student.from_JSON('{"id": "260745567", "name": "Larry"}')
>>> str(larry)
'Larry (260745567)'
 
>>> jhon = Student.from_JSON('{"id": "260151433", "name": "Jhon"}')
>>> str(Jhon)
'Jhon (260151433)'
 
>>> stewart = Student.from_JSON('{"id": "260123456", "name": "Stewart"}')
>>> str(stewart)
'Stewart (260123456)'
 
 
'''
        
        
        dict_format_list = [',','id','"','name',':','}','{',': ', ', ']
        
        #split keys and values in the dict with " characters
        
        split_once = dict_str.split('"')
        
        # scans student id and name
        
        for i in split_once:
            
            if i in dict_format_list:
                
                continue
            
            else:
                
                if Student.is_valid_id(i):
                    
                    student_id = i
                    
                
                else:
                    
                    name = i
        
        # creates a student id and return
        
        return Student(student_id,name)
    
 
                
                
            
            
            
        
        
        
                
            
    
    
        
        
