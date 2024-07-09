file=open('test.txt',mode='r+',encoding='utf-8')
abc=file.read().split(',')
print(abc)
print(type(abc))