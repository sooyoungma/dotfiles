#!/usr/bin/env python3

import os
import re 

scheme      = 'https'

authority   = 'api.digitalocean.com'
tag         = 'test'
path        = '/v2/droplets'
query_string = '?tag_name={tag}'.format(tag=tag)


endpoint = '{scheme}://                                             \
            {authority}                                             \
            {path}                                                  \
            {query_string}'.format(scheme=scheme,                   \
                                    authority=authority,            \
                                    path=path,                      \
                                    query_string=query_string)      

token = 'smoken'


teardown_droplet_command = "curl -X DELETE \
                            -H \"Content-Type: application/json\"    \
                            -H \"Authorization: Bearer {token}\"     \
                            \"{endpoint}\"".format(token=token,
                                                    endpoint=endpoint)



#This replaces multiple spaces with one space
teardown_droplet_command = re.sub(' +',' ', teardown_droplet_command)
print(teardown_droplet_command)
