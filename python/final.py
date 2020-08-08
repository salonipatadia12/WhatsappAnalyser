import re
import sys
import pickle
import calendar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nltk.classify import NaiveBayesClassifier
import nltk.classify.util


def clean(words):
    return dict([(word, True) for word in words])

f = open('python/model', 'rb')
classifier = pickle.load(f)
f.close()


def findMostUsedWord():
    d = {}
    for i in words_list:
        if i in d.keys():
            d[i] = d[i] + 1
        elif i.isalpha():
            d[i] = 1
    max = 0
    key = ''
    for k, v in d.items():
        if v > max:
            max = v
            key = k
    return key.capitalize(), max

def findTopFiveUsers():
    d = []
    for i in df_user.iterrows():
        d.append([i[1][0], i[0]])
    d.sort(reverse=True)
    top5_names = []
    top5_no_of_msgs = []
    c = 0
    for i in d:
        if i[1] != 'N/A':
            top5_no_of_msgs.append(i[0])
            top5_names.append(i[1])
            c += 1
        if c == 5: break
    return top5_no_of_msgs,top5_names


# Here ex3 file contains our whatsapp Chat Data
f = open('upload/ex3.txt', encoding='utf8')
l = []
ind = -1
for i in f:
    s = i.rstrip('\n')
    r = re.match(r'[\d]{1,2}/[\d]{2}/[\d]{2}, [\d]{1,2}:[\d]{2}', s)
    if r:
        l.append(s)
        ind = ind + 1
    else:
        l[ind] = l[ind] + s

f.close()


data = []
opinion={}
pos,neg=0,0
words_list = []
day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
for i in l:
    a = i.strip().split(',')
    a1 = a[0]
    a2, a3, a4 = a[0].strip().split('/')
    a5 = day_names[calendar.weekday(int(a4), int(a3), int(a2))]
    a6 = a[1].strip().split('-')
    a7 = a6[0].split(':')[0]
    a7 = int(a7)
    a8 = a6[0].split(' ')[1]
    if a8=="am":
        a7 = a7
    elif a8=="pm":
        a7 = a7+12
    c = a6[1].split(':')
    a9 = ''
    a10 = ''
    if len(c) >= 2 and 'changed' not in c[0]:
        a9 = c[0].strip()
        a10 = c[1]
    else:
        a9 = 'N/A'
        a10 = c[0]
    r = re.split(r'\W+', a10.lower())
    words_list.extend(r)
    a11 = len(a10)
    try:
        chat=a10
        name=a9
        if opinion.get(name,None) is None:
            opinion[name]=[0,0]
        res=classifier.classify(clean(chat))
        if res=='positive':
            pos+=1
            opinion[name][0]+=1
        else:
            neg+=1
            opinion[name][1]+=1
    except:
        pass
    data.append([a1, a2, month_names[int(a3) - 1], '20' + a4, a5, a6[0], a7, a8, a9, a10, a11])

df = pd.DataFrame(data,
                      columns=['Date', 'Day', 'Month', 'Year', 'Day_Name', 'Time', 'Time_H','meridiem', 'User', 'Message',
                               'MessageSize'])


df_user = df.groupby(['User']).count()
df_user.plot.bar(y='Message', title='Number of Messages by Each User')
plt.tight_layout()
plt.savefig('images/user.png')


df_month = df.groupby(['Month']).count()
df_month.plot.bar(y='Message', title='Number of Messages in each Month')
plt.tight_layout()
plt.savefig('images/month.png')


df_timeh = df.groupby(['Time_H']).count()
df_timeh.plot.bar(y='Message', title='Number of Messages in each Hour')
#plt.show()
plt.savefig('images/hours.png')



df_year = df.groupby(['Year']).count()
df_year.plot.bar(y='Message', title='Number of Messages in each Year')
#plt.show()
plt.savefig('images/year.png')



df_dayname = df.groupby(['Day_Name']).count()
df_dayname.plot.barh(y='Message', title='Number of Messages according to day_wise ')
#plt.show()
plt.tight_layout()
plt.savefig('images/days.png')



# for top 5 users
top5=findTopFiveUsers()
plt.pie(top5[0], labels=top5[1])
plt.title('Top 5 Users')
#plt.show()
plt.savefig('images/most.png')



neg=abs(neg)
labels = ['positive','negative']
sizes = [pos,neg]
fig1, ax1 = plt.subplots()
ax1.pie(sizes ,labels=labels, autopct='%1.1f%%')
plt.title('Whatsapp Sentiment Analysis')
#plt.show()
plt.savefig('images/senti.png')



names,positive,negative=[],[],[]
for name in opinion:
    names.append(name)
    positive.append(opinion[name][0])
    negative.append(opinion[name][1])
    
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')


ind = np.arange(len(names))
width=0.3
max_x=max(max(positive),max(negative))+2

#fig = plt.figure()
#ax = fig.add_subplot()
fig, ax =plt.subplots()
yvals = positive
rects1 = ax.bar(ind, yvals, width, color='g')
zvals = negative
rects2 = ax.bar(ind+width, zvals, width, color='r')

ax.set_xlabel('Names')
ax.set_ylabel('Sentiment')

ax.set_xticks(ind+width)
#ax.set_yticks(np.arange(0,max_x,1))
plt.xticks(rotation=90)
ax.set_xticklabels( names )
ax.legend( (rects1[0], rects2[0]), ('positive', 'negative') )
ax.set_title('Whatsapp Chat Sentiment Analysis')


autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
plt.savefig('images/sentibar.png')



month_list = df.groupby(['Month']).groups.keys()
list(month_list)

cnt_list = list(df.groupby('Month')['Date'].count())
d = cnt_list[0]
cnt_list.append(d)



category= month_list
values = cnt_list
label_placement=np.linspace(start=0, stop=2*np.pi, num=len(values))
plt.figure(figsize=(6,6))
plt.subplot(polar=True)
plt.plot(label_placement, values)
lines, labels = plt.thetagrids(np.degrees(label_placement), labels=category)
plt.savefig('images/spider.png')


from PIL import Image
from wordcloud import *
with open('word.txt', 'w') as filehandle:
    for listitem in words_list:
        if(listitem!='media' and listitem!='omitted'):
            filehandle.write('%s\n' % listitem)

dataset = open("word.txt", "r").read()
def create_word_cloud(string):
   maskArray = np.array(Image.open("images/whhhhh.png"))
   cloud = WordCloud(background_color = "white",mask = maskArray ,max_words = 200, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("images/word.png")
dataset = dataset.lower()
create_word_cloud(dataset)

