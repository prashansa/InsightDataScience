#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:53:05 2020

@author: gupta
"""


#!/usr/bin/env python3

import os

#TODO Make sure the modify it for every different month or archive source
internet_root_url = "https://archive.org/download/archiveteam-twitter-stream-2019-06/"
for num in range(1,31):
    cmd_txt = 'wget ' + internet_root_url + "twitter_stream_2019_06_{0:02d}.tar".format(num)
    os.system(cmd_txt)



# #!/bin/bash

# file="list_file__00.txt"

# while read -r line;  do
# echo "aws s3 cp s3://insighttwitterdeals/Twitter_dumps/$line Twitter_data/"
# echo tar -xvf $line
# echo aws s3 mv 2018/ s3://insighttwitterdeals/Twitter_dumps/bz2_folder/ --recursive
# done < "$file" 

























