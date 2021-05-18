#!/usr/bin/env python
# coding: utf-8

# In[7]:


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


# In[8]:


def get_posts(base_url, subreddit, n_iter, epoch_right_now):

    df_list = []
    current_time = epoch_right_now

    for post in range(n_iter):
        
        params = {
            'subreddit': subreddit,
            'size': 100,
            'lang': True,   
            'before': current_time
        }
        
        res = requests.get(base_url, params)

        df = pd.DataFrame(res.json()['data'])
        
        df = df[['subreddit', 'title', 'created_utc', 'selftext', 'author', 'media_only', 'permalink']]

        df_list.append(df)
        
        current_time = df['created_utc'].min()  
        
        # add wait time
        time.sleep(5)

    return pd.concat(df_list)


# In[9]:


reddit_url = 'https://api.pushshift.io/reddit/search/submission' 


# In[10]:


tolk_subreddit = 'tolkienfans'
tolkien_posts = get_posts(reddit_url, tolk_subreddit, n_iter=100, epoch_right_now=1616998184)


# In[11]:


hp_subreddit = 'harrypotter'
hp_posts = get_posts(reddit_url, hp_subreddit, n_iter=100, epoch_right_now=1616998184)


# In[12]:


posts = pd.concat([tolkien_posts, hp_posts])


# In[ ]:


posts.to_csv('../../data/reddit_posts.csv')

