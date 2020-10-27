print('1.社團登記 2.活動登記')
registration = int(input())
if(registration==1):
    club = input('社團名稱：')
elif(registration==2):
    activename = input('社團名稱：')
    credit = input('學分數：')
    rank = input('上學期班排：')
    average = input('上學期總平均:')