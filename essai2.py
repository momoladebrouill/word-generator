"""
from pandas_ods_reader import read_ods
#on peut aussi utiliser le csv
df = read_ods("mots.ods",1, columns=["type", "freq", "mot"])
#premier mot à la ligne 4
for i in range(4,15):
  print(df['mot'][i],i)
"""
import random
f=open('mots.csv','r').read()

deb=0
vocab={}
types=[]
while "\n" in f[deb:]:
  #extraire la ligne
  ligne=f[deb:f.find('\n',deb+1)]
  deb+=len(ligne)
  typ=ligne.find(',')
  mot=ligne.find(',',typ+1)
  if ligne[1:typ] in types:
    vocab[ligne[1:typ]].append(ligne[mot+1:]+' ')
  else:
    types.append(ligne[1:typ])
    vocab[ligne[1:typ]]=[]
print(vocab.keys())
abc='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(sep=' ')

suiv={}
for genre in vocab:
  suiv[genre]={}
  for mot in vocab[genre]:
    for ind in range(len(mot)):
      lettre=mot[ind]
      try:
        suiv[genre][lettre]=suiv[genre].get(lettre,[])+[mot[ind+1]]
      except:
        pass
print(suiv['verbe'].keys())
def create(nature=None,weird=None):
  if not nature: nature=random.choice(types)
  if not weird: weird=random.choice(abc)
  choice=''
  while choice!=' ':
    try:
      choice=random.choice(suiv[nature][weird[-1]])
    except:
      choice=' '
    weird+=choice
  return weird[:-1],nature
for i in range(10):
  print(create(),end='\n::')

