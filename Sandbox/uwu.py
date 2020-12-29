import pickle


with open('www.dat','rb') as file:
    a = pickle.load(file)
    b = pickle.load(file)
    
c = int(b[2]) +3
print(c)

