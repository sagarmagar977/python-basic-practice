import pickle
l=[10,20,30,40,50]
file=open("text.txt","wb")
pickle.dump(l,file)
file.close()   
