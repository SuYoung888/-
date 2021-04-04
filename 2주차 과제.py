a = input('사이트를 입력하시오 : ')
a = a[7:]
a = a[:-4]
print(a[0:3] + str(len(a)) + str(a.count('e')) + '!')