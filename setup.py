#!/usr/bin/env python3

import os
import re

path_to_token = input("Path to token: ")
with open('{token}'.format(token=input('Path to token: ')), 'r') as f:
	token = f.read().rsplit()[0]
print(token)

#token = path_to_token

path = '/v2/droplets'
scheme = 'https'
authority = 'api.digitalocean.com'


endpoint ='{scheme}://{authority}{path}'.format(scheme=scheme, authority=authority, path=path) 

endpoint = re.sub(' +', ' ', endpoint)
# FIXME - Format the Following String

data = 'sata'
token = 'smoken'


create_droplet_command = "curl -X POST -d \'{curl}\'                        \
                            -H \"Authentication: Bearer {token}\"           \
                            -H \"Content-Type: application/json\"           \
                            \"{endpoint}\".format(data=data,                \
                                                    token=token,            \
                                                    endpoint=endpoint)"     \


print (re.sub(' +', ' ', create_droplet_command))

#os.system(create_droplet_command)


#Then, we neeed to wait for the droplet to be created.
#os.systems()


#Then, we need to get the IP address of the droplet that we created.
#os.systems()

#Finally, we need to clone our dotfiles to the droplet.
#host =




#os.systems('ssh -o "StrictHostKeyChecking no" root@{host}                   \
#             \'bash -s\' < dotfiles/run.sh'.format(host=host)')
