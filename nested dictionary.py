course={

    'php':{'duration':'3 months', 'fees': '15000'},
    'java':{'duration': '2 months', 'fees': ' 12000'},
    'python': {'duration':'1.5 months','fees':'10000'}
     
}

#for printing dictionary and its items
#print(course)
#print(course['php']['fees'])
#print(course['java'])


#for iteration of items
#for k,v in course.items():
    #print(k,v['duration'],v['fees'])


#for updating items and values in dictionary

course['java']['fees']=20000
print(course['java']['fees'])



    
