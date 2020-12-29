#Copyright (c) 2020 soulesss
#distributed under MIT license


import pickle

#reader function
def reader(name):
    data = []
    with open(name, 'rb') as file:
        try:
            while True:
             a = pickle.load(file)
             data.append(a)
        except:
            print('\n Data loading is over. Result is: \n')
        for sub in data:
            print(sub)
    out_name = name[:len(name) - 4]
    with open( out_name + '.txt', 'w') as txt:
        for sub in data:
            txt.write(str(sub) + '\n')
    print('\n')
    return data



#writer funciton (writes data from .txt)
def txt_writer(name):
    data =[]
    txt = input('Name of text file: ')
    print(' '* 13 + '-' * 32 )
    with open(txt, 'r') as file:
        data = file.readlines()
    with open(name, 'wb') as file:
        for sub in data:
            pickle.dump(sub, file)
            

#program starting
print('DoDATer v1.0 \n Copyright (c) 2020 soulesss')
print('_' * 32 + '\n')
opt = ''
while True:
    opt = input('Select option: "1" Reader from .dat file; "2" Writer from .txt to .dat; "exit" to exit program ' + '\n   Your answer: ')
    if opt == 'exit':
        break
    name = input('Name of file: ')
    print(' '* 13 + '-' * 32 )
    if opt == '1':
        try:
            reader(name)
        except:
            print("!!!An error has occured. Maybe you wrote file's name wrong!!! \n")
    if opt == '2':
        txt_writer(name)





print('\n'+'Thank you for using DotDATer.')
    

    
        


