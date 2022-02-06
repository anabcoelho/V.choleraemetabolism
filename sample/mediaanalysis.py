# Table
# Name_media | bio1    | # reactions   | Group
# arquivo    | dado df | num linhas -3 | fixo input
#Imports
from os import listdir
from os.path import isfile, join
import pandas as pd



#Locais
pasta = '..//data//Reações//Grupo1- 0,5 -//Excel'
files = [f for f in listdir(pasta) if isfile(join(pasta, f))]
print(files)

# files tem uma lista com o nome de todos os arquivos da pasta

cols=['id','flux']
grp= 0.3
d = {'Namemedia': [], 'bio1': [], '#reactions': [], "grp": []}
df = pd.DataFrame(d)

for i in range(len(files)):
   arq= pasta+'\\'+files[i]

   with pd.ExcelFile(arq) as xlsx: #leitura arquivo
       df2 = pd.read_excel(arq, sheet_name=1)
       df2=df2[cols] #caso queira todas, remover
       print(df2)
   countlines= len(df2.index)
   print(countlines)
   bio1loc= countlines-2
   bio1value= df2.at[bio1loc,'flux']

   newline = {'Namemedia': files[i], 'bio1': bio1value, '#reactions': countlines-3, "grp":grp}
   df = df.append(newline, ignore_index=True)
   xlsx.close()
   #name='' #nada ''


#export
df.to_excel(pasta+'\\@analisereação.xlsx', index = False)
print('done saving')