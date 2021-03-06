# import time, json, sys, os
# from wrappers import build

# from 

# def spin_up():
#     timestamp_utc = time.time()
#     writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
#     aws_lightsail = ['awsl','aws lightsail']
#     digital_ocean = ['do', 'digital ocean']
#     iaas_platform = aws_lightsail + digital_ocean
#     vendor_choice = 'do'
#     if vendor_choice in iaas_platform:
#         if vendor_choice in aws_lightsail:
#             pass
#         elif vendor_choice in digital_ocean:
#             os.system('{unix_command} > {writeout_file}'.format(unix_command=build.builder(),writeout_file=writeout_file))
            
#             time.sleep(60) #note: waiting for droplets to spin up so IP address are privisioned 
#             return harden(writeout_file)
#     else:
#         pass

# def harden(writeout_file):
#     response = json.load(open(writeout_file))
#     payloads = [] #opening empty string
#     #FIXME assignment below reults in a KeyError
#     if 'droplets' in response:
#         payloads = response['droplets']
#         print('mult') #temp
#     else:
#         payloads = [response['droplet']] #put these in a [] to iterate them..can't iterate them in a dict 
#         print('singular') #temp
#     # return payloads #temp
#     ip_addressess = []
#     for payload in playloads:
#         ip_addressess.append(build.get_host(payload['id'], writeout_file)) 
#         # inside of get_host() 



#     y = response['droplet']['id']
#     timestamp_utc =
#     c = build.get_ip_address(y, timestamp_utc)
#     return c 
# if __name__ == '__main__':
#     from pprint import pprint
#     harden(spin_up())




#!/usr/bin/env python3

import time, json, sys, os
from pprint import pprint
import digitalocean

def spin_up():
    timestamp_utc = time.time()
    writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    # vendor_choice = input('vendor_choice: ')
    vendor_choice = 'do'
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'             \
                        .format(unix_command=digitalocean.builder(), \
                                writeout_file=writeout_file))
            time.sleep(60) 
            #gives you time for the vm to set up 
            return harden(writeout_file)
    else:
        pass # TODO 2

def harden(writeout_file):
    response = json.load(open(writeout_file))
    #writeout file spits out json object 
    if 'droplets' in response:
        payloads = response['droplets']
        #checks for more than one droplet 
    else:
        payloads = [response['droplet']]
        #check for one droplet 
    ip_addresses = []
    for payload in payloads:
        ip_addresses.append(digitalocean.get_host(payload['id'], writeout_file))
    for ip_address in ip_addresses:
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote0.sh'.format(ip_address=ip_address))
        #sets up root settings. safety procedures 
        os.system('scp /home/soo/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/soo/authorized_keys'.format(ip_address=ip_address))
        os.system('sh -c \'echo "soo:swordfish" > /home/soo/dotfiles/setup/.credentials\'')
        os.system('scp /home/soo/projects/dotfiles/setup/.credentials root@{ip_address}:/home/soo/'.format(ip_address=ip_address))
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote1.sh'.format(ip_address=ip_address))
    return ip_addresses


if __name__ == '__main__':
    pprint(spin_up())