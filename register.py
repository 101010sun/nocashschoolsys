import server

identity = int(input('你的身分是(1.老師 2.學生): '))
if(identity==1):
    nid = str(input('NID: '))
    name = str(input('姓名: '))
    department = str(input('系所: '))
    server.insert_teacher(nid, name, department)
    server.find_teacher()
    
elif(identity==2):
    nid = input('NID: ')
    name = input('姓名: ')
    department = input('系所: ')
    grade = input('年級: ')
    sex = input('性別: ')
    residence = input('居住地: ')
    server.insert_student(nid, name, department, grade, sex, residence)
    server.find_student()
        
  