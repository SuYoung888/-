def std_weight(height, gender):
    if gender == "male":
        weight = height * height * 22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height * 100, weight))
    elif gender == "female":
        weight = height * height * 21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height * 100, weight))
std_weight(1.69, 'male')
std_weight(1.65, 'female')

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))