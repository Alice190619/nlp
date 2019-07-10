#!/usr/bin/env python
# coding: utf-8

# In[104]:


simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article => 一个 | 这个
noun => 女人 | 篮球 | 桌子 | 小猫
verb => 看着 | 坐在 | 听着 | 看见
Adj => 蓝色的 | 好看的 | 小小的
"""


# In[105]:


another_grammar = """
#
"""


# In[114]:


import random


# In[115]:


def adj():
    return random.choice('蓝色的 | 好看的 | 小小的'.split('|')).split()[0]


# In[116]:


def adj_star():
    return random.choice([lambda : '',lambda : adj() + adj_star()])()


# In[117]:


adj_star()


# In[119]:


adj_grammar = """
Adj* => null | Adj Adj*
Adj => 蓝色的 | 好看的 | 小小的
"""


# In[120]:


def create_grammar(grammar_str, split='=>', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip():
            continue
        exp,stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar


# In[121]:


grammar['Adj*']


# In[122]:


choice = random.choice
def generate(gram,target):
    if target not in gram:
        return target #means target is a terminal expression
    expaned = [generate(gram, t) for t in choice(gram[target])]
    return ''.join([e if e != '/n' else '\n' for e in expaned if e != 'null'])


# In[123]:


example_grammar = create_grammar(simple_grammar)


# In[124]:


example_grammar


# In[126]:


generate(gram=example_grammar,target='sentence')


# In[127]:


#西部世界中，一个人类的语言可以定义为

human = """
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们
寻找 = 找找 | 想找点
活动 = 乐子 | 玩的
"""

#一个接待员的语言可以定义为
host = """
host = 寒暄 报数 询问 业务相关 结尾
报数 = 我是 数字 号 ，
数字 = 单个数字 | 数字 单个数字
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ，
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = null
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？
"""


# In[128]:


for i in range(20):
    print(generate(gram=create_grammar(host,split='='),target='host'))


# In[ ]:




