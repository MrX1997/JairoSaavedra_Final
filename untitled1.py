import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# Loading work data 
names=['Q1','Q2','Q3','Q4','Q8','Q9','Q16_Part_1','Q16_Part_2','Q16_Part_3','Q16_Part_4','Q16_Part_5','Q16_Part_6','Q16_Part_7','Q16_Part_8','Q16_Part_9','Q16_Part_10','Q16_Part_11','Q16_Part_12','Q16_Part_13','Q16_Part_14','Q16_Part_15','Q16_Part_16'
,'Q16_Part_18']
data=pd.read_csv('multipleChoiceResponses.csv',usecols=names)
data=data.iloc[1:,:]

# 

# Segregating data in Latin Countries 
def latin_countries(data):
    dataC=data[data['Q3']=='Colombia']
    dataCh=data[data['Q3']=='Chile']
    dataP=data[data['Q3']=='Peru']
    dataB=data[data['Q3']=='Brazil']
    dataAr=data[data['Q3']=='Argentina']
    dataMx=data[data['Q3']=='Mexico']

    # Concatening all countries on one matrix
    frames=[dataC,dataCh,dataP,dataB,dataAr,dataMx]
    new_data= pd.concat(frames)
    return new_data
new_data=latin_countries(data)

# Eliminating data with nan's.
def nans_killer(new_data):
    new_data=new_data.drop(new_data[new_data['Q1']=='Prefer to self-describe'].index)   
    new_data=new_data.drop(new_data[new_data['Q1']=='Prefer not to say'].index)
    new_data=new_data.drop(new_data[new_data['Q4']=='I prefer not to answer'].index)
    new_data=new_data.dropna(axis=0,subset=['Q4'])
    new_data=new_data.dropna(axis=0,subset=['Q8'])
    new_data=new_data.dropna(axis=0,subset=['Q9'])
    new_data=new_data.drop(new_data[new_data['Q9']=='I do not wish to disclose my approximate yearly compensation'].index)
    return new_data
new_data=nans_killer(new_data)

def matrix(data):
    data=data.fillna(0)
    data=data.values
    data=data.T
    #print(data)
    rows=len(data[0])

    matrix=np.zeros((7,rows))
    
    ii=data[0]=='Male'
    matrix[0,ii]=1.0
    matrix[0,~ii]=-1.0
    
    i1=data[1]=='18-21'
    i2=data[1]=='22-24'
    i3=data[1]=='25-29'
    i4=data[1]=='30-34'
    i5=data[1]=='35-39'
    i6=data[1]=='40-44'
    i7=data[1]=='45-49'
    i8=data[1]=='50-54'
    i9=data[1]=='55-59'
    i10=data[1]=='60-69'
    i11=data[1]=='70-79'
    i12=data[1]=='80+'
    matrix[1,i1]=np.mean([18,21])
    matrix[1,i2]=np.mean([22,24])
    matrix[1,i3]=np.mean([25,29])
    matrix[1,i4]=np.mean([30,34])
    matrix[1,i5]=np.mean([35,39])
    matrix[1,i6]=np.mean([40,44])
    matrix[1,i7]=np.mean([45,49])
    matrix[1,i8]=np.mean([50,54])
    matrix[1,i9]=np.mean([55,59])
    matrix[1,i10]=np.mean([60,69])
    matrix[1,i11]=np.mean([70,79])
    matrix[1,i12]=80.0
    
    o1=data[2]=='Colombia'
    o2=data[2]=='Chile'
    o3=data[2]=='Peru'
    o4=data[2]=='Brazil'
    o5=data[2]=='Argentica'
    o6=data[2]=='Mexico'
    matrix[2,o1]=10 
    matrix[2,o2]=20
    matrix[2,o3]=30
    matrix[2,o4]=40
    matrix[2,o5]=50
    matrix[2,o6]=60
    
    a1=data[3]=='Some college/university study without earning a bachelor’s degree'
    a2=data[3]=='Professional degree'
    a3=data[3]=='Bachelor’s degree'
    a4=data[3]=='Master’s degree'    
    a5=data[3]=='Doctoral degree'
    matrix[3,a1]=100 
    matrix[3,a2]=200
    matrix[3,a3]=300
    matrix[3,a4]=400
    matrix[3,a5]=500
    
    a1=data[5]=='0-10,000'
    a2=data[5]=='10-20,000'
    a3=data[5]=='20-30,000'
    a4=data[5]=='30-40,000'
    a5=data[5]=='40-50,000'
    a6=data[5]=='50-60,000'
    a7=data[5]=='60-70,000'
    a8=data[5]=='70-80,000'
    a9=data[5]=='80-90,000'
    a10=data[5]=='90-100,000'
    a11=data[5]=='100-125,000'
    a12=data[5]=='125-150,000'
    a13=data[5]=='150-200,000'
    a14=data[5]=='200-250,000'
    a15=data[5]=='250-300,000'
    a16=data[5]=='300-400,000'
    a17=data[5]=='400-500,000'
    a18=data[5]=='500,000+'
    matrix[4,a1]=786
    matrix[4,a2]=865
    matrix[4,a3]=322
    matrix[4,a4]=124
    matrix[4,a5]=325
    matrix[4,a6]=741
    matrix[4,a7]=965
    matrix[4,a8]=564
    matrix[4,a9]=624
    matrix[4,a10]=523
    matrix[4,a11]=693
    matrix[4,a12]=800
    matrix[4,a13]=738
    matrix[4,a14]=239
    matrix[4,a15]=469
    matrix[4,a16]=697
    matrix[4,a17]=108
    matrix[4,a18]=809
    
    a1=data[4]=='0-1'
    a2=data[4]=='1-2'
    a3=data[4]=='2-3'
    a4=data[4]=='3-4'
    a5=data[4]=='4-5'
    a6=data[4]=='5-10'
    a7=data[4]=='10-15'
    a8=data[4]=='15-20'
    a9=data[4]=='20-25'
    a10=data[4]=='25-30'
    a11=data[4]=='30+'
    matrix[5,a1]=0.5
    matrix[5,a2]=1.5
    matrix[5,a3]=2.5
    matrix[5,a4]=3.5
    matrix[5,a5]=4.5
    matrix[5,a6]=7.5
    matrix[5,a7]=12.5
    matrix[5,a8]=17.5
    matrix[5,a9]=22.5
    matrix[5,a10]=27.5
    matrix[5,a11]=30
    rang=np.arange(8,22,1)
    for j in range(rows):
        cont=0
        for i in rang:
            if(data[i,j]!=0):
                cont=cont+1
        matrix[6,j]=cont
    

    
    return matrix.T
matrix=matrix(new_data)
index=np.arange(0,1006,1)
columns=np.arange(0,7,1)
Data=pd.DataFrame(matrix,index=index,columns=columns)





#print(new_data)
countries=data['Q3']
#print(countries)