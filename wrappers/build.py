#!/usr/bin/env python3

import json
import os
import re
import sys
import time
import socket, requests
# ssh id 17376941 


def create_digital_ocean_vps():
    endpoint = 'https://api.digitalocean.com/v2/droplets'
    hostname = 'node'
    payload = {}
    pat_path = '/home{username}/.pat/.digitalocean'.format(username=('soo'))
    linux_pa_token = open('{pat_path}'.format(pat_path=pat_path)).read()
    a_header = 'Authorization: Bearer {linux_pa_token}'.format(linux_pa_token=linux_pa_token)
    c_header = 'Content-Type: application/json'
    vm_count = int(input('vm count '))
    if vm_count < 1:
        print("ERROR: You cannot spin up less than one server")
        create_digital_ocean_vps()
    elif vm_count < 2:
        payload['name'] = hostname
    else:
        payload['names'] = ['{hostname} {_}'.format(hostname=hostname,_=_).replace(' ', '-')for _ in range(vm_count)]
    payload['region'] = 'nyc1'
    payload['size']   = '1gb'
    payload['image']  = 'ubuntu-16-04-x64'
    headers = {}
    headers['Authorization'] = 'Bearer {linux_pa_token}'.format(linux_pa_token=linux_pa_token)
    headers['Content-Type'] = 'application/json'
    # keys = json.loads(requests.get('https://api.digitalocean.com/v2/account/keys', headers=headers).text)['ssh_keys']
    # payload['ssh_keys'] = [str(key['id']) for key in keys if key['name'] == socket.gethostname()]
    payload['ssh_keys'] = ['{ssh_key_id}'.format(ssh_key_id=17376941 )] #FIXME
    payload['tags'] = ['test']
    endstate = 'curl -X POST "{endpoint}" -d {x}{api_data}{x} -H "{a_header}" -H "{c_header}"'.format(endpoint=endpoint,x = "'",api_data=json.dumps(payload),a_header=a_header.strip(),c_header=c_header)
    # print(endstate)
    return re.sub(' +', ' ', endstate)

def build_single_vps():
    timestamp_utc = time.time()
    writeout_file = 'build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = 'do' # FIXME
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass # FIXME
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'                 \
                        .format(unix_command=create_digital_ocean_vps(),
                                writeout_file=writeout_file))
            sys.exit(0)
    else:
        pass # FIXME

def get_host(droplet_id, writeout_file):
    print(droplet_id)
    print(writeout_file)
    pat_path = '/Users/{username}/.pat/.digitalocean'.format(username=('soo'))
    linux_pa_token = open('{pat_path}'.format(pat_path=pat_path)).read()
    #writeout_file_i = writeout_file.split('.')[0] + writeout_file.split('.')[1] + '-' + str(droplet_id) + '.json'
    writeout_file_i = writeout_file.split('.')[0] \
     + writeout_file.split('.')[1] + '-'+ str(droplet_id) + '.json' os.system('curl -X GET "https://api.digitalocean.com/v2/droplets/{droplet_id}" \
    -H "Content-Type: application/json" -H "Authorization: Bearer {linux_pa_token}">                                   
    {writeout_file_i}'.format(droplet_id=droplet_id,linux_pa_token=linux_pa_token,writeout_file_i=writeout_file_i))payload = json.load(open(writeout_file_i))
    ip_address = payload['droplet']['networks']['v4'][0]['ip_address']
    
    return ip_address

if __name__ == '__main__':
    build_single_vps()