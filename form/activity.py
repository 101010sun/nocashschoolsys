import server

print('-------- ACTIVITY PAGE --------')
print('1.社團登記 2.課堂/活動登記')
registration = int(input())
if(registration==1):
    nid = str(input('NID: '))
    club = str(input('社團名稱：'))

    server.insert_organization(nid, club)
    server.find_organization()

elif(registration==2):
    nid = str(input('NID: '))
    activename = str(input('課堂/活動名稱：'))
    credit = int(input('學分數：'))
    rank = int(input('上學期班排：'))
    average = float(input('上學期總平均:'))

    server.insert_active(nid,activename, average, credit, rank)
    server.find_active()
