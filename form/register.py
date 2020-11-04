import server

flag = 0
print('-------- REGISTER PAGE --------')
identity = int(input('你的身分是(1.老師 2.學生): '))
#register teacher's account
if(identity == 1):
    nid = str(input('NID: '))
    name = str(input('姓名: '))
    department = str(input('系所: '))
    #protect repeat register
    search_te = server.find_teacher()
    for d in search_te:
        if d['NID'] == nid:
            print('You had registered ! Please LOGIN')
            flag = 1
    if(flag == 0): 
        server.insert_teacher(nid, name, department)
        print('Register Successful !')
    
#register student's account   
elif(identity == 2):
    nid = str(input('NID: '))
    name = str(input('姓名: '))
    department = str(input('系所: '))
    grade = int(input('年級: '))
    sex = str(input('性別(Man/Woman): '))
    residence = str(input('居住地: '))
    #protect repeat register
    search_st = server.find_student()
    for d in search_st:
        if d['NID'] == nid:
            print('You had registered ! Please LOGIN')
            flag = 1
    if(flag == 0): 
        server.insert_student(nid, name, department, grade, sex, residence)
        print('Register Successful !')

        
  