#imports
from os import listdir
from os.path import isfile, join
import pandas as pd

#Locais
pasta = '..//data//Reações//Grupo1- 0,5 -//Excel'

reactions=True
media = False
iskbase=True
results=False

inner=False
outer=True

fluxo=False
composi=False

files = [f for f in listdir(pasta) if isfile(join(pasta, f))]
print(files)

# files tem uma lista com o nome de todos os arquivos da pasta
arq1=pasta+'\\'+files[0] #é o local do arquivo 1

cols=0

if reactions == True:
    cols=['id','direction','flux']
elif media == True:
    if fluxo == True:
        cols=['compounds','minFlux','maxFlux']
    elif composi == True:
        cols = ['compounds', 'name']
    iskbase = False
elif results == True and reactions == True:
    cols = ['id', 'Enzime', 'Reaction']
    iskbase = False
elif results == True and media == True:
    cols =['compounds', 'name' ]
    iskbase = False
else:
    print("nenhum foi selecionado")



if inner == True:
    how="inner"
    outer = False
elif outer == True:
    how="outer"


# Transformando xlsx em dataframe
with pd.ExcelFile(arq1) as xlsx: #leitura arquivo
    if iskbase == True:
        df1 = pd.read_excel(arq1, sheet_name=1)
        df1 = df1[cols]
    elif media == True:
        df1 = pd.read_excel(arq1)
        df1 = df1[cols]
    elif results == True and media == False:
        df1 = pd.read_excel(arq1, sheet_name=1)
        df1 = df1[cols]
    elif cols !=0:
        df1 = pd.read_excel(arq1)
        df1 = df1[cols]
    elif results == True and media == True:
        df1 = pd.read_excel(arq1)
        df1 = df1[cols]
    else:
        df1 = pd.read_excel(arq1)
xlsx.close()

data1=df1
#print(data1)
name='_' + files[0]

for l in range(len(files)-1):
   i=l+1
   arq= pasta+'\\'+files[i]

   with pd.ExcelFile(arq) as xlsx: #leitura arquivo
       if iskbase == True:
           df2 = pd.read_excel(arq, sheet_name=1)
           df2=df2[cols] #caso queira todas, remover
       elif media == True or results == True:
           df2 = pd.read_excel(arq)
           df2 = df2[cols]

       else:
           df2 = pd.read_excel(arq)

   #merge
   name = '_' + files[l]
   DF= pd.merge(data1,df2,how=how,on=[cols[0]], suffixes=(name, '_' + files[i])) ## merge
   xlsx.close()
   #name='' #nada ''
   data1=DF

#export
DF.to_excel(pasta+'\\@saida'+how+'.xlsx', index = False)
print('done saving')