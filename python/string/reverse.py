# 字符串逆序 #
string = 'abcdefghijklmnopqrstuvwxyz'
str = ''
for index in range(len(string) - 1, -1, -1):
    str += string[index]
print(string)
print(str)
