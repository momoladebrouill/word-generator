"""
from pandas_ods_reader import read_ods
#on peut aussi utiliser le csv
df = read_ods("mots.ods",1, columns=["type", "freq", "mot"])
#premier mot à la ligne 4
for i in range(4,15):
  print(df['mot'][i],i)
"""
import random
import keyboard
import time
f=open('mots.csv','r').read()
def recurence(lis):
  '''Renvoie un dictionnaire avec le nombre de fois qu'apparait chaque lettre'''
  lis.sort()
  i=0
  inventaire={}
  while i<len(lis):
    inventaire[lis[i]]=inventaire.get(lis[i],0)+1
    i+=1
  return inventaire
    
deb=0
vocab=[]
while "\n" in f[deb:]:
  #extraire la ligne
  ligne=f[deb:f.find('\n',deb+1)]
  deb+=len(ligne)
  freq=ligne.find(',')
  mot=ligne.find(',',freq+1)
  vocab.append(ligne[mot+1:]+' ')
  
abc='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(sep=' ')

suiv={}
for mot in vocab:
  for ind in range(len(mot)):
    lettre=mot[ind]
    try:
      suiv[lettre]=suiv.get(lettre,[])+[mot[ind+1]]
    except IndexError:
      pass
prob={}
for lettre in suiv:
  ls=suiv[lettre]
  ls.sort()
  total=len(ls)
  dic=recurence(ls)
  for key in dic:
    dic[key]=dic[key]/total
  prob[lettre]=dic

def create(weird=None):
  if not weird: weird=random.choice(abc)
  choice=''
  while choice!=' ':
      lieu=random.random()
      som=0
      try:
        dispo=prob[weird[-1]]
        choice=''
        for i in dispo:
          som+=dispo[i]
          if som>lieu:
            choice=i
            break
      except KeyError:
        choice=' '
      weird+=choice
  return weird[:-1]
