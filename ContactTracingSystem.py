#Aiden Sanghyeop Hyun
#260974945
 
 
 
def load_file(file_name):
    '''(str)-> str
 
finds the file with the file name and returns
the content in the file as a string
 
>>>a = load_file('README.txt')
 
>>>print(a)
 
'comp202 assignment 4'
 
>>> b = load_file('cases.csv')
 
>>> print(b)
 
260808934, 260840155, 260248711, 260996175,
260476020, 260561504
260996175, 260248711, 260476020
260675874, 260840155
...
 
>>> c = load_file('all_students.json')
 
>>>print(c)
 
[{"id": "260808934", "name": "Bob"},
{"id": "260840155", "name": "Paul"},
{"id": "260248711", "name": "Mark"},
{"id": "260996175", "name": "Carol"},
...]
 
''
 
'''
    #open file
    
    f = open(file_name,'r')
    
    # when error raised for read function
    
    # close the file and return none
    
    try:
        
        file_content = f.read()
        
    except :
        
        f.close()
        
        return None
    
    return file_content
 
 
 
 
 
 
    
def JSON_to_students(data):
    
    '''(str)   ->  list
 
It takes a string in json format and return
a list of student objects
 
 
>>> data = load_file("all_students.json")
 
>>> print(JSON_to_students(data))
 
[Bob (260808934), Paul (260840155), Mark (260248711),
Carol (260996175), Leanne (260476020),
Will (260561504), Farley (260675874), Sarai (260758421),
Larry (260386543),Philip (260212160), Zach (260970944)
 
>>>c = load_file('all_students1.json')
 
>>>print(JSON_to_students(c))
 
[Alice (260018288), Bob (260808934), Carol (260996175),
Darryl (260084903), Ettienne (260026473), Forbert (260072990),
Gordie (260039118), Hanes (260041845), Illersley (260092533),
Job (260013314), Kirk (260041812), Lammle (260065208),
Molly (260061737)]
 
>>>c = load_file('all_students2.json')
 
>>>print(JSON_to_students(c))
 
[Angelina (260095234), Francesca (260032440), Rory (260092283),
Piper (260055764), Sanaa (260025405), Danna (260068680),
Ayla (260005925), Leonardo (260031356), Reed (260010997),
Jackson (260014616), Zara (260026754), Avah (260072488),
Anahi (260068501), Hailee (260012075), Naima (260071927),
Weston (260094691), Maddison (260031971), Brittany (260092902),
Jasmine (260094997), Hadley (260064375)]
 
 
]'''
    
    import student
    
    list_of_students_JSON = []
    
    record = 0
    
    json_string = ''
    
    student_list = []
    
    #creates a list that contains the student id.s
    
    for i in data:
        
        if i == '{' and record == 0:
            
            record = 1
        
        if record == 1:
            
            json_string += i
        
        if i =='}' and record ==1:
            
            list_of_students_JSON += [json_string]
            
            record = 0
    
    #convert student ID into student objects
            
    #using Student module function
            
    for i in list_of_students_JSON:
        
        filtered_student = student.Student.from_JSON(i)
        
        student_list += [filtered_student]
    
    return student_list
        
        
def csv_to_dictionary(data):
    '''(str)-> dict
 
takes a string in CSV format and returns
a dictionary where the keys are the sick
students’ ids, and for each sick student the
value is the list of student IDs that the sick student had
contact with
 
>>>data = load_file("cases.csv")
 
>>>print(csv_to_dictionary(data))
 
{'260808934': ['260840155', '260248711', '260996175',
'260476020', '260561504'], '260996175': ['260248711',
'260476020'], '260675874': ['260840155'], '260476020':
['260758421'], '260386543': ['260996175', '260248711',
'260476020', '260561504'], '260248711': ['260212160',
'260970944'], '260840155': ['260970944'], '260561504':
['260476020', '260248711'], '260970944': ['260212160']}
 
>>>data = load_file("cases1.csv")
 
>>>print(csv_to_dictionary(data))
 
{'260018288': ['260808934', '260996175', '260084903',
'260026473', '260072990', '260039118'], '260041845':
['260808934', '260996175', '260026473', '260072990'],
'260092533': ['260084903', '260026473', '260072990',
'260013314', '260041812', '260039118'], '260013314':
['260065208'], '260072990': ['260061737', '260013314'],
'260041812': ['260013314'], '260084903': ['260065208'],
'260808934': ['260065208'], '260026473': ['260065208'],
260996175': ['260065208'], '260061737': ['260013314',
'260041812'], '260039118': ['260041812']}
 
>>>data = load_file("cases2.csv")
 
>>>print(csv_to_dictionary(data))
  
{'260064375': ['260005925', '260032440'], '260094997':
['260072488', '260026754', '260010997', '260031971'],
'260092902': ['260010997', '260068501', '260005925',
'260064375'], '260031971': ['260092283', '260092902',
'260010997', '260005925'], '260010997': ['260005925',
'260031356'], '260068680': ['260094691', '260092283',
'260005925'], '260071927': ['260068680', '260094691',
'260014616'], '260014616': ['260064375', '260026754',
'260092902', '260010997', '260092283'], '260094691':
['260005925', '260092902'], '260026754': ['260064375',
'260010997', '260005925', '260092902', '260068501'],
'260072488': ['260064375'], '260092283': ['260064375',
'260068501', '260010997', '260092902', '260005925'],
'260012075': ['260095234'], '260025405': ['260094997'],
'260055764': ['260031971'], '260068501': ['260005925'],
'260095234': ['260092902']}
 
 
 
 '''
    
    
    result_dict = {}
    
    data_no_comma = data.replace(',','')
    
    #divides the data by lines
    
    data_per_line = data_no_comma.split('\n')
    
    list_per_line = []
    
     
    
    #seperate one string of student ids into a few
    
    for line in data_per_line:
        
        split_ids = line.split()
        
        list_per_line += [split_ids]
        
    #creates a dict, key: the first idex and values
        
    # are the remainders in the list
    
    for listed_line in list_per_line:
        
        result_dict[listed_line[0]] = listed_line[1:]
    
 
    return result_dict
 
 
 
 
def build_report(tracker):
    
    ''' (ContactTracker)-> str
 
With the provided ContactTracker object,
write a report in a specific format and return
the string'''
    
    import copy
    
    string = 'Contact Records:'+'\n'
        
    student_dict = copy.deepcopy(tracker.cases_with_contacts)
    
    #read through a dictionary and add 'had contact with' phrase
    
    for sick_student in student_dict:
        
        for student_object in tracker.students:
            
            if student_object.student_id ==sick_student:
                
                student_string = str(student_object)
        
        contact_list = tracker.get_contacts_by_student_id(sick_student)
        
        string += '\t'+student_string+' had contact with ' + str(contact_list) +'\n'
        
        
        
    # creates different sorts of student group using functions
    
    #from ContactTracker module
    
    patient_zeros = tracker.patient_zeros()
    
    potential_sick_students = tracker.potential_sick_students()
    
    sick_from_another_student = tracker.sick_from_another_student()
    
    most_viral_students = tracker.most_viral_students()
    
    most_contacted_student = tracker.most_contacted_student()
    
    ultra_spreaders = tracker.ultra_spreaders()
    
    non_spreaders = tracker.non_spreaders()
    
    #adds a name on each student group and add to the
    
    #result string
    
    string += 'Patient Zero(s): ' +str(patient_zeros) +'\n'
    
    string += 'Potential sick students: ' + str(potential_sick_students)+'\n'
    
    string += 'Sick students who got infected from another student: ' +str(sick_from_another_student)+'\n'
    
    string += 'Most viral students: '+str(most_viral_students)+'\n'
    
    string +='Most contacted students: '+ str(most_contacted_student)+'\n'
    
    string +='Ultra spreaders: '+str(ultra_spreaders)+'\n'
    
    string +='Non-spreaders: '+str(non_spreaders)
    
    
    
    #replace empty list with 'non' and erase list-brackets 
        
    replaced_string = string.replace('[]','none')
        
    replaced_string = replaced_string.replace('[','')
    
    replaced_string = replaced_string.replace(']','')
    
    
            
    return replaced_string
 
 
 
def write_in_file(file_name, text):
    '''(str,str)-> none
 
create a file with the name provided and write
the text and returns nothing.'''
    
    #open file, and write, except error -> close file
    f = open(file_name,'w')
    try:
        
        f.write(text)
    
    except:
        
        f.close()
    
    f.close()
    
def main():
    '''() -> none:
 
This function combines all the functions
in the above and excute them in order.
'''
    
    #load_file but when file not found, raise an error message
    
    try:
        
        data = load_file('all_students.json')
    
    except FileNotFoundError:
        
        "Sorry, the file " + 'all_students.json' + " could not be found."
    
    try:
        
        csv_data = load_file("cases.csv")
    
    except FileNotFoundError:
        
        "Sorry, the file " + 'cases.csv' + " could not be found."
    
    #Creates a ContactTracker object
        
    first_student_list = JSON_to_students(data)
        
    first_student_dictionary = csv_to_dictionary(csv_data)
              
    ct1 = ContactTracker.ContactTracker(first_student_list, first_student_dictionary)
    
    #creates a report in a file
    
    report = build_report(ct1)
    
    write_in_file('contact_tracing_report.txt',report)
    
            
 
        
