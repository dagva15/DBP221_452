#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

#Seasons
Seasons = ['2015','2016','2017','2018','2019','2020']
Sdict = {"2015":0,"2016":1,"2017":2,"2018":3,"2019":4,"2020":5}

#Players
Players = ['LebronJames','JamesHarden','JohnWall','StephenCurry','GiannisAntetokounmpo','KevinDurant']
Pdict = {"LebronJames":0,"JamesHarden":1,"JohnWall":2,"StephenCurry":3,"GiannisAntetokounmpo":4,"KevinDurant":5}

#Salaries
LebronJames_salaries=[22970500,30963450,33285709,35654150,37436858,39219566]
JamesHarden_salaries=[15719062,26540100,28299399,30570000,38199000,41254920]
JohnWall_salaries=[14728844,15756438,18063850,19169800,38199000,41254920]
StephenCurry_salaries=[11370786,12112359,34682550,37457154,40231758,43006362]
GiannisAntetokounmpo_salaries=[1953960,2995420,22471911,24157304,25842697,27528088]
KevinDurant_salaries=[21971850,26540100,25000000,30000000,37199000,40108950]
Salary=np.array([LebronJames_salaries,JamesHarden_salaries,JohnWall_salaries,StephenCurry_salaries,GiannisAntetokounmpo_salaries,KevinDurant_salaries])
#Playoff_wins
LebronJames_playoff_wins=[14,16,13,12,0,16]
JamesHarden_playoff_wins=[9,1,6,11,6,5]
JohnWall_playoff_wins=[4,0,7,2,0,0]
StephenCurry_playoff_wins=[16,15,16,16,14,0]
GiannisAntetokounmpo_playoff_wins=[2,0,2,3,10,5]
KevinDurant_playoff_wins=[0,11,16,16,14,0]
playoff_wins=np.array([LebronJames_playoff_wins,JamesHarden_playoff_wins,JohnWall_playoff_wins,StephenCurry_playoff_wins,GiannisAntetokounmpo_playoff_wins,KevinDurant_playoff_wins])
#Games_played
LebronJames_games=[76,74,82,55,67,45]
JamesHarden_games=[82,81,72,78,68,44]
JohnWall_games=[77,78,41,32,0,40]
StephenCurry_games=[79,79,51,69,5,63]
GiannisAntetokounmpo_games=[80,80,75,72,63,61]
KevinDurant_playoff_games=[72,62,78,68,0,35]
games_played=np.array([LebronJames_games,JamesHarden_games,JohnWall_games,StephenCurry_games,GiannisAntetokounmpo_games,KevinDurant_playoff_games])




# In[6]:


Salary


# In[28]:


playoff_wins


# In[29]:


games_played


# In[8]:


import warnings
warnings.filterwarnings('ignore')
a=np.matrix.round(games_played/playoff_wins)
a[Pdict['JohnWall'],Sdict['2017']]


# In[9]:


games_played[0]>games_played[2]
# Lebron James 2015 болон 2016 оноос бусад улиралд John Wall-аас илүү тоглолт тогложээ. Учир нь Lebron James өөрийн биендээ
# маш их анхаарал хандуулдаг ба жилд дунджаар 1.5$ сая-ийг зарцуулдаг бол John Wall гэмтэл бэртэл ихтэй жилүүдийг өнгөрүүлж байна.


# In[19]:


champ_count=0
for i in StephenCurry_playoff_wins:
    if i==16:
        champ_count+=1
print('2015-2020 оны улирлуудад аварга болсон тоо: ',champ_count)
    
    


# In[22]:


LebronJames_games[5]>JamesHarden_games[5]


# In[23]:


Salary[5,5]<Salary[2,5]
# 2020-2021 оны улиралд John Wall нь Kevin Durant-аас илүү цалин авч байна.


# In[27]:


Salary[3][3]+Salary[5,3]
# Kevin Durant нь 2016-2017 оны улирлаас 2018-2019 оны улирал хүртэл 3 улирал Golden State Warriors багт Stephen Curry-тэй хамт 
# тоглосон бөгөөд тэд хамтдаа 3 жилийн хугацаанд 2 удаа аварга болсон бөгөөд тэдний хамт тоглосон сүүлийн улиралдаа авсан нийт цалин 


# In[ ]:




