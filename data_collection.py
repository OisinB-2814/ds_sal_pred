#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:01:28 2020

@author: oisinbrannock
"""

import glassdoor_scraper as gs 


path = "/usr/local/bin/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)