#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import re
import io
import jieba
import json
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',
}
sequence=[]
rsequence=[]
aggregate=['5963120294','5963137527','5963276398','5963339045','5963278775','5974620716','5979269414','5979342237','5979747069','5979699081']
flag='1613982305419'
number='0'
for j in range(0,len(aggregate)):
    for i in range(0,40):
        url = 'https://coral.qq.com/article/'+aggregate[j]+'/comment/v2?callback=_article'+aggregate[j]+'commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+number+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+flag
        data = requests.get(url, headers=headers).content.decode()
        content='content":"(.*?),"'
        sequence=re.findall(content,data,re.S)
        rsequence.append(sequence)
        pat='"last":"(.*?)"'
        number=re.findall(pat,data,re.S)[0].replace("\n","").replace(" ","")
        flag=str(int(flag)+1)
with open('comment.txt', 'a' ,encoding='utf-8') as file:
    file.write(str(rsequence))
txt = io.open("comment.txt", "r", encoding='utf-8').read()
word= jieba.lcut(txt)
counts = {}
for w in word:
    if len(w) == 1:
        continue
    else:
        counts[w] = counts.get(w,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
xulie = []
for i in range(len(items)):
    m = {}
    w, count = items[i]
    if count >= 40:
        m['name'] = w
        m['value'] = count
        xulie.append(m)
result= {}
result[''] = xulie
print(result)
with open('xyd.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)


# In[ ]:




