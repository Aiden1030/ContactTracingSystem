#Aiden Sanghyeop Hyun
#260974945
 
         
 
class ContactTracker:
    '''(list, dict) -> None
It takes a list of student objects and a dictionary of cases with contacts
and initiates the input
 
Attributes: students, cases_with_contacts'''
    
    import copy
    
    
    def __init__(self, students, cases_with_contacts = {} ):
        ''' (list,dict)-> none
 
takes a list of student objects and a dict of sick
students and their contact list
 
import contactTracingSystem as cts
 
a = cts.load_file('cases.csv')
 
b = cts.load_file('all_students.json')
 
first_student_list = cts.JSON_to_students(b)
        
first_student_dictionary = cts.csv_to_dictionary(a)
              
print(ContactTracker(first_student_list, first_student_dictionary))
 
<__main__.ContactTracker object at 0x7fb6f80af350>
 
import contactTracingSystem as cts
 
a = cts.load_file('cases1.csv')
 
b = cts.load_file('all_students1.json')
 
first_student_list = cts.JSON_to_students(b)
        
first_student_dictionary = cts.csv_to_dictionary(a)
              
print(ContactTracker(first_student_list, first_student_dictionary))
<__main__.ContactTracker object at 0x7fb7080c7710>
 
import contactTracingSystem as cts
 
a = cts.load_file('cases2.csv')
 
b = cts.load_file('all_students2.json')
 
first_student_list = cts.JSON_to_students(b)
        
first_student_dictionary = cts.csv_to_dictionary(a)
              
print(ContactTracker(first_student_list, first_student_dictionary))
<__main__.ContactTracker object at 0x7fb6f833c290>
 
 
 
'''
        
        import copy
        
        # if students attribute is not included
        
        #leave it as an empty list
        
        if type(students) == dict():
            
            cases_with_contacts = copy.deepcopy(students)
            
            students = []
        
        
        
        
        self.students = students
        
        contacts_copy = copy.deepcopy(cases_with_contacts)
        
        self.cases_with_contacts = contacts_copy
        
        
        #checks if the student list validity
        
        list_of_student = []
        
        student_id_list = []
        
        #goes through the dictionary
        
        #saves the keys and values
        
        for key in self.cases_with_contacts:
            
            list_of_student += cases_with_contacts[key] + [key]
            
        #goes through student list and records their ids
    
        for i in self.students:
            
            student_id_list += [i.student_id]
        
            
        #goes through sick student and if they are in
            
        # the student list raise value error
            
        for id_num in list_of_student:
            
            if id_num not in student_id_list:
                
                raise ValueError("A student with id "+id_num.student_id+" either doesn't exist or is not reported as sick.")
    
    
    def get_contacts_by_student_id(self, student_id):
        '''(str)-> list
 
returns a list of students who the sick student had contact
with
 
>>> c.get_contacts_by_student_id('260064375')
[Francesca (260032440), Ayla (260005925)]
 
 
>>> c.get_contacts_by_student_id('260094997')
[Reed (260010997), Zara (260026754), Avah (260072488), Maddison (260031971)]
 
>>> c.get_contacts_by_student_id('260014616')
[Rory (260092283), Reed (260010997), Zara (260026754), Brittany (260092902), Hadley (260064375)]
 
'''
        import copy
        
        
        result = []
        
        # if the given student id is not one of the sick student's
        
        #raise valueError with a message
        
        try:
            
            list_of_student_in_contact = self.cases_with_contacts[student_id]
            
        except KeyError:
            
            raise ValueError("A student with id "+student_id+ " either doesn't exist or is not reported as sick.")
        
        #Convert student ids into student objects
        
        for student_object in self.students:
            
            if student_object.student_id in list_of_student_in_contact:
                
                result += [student_object]
                
            
        return result
    
    def get_all_contacts(self):
        
        import copy
        
        '''()-> dict
 
change dict with a list of strings as value into a list of
student objects
 
>>> c.get_all_contacts()
{'260064375': [Ayla (260005925), Francesca (260032440)],
'260094997': [Avah (260072488), Zara (260026754),
Reed (260010997), Maddison (260031971)], '260092902':
[Reed (260010997), Anahi (260068501), Ayla (260005925),
...]}
 
import contactTracingSystem as cts
 
        a = cts.load_file('cases.csv')
 
        b = cts.load_file('all_students.json')
 
        first_student_list = cts.JSON_to_students(b)
                
        first_student_dictionary = cts.csv_to_dictionary(a)
              
c = ContactTracker(first_student_list, first_student_dictionary)
 
>>> c.get_all_contacts()
 
{'260808934': [Paul (260840155), Mark (260248711), Carol (260996175),
Leanne (260476020), Will (260561504)], '260996175': [Mark (260248711),
Leanne (260476020)], '260675874': [Paul (260840155)], '260476020':
[Sarai (260758421)], '260386543': [Carol (260996175), Mark (260248711),
Leanne (260476020), Will (260561504)], '260248711': [Philip (260212160),
Zach (260970944)], '260840155': [Zach (260970944)], '260561504':
[Leanne (260476020), Mark (260248711)], '260970944': [Philip (260212160)]}
 
>>> import contactTracingSystem as cts
 
        a = cts.load_file('cases1.csv')
 
        b = cts.load_file('all_students1.json')
 
        first_student_list = cts.JSON_to_students(b)
                
        first_student_dictionary = cts.csv_to_dictionary(a)
              
c = ContactTracker(first_student_list, first_student_dictionary)
 
>>> c.get_all_contacts()
{'260018288': [Bob (260808934), Carol (260996175),
Darryl (260084903), Ettienne (260026473), Forbert
(260072990), Gordie (260039118)], '260041845':
[Bob (260808934), Carol (260996175), Ettienne
(260026473), Forbert (260072990)], '260092533': [Darryl (260084903),
Ettienne (260026473), Forbert (260072990), Job (260013314),
Kirk (260041812), Gordie (260039118)], '260013314': [Lammle (260065208)],
'260072990': [Molly (260061737), Job (260013314)], '260041812':
[Job (260013314)], '260084903': [Lammle (260065208)],
'260808934': [Lammle (260065208)], '260026473':
[Lammle (260065208)], '260996175': [Lammle (260065208)],
'260061737': [Job (260013314), Kirk (260041812)],
'260039118': [Kirk (260041812)]}
 
 
 
'''
        
        
        
        student_dict = copy.deepcopy(self.cases_with_contacts)
        result_dict = {}
        value_list = []
        
        #getting all the sicks students in a loop
        for key in student_dict:
            
            #sick student's list
            
            list_of_student_with_contacts = student_dict[key]
            
            #put through potential student's id.s
            
            for id_string in list_of_student_with_contacts:
                
                # Convert each of them to student objects
                
                for student_object in self.students:
                    
                    if student_object.student_id == id_string:
                        
                        value_list += [student_object]
            
            # save the list of student ids in a dictionary
            
            result_dict[key] = copy.deepcopy(value_list)
             
            #empty this list and continue the loop until all sick students
            
            #are put through
            
            value_list = []
        
        return result_dict
    
    def patient_zeros(self):
        '''()-> list
 
takes no parameters and returns a list of sick students (Student objects) who are the
possible patient zero(s).
 
>>> print(patient_zeros())
[Bob (260808934), Farley (260675874), Larry (260386543)]
 
>>> print(patient_zeros())
 [Lammle (260065208)]
 
>>> print(patient_zeros())
[Job (260013314), Kirk (260041812)]
 
'''
        
        import copy
 
        result = []
 
        list_of_sick_student = []
 
        student_dict = copy.deepcopy(self.cases_with_contacts)
 
         #sick patient in the list
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
        
        
        # remove people who are not patient zero
        
        for sick_patient in student_dict:
            
            for student in student_dict[sick_patient]:
                
                if student in list_of_sick_student:
                    
                    list_of_sick_student.remove(student)
 
        #convert into student objects
                    
        for student_object in self.students:
            
            if student_object.student_id in list_of_sick_student:
                
                result += [student_object]
 
        return result
    
    def potential_sick_students(self):
        
        '''()-> list
 
returns a list of students who is in the list but not sick
 
>>> print(potential_sick_students())
 [Job (260013314), Kirk (260041812)]
 
>>> print(potential_sick_students())
[Philip (260212160), Sarai (260758421)]
 
>>> print(potential_sick_students())
[Bob (260808934), Carol (260996175), Darryl (260084903),
Ettienne (260026473), Forbert (260072990), Gordie (260039118)]
 
'''
        
        import copy
        
        student_dict = copy.deepcopy(self.cases_with_contacts)
        
        list_of_students_with_contact = []
        
        list_of_sick_student = []
        
        result_string = []
        
        result = []
        
        # put students with positive test result in a list
        
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
            
        #put students with contact in a list
            
        for sick_student in list_of_sick_student:
            
            sick_student_contact = student_dict[sick_student]
            
            for potential_student in sick_student_contact:
                
                if potential_student not in list_of_students_with_contact:
                    
                    list_of_students_with_contact += [potential_student]
            
            sick_student_contact = []
        
        #erase sick students from the list
            
        for sick_student in list_of_sick_student:
            
            if sick_student in list_of_students_with_contact:
                
                list_of_students_with_contact.remove(sick_student)
        
        #convert into student objects
                
        for student_object in self.students:
            
            if student_object.student_id in list_of_students_with_contact:
                
                result += [student_object]
                
        
        return result
    
    
    
    def sick_from_another_student(self):
        
        '''()-> list
 
returns a list of student objects who got covid from
another person in the list
 
>>> print(sick_from_another_student())
 
 [Bob (260808934), Carol (260996175), Darryl (260084903),
 Ettienne (260026473), Forbert (260072990), Gordie (260039118)]
 
>>> print(sick_from_another_student())
 
 [Lammle (260065208)]
 
>>> print(sick_from_another_student())
 
 [Job (260013314), Kirk (260041812)]
 
'''
    
        import copy
 
        result = []
        
        final_result = []
 
        list_of_sick_student = []
        
        sick_student_contact = []
 
        student_dict = copy.deepcopy(self.cases_with_contacts)
         
         #sick patient in the list
        
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
            
        #sick student's contact list in a list
            
        for sick_student in list_of_sick_student:
            
            sick_student_contact += student_dict[sick_student]
        
        #if sick_student is in the contact list
            
        #save that sick_student in a list
            
        for sick_student in list_of_sick_student:
            
            if sick_student in sick_student_contact:
                
                result += [sick_student]
                
        
        #convert the list into a list of student objects
                
        for student_object in self.students:
            
            if student_object.student_id in result:
                
                final_result += [student_object]
        
        return final_result
            
    
    def most_viral_students(self):
        '''()-> list
 
return a list of student.s that has the longest contact list
 
>>> print(most_viral_students())
[Bob (260808934)]
 
>>> print(most_viral_students())
 [Job (260013314), Kirk (260041812)]
 
>>> print(most_viral_students())
[Bob (260808934), Carol (260996175), Darryl (260084903),
Ettienne (260026473), Forbert (260072990), Gordie (260039118)]
 
'''
        
        
        
        import copy
 
        result = []
        
        final_result = []
 
        list_of_sick_student = []
        
        sick_student_contact = []
        
        contact_len = 0
 
        student_dict = copy.deepcopy(self.cases_with_contacts)
        
        #sick patient in the list
        
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
            
        #Checks who has the longest contact list
            
        for sick_student in list_of_sick_student:
            
            result += [sick_student]
            
            
            if contact_len > len(student_dict[sick_student]):
                
                result.remove(sick_student)
                
            elif contact_len < len(student_dict[sick_student]):
                
                contact_len = len(student_dict[sick_student])
            
            
                
        
        #convert into student objects
                
        for student_object in self.students:
            
            if student_object.student_id in result:
                
                final_result += [student_object]
        
        return final_result
    
         
        
    def most_contacted_student(self):
        '''  ()-> list
 
returns a list of student.s that contacted with
sick students the most and not sick.
 
>>> print(contact_tracker.most_contacted_student())
 
 [Job (260013314), Kirk (260041812)]
 
 >>> print(contact_tracker.most_contacted_student())
 
 [Bob (260808934), Carol (260996175), Darryl (260084903),
Ettienne (260026473), Forbert (260072990), Gordie (260039118)]
 
[Bob (260808934)]'''
        
        import copy
 
        result = []
        
        final_result = []
        
        final_final_result = []
 
        list_of_sick_student = []
        
        sick_student_contact = []
        
        contact_len = 0
 
        student_dict = copy.deepcopy(self.cases_with_contacts)
 
        #sick patient in the list
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
            
        #sick patient's contact list into a list
        
        for sick_student in list_of_sick_student:
            
            result += student_dict[sick_student]
        
        result_copy = copy.deepcopy(result)
        
        #if a student that was in the contact list is sick
        
        # remove them from the list
        
        for potential_student in result:
            
            if potential_student in list_of_sick_student:
                
                result_copy.remove(potential_student)
        
        previous_count = 0
        
        #compare who is the most contacted  student
        
        for potential_student in result_copy:
            
            current_count = result.count(potential_student)
            
            #if a student has longer list than the one before
            
            if previous_count < current_count:
                
                previous_count = current_count
                    
                final_result = []
                    
                final_result += [potential_student]
            
            # if a student contact list has the same length
            
            #as the one before
            
            elif previous_count == current_count:
                
                if potential_student not in final_result:
                    
                    final_result += potential_student
        
        
        #convert into student objects
                    
        for student_object in self.students:
            
            if student_object.student_id in final_result:
                
                final_final_result += [student_object]
        
        return final_final_result
            
    def ultra_spreaders(self):
        
        '''  ()-> list
 
returns a list of spreader students who has a list of
contact with no sick students.
 
>>> print(contact_tracker.ultra_spreaders())
 [Job (260013314), Kirk (260041812)]
 
 
 >>> print(contact_tracker.ultra_spreaders())
 [Bob (260808934), Carol (260996175), Darryl (260084903),
Ettienne (260026473), Forbert (260072990), Gordie (260039118)]
 
 
>>> print(contact_tracker.ultra_spreaders())
[Bob (260808934)]'''
        
        
        
        import copy
 
        result = []
        
        final_result = []
        
        final_final_result = []
 
        list_of_sick_student = []
        
        sick_student_contact = []
        
        contact_len = 0
        
        record = 0
 
        student_dict = copy.deepcopy(self.cases_with_contacts)
 
        #sick patient in the list
        
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
            
        #checks if the sick student's contact list
            
        #has a sick student
        
        for sick_student in list_of_sick_student:
            
            contact_list = student_dict[sick_student]
            
            for potential_student in contact_list:
                
                if potential_student in list_of_sick_student:
                    
                    record = 1
                
            if record == 0:
                
                result += [sick_student]
            
            record = 0
            
        #convert into student objects
            
        for student_object in self.students:
            
            if student_object.student_id in result:
                
                final_result += [student_object]
        
        return final_result
        
        
        
                
                
            
    def non_spreaders(self):
        
        ''' ()-> list
 
returns a list of sick non spreaders who only had
contact with sick students
 
 
>>> print(contact_tracker.non_spreaders())
 [Job (260013314), Kirk (260041812)]
 
 
 >>> print(contact_tracker.non_spreaders())
 [Bob (260808934), Carol (260996175), Darryl (260084903),
Ettienne (260026473), Forbert (260072990), Gordie (260039118)]
 
 
>>> print(contact_tracker.non_spreaders())
[Bob (260808934)]'''
        
        import copy 
 
        result = []
        
        final_result = []
        
        list_of_sick_student = []
        
        sick_student_contact = []
        
        record = 0
        
        student_dict = copy.deepcopy(self.cases_with_contacts)
 
        #sick patient in the list
        for sick_patient in student_dict:
            
            list_of_sick_student += [sick_patient]
            
        list_of_sick_student_copy = copy.deepcopy(list_of_sick_student)
            
        
        # finds sick students that are not in other parts of dict
        
        for sick_student in list_of_sick_student:
            
            for potential_student in student_dict[sick_student]:
                
                if potential_student not in list_of_sick_student_copy:
                    
                    
                    record = 1
                
            if record == 0 :
                
                result += [sick_student]
            
            record = 0
        
       #convert into student objects
            
        for student_object in self.students:
            
            if student_object.student_id in result:
                
                final_result += [student_object]
        
        return final_result
        
                   
                            
           
                    
            
 
      
