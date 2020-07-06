#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:43:37 2020

@author: gupta
"""


from requests_aws4auth import AWS4Auth
import boto3
import requests

host = 'https://prashansasdomain.us-east-1.es.amazonaws.com/' # The domain with https:// and trailing slash. For example, https://my-test-domain.us-east-1.es.amazonaws.com/
path = 'https://search-prashansasdomain-ty7samwrnomzpciusl6eakytwm.us-east-1.es.amazonaws.com' # the Elasticsearch API endpoint
region = 'us-east-1' # For example, us-west-1

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

url = host + path

# The JSON body to accompany the request (if necessary)
payload = {
    "settings" : {
        "number_of_shards" : 7,
        "number_of_replicas" : 2
    }
}

r = requests.put(url, auth=awsauth, json=payload) # requests.get, post, and delete have similar syntax

print(r.text)
























