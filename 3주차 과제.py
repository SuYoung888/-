print("--당첨자 발표--")
from random import *
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(lst) 
lst_1 = sample(lst, 4)
print("치킨 당첨자 : ", lst_1[0])
print("커피 당첨자 : ", lst_1[1:])
print("--축하합니다---")

#from random import *
#users = range(1, 21)
#users = list(users)
#shuffle(users)
#winners = sample(users, 4)
#print(" -- 당첨자 발표 -- ")
#print("치킨 당첨자 : {0}".format(winners[0]))
#print("커피 당첨자 : {0}".format(winners[1:]))
#print(" -- 축하합니다 -- ")

from random import *
customers = range(1, 51)
customers = list(customers)
time_customers = range(1, 51)
time_customers = list(time_customers)
i = 0
num = 0
for customers[i] in range(1, 51):
    time_customers[i] = randint(5, 50)
    if 5 <= time_customers[i] <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i + 1, time_customers[i]))
        num += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i + 1, time_customers[i]))
    i += 1
print("")
print("총 탑승 승객 : {0}분".format(num))

#from random import *
#cnt = 0
#for i in range(1, 51):
#    time = randrange(5, 51)
#    if 5 <= time <= 15:
#        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#        cnt += 1
#    else:
#        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#print("총 탑승 승객 : {0} 분".format(cnt)) 





