import server

while(1):
    id = input('NID：')
    search_st = server.find_student()
    search_te = server.find_teacher()
    for key, value in (d for d in search_st):
        if key == 'NID':
            if id == value:
                print('Welcome ' + id)
                break
    print('No Account ! Register or Try again !')


