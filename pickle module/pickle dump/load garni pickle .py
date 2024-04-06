import pickle
file=open("text.txt","rb")
l=pickle.load(file)
print(l)
    