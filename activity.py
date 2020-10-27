import server

activename = str
credit = int
rank = int
average = int
club = str
nid = str

print('1.社團登記 2.活動登記')
registration = int(input())
if(registration==1):
    nid = str(input('NID: '))
    club = str(input('社團名稱：'))

    server.insert_organization(nid, club)
    server.find_organization()

elif(registration==2):
    activename = str(input('課堂名稱：'))
    credit = int(input('學分數：'))
    rank = int(input('上學期班排：'))
    average = int(input('上學期總平均:'))

    server.insert_active(activename, average, credit, rank)
    server.find_active()
