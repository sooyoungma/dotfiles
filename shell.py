import time, json, sys, os
from wrappers import digitalocean

def spin_up():
    timestamp_utc = time.time()
    writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl','aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = 'do'
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'.format(unix_command=digitalocean.builder(),writeout_file=writeout_file))
            return writeout_file
    else:
        pass

def harden(writeout_file):
    response = json.load(open(writeout_file))
    #FIXME assignment below reults in a KeyError
    if 'droplets' in response:
        ids = response['droplets']

    y = response['droplet']['id']
    timestamp_utc =
    c = digitalocean.get_ip_address(y, timestamp_utc)

if __name__ == '__main__':
    harden(spin_up())