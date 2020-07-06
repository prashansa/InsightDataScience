#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:14:02 2020

@author: gupta
"""


curl -XGET -u prashansagupta:Iamthemaster17! https://search-prashansasdomain-ty7samwrnomzpciusl6eakytwm.us-east-1.es.amazonaws.com/movies/_search?q=rebel&pretty=true



curl -XPOST -u prashansagupta:Iamthemaster17! https://search-prashansasdomain-ty7samwrnomzpciusl6eakytwm.us-east-1.es.amazonaws.com/_bulk --data-binary @bulk_movies.json -H 'Content-Type: application/json'



curl -XPUT -u prashansagupta:Iamthemaster17! https://search-prashansasdomain-ty7samwrnomzpciusl6eakytwm.us-east-1.es.amazonaws.com/movies/_doc/1 -d '{"director": "Burton, Tim", "genre": ["Comedy","Sci-Fi"], "year": 1996, "actor": ["Jack Nicholson","Pierce Brosnan","Sarah Jessica Parker"], "title": "Mars Attacks!"}' -H 'Content-Type: application/json'






























