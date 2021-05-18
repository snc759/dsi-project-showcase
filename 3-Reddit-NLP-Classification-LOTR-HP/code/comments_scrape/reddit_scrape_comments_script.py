#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Imports

# Standards
import numpy as np
import pandas as pd

# API
import requests

# Automating
import time
import datetime as dt
import warnings
import sys


# In[10]:


def get_comments(base_url, subreddit, n_iter, epoch_right_now):

    df_list = []
    current_time = epoch_right_now

    for comment in range(n_iter):
        
        params = {
            'subreddit': subreddit,
            'size': 100,
            'lang': True,   
            'before': current_time
        }
        
        res = requests.get(base_url, params)

        df = pd.DataFrame(res.json()['data'])
        
        df = df[['subreddit', 'created_utc', 'body', 'author', 'permalink']]

        df_list.append(df)
        
        current_time = df['created_utc'].min()  
        
        # add wait time
        time.sleep(5)

    return pd.concat(df_list)


# In[11]:


reddit_url = 'https://api.pushshift.io/reddit/search/comment' 


# In[12]:


tolk_subreddit = 'tolkienfans'
tolkien_comments = get_comments(reddit_url, tolk_subreddit, n_iter=100, epoch_right_now=1616998184)


# In[13]:


hp_subreddit = 'harrypotter'
hp_comments = get_comments(reddit_url, hp_subreddit, n_iter=100, epoch_right_now=1616998184)


# In[14]:


comments = pd.concat([tolkien_comments, hp_comments])


# In[15]:


comments.to_csv('../../data/reddit_comments.csv')


# In[ ]:




