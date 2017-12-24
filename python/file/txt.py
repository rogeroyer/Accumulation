
# 读取txt文件 #
f = open(r"D:\dataSet\NLP\news_classification\dict.txt", encoding='utf-8')             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
string = []
while line:
    string.append(line.split('\t')[0])
    # print(line)              # 后面跟 ',' 将忽略换行符
    # print(line, end = '')　　　# 在 Python 3中使用
    line = f.readline()

f.close()

print(string[0])
print(string[1])
print(string[2])

fl = open('dict.txt', 'w', encoding='utf-8')

for i in string:
    fl.write(i)
    fl.write("\n")

fl.close()
