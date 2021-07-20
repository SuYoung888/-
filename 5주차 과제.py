for num in range(1, 51):
    with open(str(num) + "주차.txt", "w", encoding="utf8") as weekly_file:
        weekly_file.write("- "+ str(num) + "주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ")

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
   
