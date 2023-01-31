import  os
line_train = [line.rstrip('\n') for i open(Data1.txt)]
line_val   =[line.rstrip('\n')] for i open(Data3.txt)]


for i in line_train:
    os.remove('E:\pythonProject\pythonProject\Test_Forlopp\HinhAnh'+i+'.jpg')
    os.remove('E:\pythonProject\pythonProject\Test_Forlopp\FileTXT'+i+'.txt')

for line in open(filename):
    do_something(line)