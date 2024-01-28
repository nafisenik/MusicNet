import ast
import mido 
from mido import MidiFile 
import numpy as np
import math
import os
from pathlib import Path
#from scipy import spatial
c=9

def chunks(l, n):
    for i in range(1, len(l)-3, 1):
        yield l[i:i+n]


def findCorectNote(trainData, frequencies, listNote):
    
    freq=-1;
    correctNote=100
    for index,i in enumerate(trainData) :
        # print(type(i[5]))
        for l in range(2):
            # print(l)
            if(i[l] != listNote[l]):
                break
            if(l==1):
                 if(freq<frequencies[index]):
                    freq=frequencies[index]
                    correctNote=i[2]
                    # print(i)
                    
                    #c=correctNote
    # print(correctNote)
    return correctNote
            



                

# reading TrainData
trainData={}
with open('F:\\Current Sem\\Machine Learning\\Project\\first phase\\dict.txt', 'r') as f:
    trainData =ast.literal_eval (f.read())


#separating Chunks from frequencies
trainDataChunks=[]
for key, value in trainData.items():
    trainDataChunks.append(key)



#put train data chunks in a llist
trainDataChunksList=[]
for x in trainDataChunks:
    trainDataChunksList.append(list(x))




#put frequencies in a list
trainDatafreqList=[]
for key, value in trainData.items():
    trainDatafreqList.append(value)

path = 'F:\\Current Sem\\Machine Learning\\Project\\first phase\\test'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.mid' in file:
            files.append(os.path.join(r, file))

#reading ground truth
# vector2 = []
# mid = MidiFile('F:\\Current Sem\\Machine Learning\\Project\\first phase\\validation\\groundTruth\\child13.mid') 
# for i, track in enumerate(mid.tracks):     
#     for msg in track:         
#         if hasattr(msg, 'note'):            
#              vector2.append(msg.note)

# print(vector2)
# print("ground truth-------------------------------------------------------------------------------------------------------")

#reading the song file
alll=[]

for file in files:
    res=Path(file).stem
    
    # result=file.replace('\', '')
    # result2=os.path.splitext(file)[0]
    # result2=path.GetFileNameWithoutExtension(result)
    # print(result2)
    vector = []
    mid = MidiFile(file) 
    for i, track in enumerate(mid.tracks):     
        for msg in track:         
            if hasattr(msg, 'note'):            
                vector.append(msg.note)
    # print(vector)
    # print("input-------------------------------------------------------------------------------------------------------")
    # vectorCopy=vector;
    chunkCounter=0

    dif=[]



    for i, note in enumerate(vector):
        if i==0:
            dif.append(0)
        else:
            dif.append(vector[i]-vector[i-1])

    # print (dif)
    chunksofSong=list(chunks(dif, 3))


    jj=0


    while (jj<100):
        for index,i in enumerate (chunksofSong):
            # print(index)
            if i not in trainDataChunksList and abs(i[2])>5:
                
                # print (i)
                a=findCorectNote(trainDataChunksList,trainDatafreqList,i)
                # print(a)
                if a==100:
                    vector[index+3]=int(np.floor(np.mean(vector[index:index+6])))
                else:
                    vector[index+3]=vector[index+2]+a
                dif=[]
                for rr, note in enumerate(vector):
                    if rr==0:
                        dif.append(0)
                    else:
                        dif.append(vector[rr]-vector[rr-1])
                        
                        
                chunksofSong=list(chunks(dif, 3))
                break
        jj+=1
    res2=res+".txt"
    print(res2)
    f = open(res2,"w")
    f.write( str(vector) )
    f.close()

    # alll.append(vector)
    # file[-4:]=".txt" 
   
# f = open("all.txt","w")
# f.write( str(alll) )
# f.close()

