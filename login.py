import server

flag = 0
print('-------- LOGIN PAGE --------')
id = input('-Input your NID：')
search_st = server.find_student()
search_te = server.find_teacher()
#search NID of students' account
for d in search_st:
    if d['NID'] == id:
        print('- Welcome Student:' + id)
        flag = 1
#search NID of teachers' account
for d in search_te:
    if d['NID'] == id:
        print('- Welcome Teacher:' + id)
        flag = 1
#search no result
if(flag == 0): print('No Account ! Register or Try Again !')

