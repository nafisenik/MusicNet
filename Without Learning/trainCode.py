
import numpy as np
import mido 
from mido import MidiFile 
import os

def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l)-4, 1):
        # Create an index range for l of n items:
        
        yield l[i:i+n]


path = 'F:\\Current Sem\\Machine Learning\\Project\\first phase\\train'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.mid' in file:
            files.append(os.path.join(r, file))


vector = [] 
allChunks=[]
allVector=[]
for file in files:
  mid = MidiFile(file) 
  vector = [] 
  for i, track in enumerate(mid.tracks):     
      for msg in track:         
          if hasattr(msg, 'note'):            
               vector.append(msg.note)
  vector.pop()
  allVector.append(vector)



dif=[]
alldif=[]
for vector in allVector:
  dif=[]
  for i, note in enumerate(vector):
    if i==0:
      dif.append(0)
    else:
      dif.append(vector[i]-vector[i-1])
  a=list(chunks(dif, 3))
  alldif.extend(a)

f = open("alldis.txt","w")
f.write( str(alldif) )
f.close()
length=len(alldif)


d = {}
for l in alldif:
    t = tuple(l)
    if t in d:
        
        d[t] += 1
    else:
        d[t] = 1
  





x= {i:d[i] for i in d if d[i]>30}

print(len(x))
f = open("dict.txt","w")
f.write( str(x) )
f.close()
    







## diffrence list
# vectordif=[]

# for ww in range(3,10):
#   print (vector[ww])
#   print (vector[ww-1])


#   vectordif.append(vector[ww]-vector[ww-1])

#   print(vectordif)


# print(vectordif)

# #vectordif[0]=0

# #chunking tvectordif
# allChunks=[]
# a=list(chunks(vectordif, 3))
# allChunks.extend(a)
# print(allChunks)





#   a=list(chunks(vector, 7))
#   allChunks.extend(a)



 

# for j in allChunks:
#   for k in range(len(j)-1,-1,-1):
#     if(k==0):
#       j[k]=0
      
#     else:
#       j[k]=j[k]-j[k-1]

# length=len(allChunks)
# print(length)

# d = {}
# for l in allChunks:
#     t = tuple(l)
#     if t in d:
        
#         d[t] += 1/length
#     else:
#         d[t] = 1/length

# f = open("dict.txt","w")
# f.write( str(d) )
# f.close()
 

# # # for key, value in d.items(): 
# # #         print (value) 
    
  