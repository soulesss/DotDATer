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

#list creation function           
def lister(num):
    z =[]
    for el in range(0, num):
        sel = input('Select type: ')
        if sel == 'int':
            a = int(input('Inreger: '))
        elif sel == 'float':
            a = float(input('Float: '))
        elif sel == 'string':
            a = input('String: ')
        elif sel == 'list':
            x = int(input('Number of elements'))
            a = lister(x)
        else:
            print('An error has occured! Stoping operation...')
            break
        z.append(a)
    return z
    

#writer function
def writer(name, func):
    a = None
    num = int(input('Select number of elements: '))
    with open(name, 'wb') as file:
        for el in range(0, num):
            sel = input('Select type: ')
            if sel == 'int':
                a = int(input('Inreger: '))
            elif sel == 'float':
                a = float(input('Float: '))
            elif sel == 'string':
                a = input('String: ')
            elif sel == 'list':
                x = int(input('Number of elements: '))
                a = func(x)    
            else:
                print('An error has occured! Stoping operation...')
                break
            pickle.dump(a, file)
                            

#program starting
print('DoDATer v1.1 \n Copyright (c) 2020 soulesss')
print('_' * 32 + '\n')
opt = ''
while True:
    opt = input('Select option: "1" Reader from .dat file; "2" Writer from .txt to .dat(only string); "3" Writer for every type (excepting dictionary and cortege); "exit" to exit program ' + '\n   Your answer: ')
    if opt == 'exit':
        break
    name = input('Name of file: ')
    print(' '* 13 + '-' * 32 )
    if opt == '1':
        try:
            reader(name)
        except:
            print("!!!An error has occured. Maybe you wrote file's name wrong!!! \n")
    elif opt == '2':
        try:
            txt_writer(name)
        except:
            print("!!!An error has occured. Maybe you wrote file's name wrong!!! \n")
    elif opt == '3':
        try:
            writer(name, lister)
        except:
            print("!!!An error has occured. Maybe you wrote file's name wrong!!! \n")
    else:
        print('Something went wrong!')
    print('_' * 64)





print('\n'+'Thank you for using DotDATer.')
    

    
        


