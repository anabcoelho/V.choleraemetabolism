# Table
# Name_media | bio1    | # reactions   | Group
# arquivo    | dado df | num linhas -3 | fixo input
#Imports
from os import listdir
from os.path import isfile, join
import pandas as pd



#Locais
pasta = '..//data//Media//media-err//xlsx'
files = [f for f in listdir(pasta) if isfile(join(pasta, f))]
# files tem uma lista com o nome de todos os arquivos da pasta

grp= "0flux"


cols=['id','flux']

d = {'Namemedia': [], 'bio1': [], '#reactions': [], "grp": []}
df = pd.DataFrame(d)

for i in range(len(files)):
   arq= pasta+'\\'+files[i]

   with pd.ExcelFile(arq) as xlsx: #leitura arquivo

       df2 = pd.read_excel(arq, sheet_name=1)
       df2=df2[cols] #caso queira todas, remover

   countlines= len(df2.index)

   bio1loc= countlines-2
   bio1value= df2.at[bio1loc,'flux']

   newline = {'Namemedia': files[i], 'bio1': bio1value, '#reactions': countlines-3, "grp":grp}
   df = df.append(newline, ignore_index=True) # warning The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
   xlsx.close()
   #name='' #nada ''


#export
df.to_excel('..\\data\\Reações\\Reaction_analysis\\@analisereação'+ 'grp'+ str(grp) + '.xlsx', index = False)
print('done saving')