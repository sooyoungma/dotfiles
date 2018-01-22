#!/usr/bin/env bash

# Local: ssh root@$IP_ADDRESS
# Remote: > yes
# Remote: git clone git://github.com/sooyoungma/dotfiles.git

mv dotfiles/nano/.nanorc . 
#Remote: chmod +x dotfiles/run.sh
#Remote: ./dotfiles/run.sh

adduser --disabled-password --gecos "" $REMOTE_USERNAME
usermod -aG sudo $REMOTE_USERNAME
cp .nanorc /home/$REMOTE_USERNAME
mkdir /etch/ssh/$REMOTE_USERNAME

exit

#Local

sh -c 'echo "$REMOTE_USERNAME:$REMOTE_PASSWORD" >> /home/$LOCAL_USERNAME/.credentials'

scp /home/$LOCAL_USERNAME/.ssh/id_rsa.pub root@$IP_ADDRESS:/etc/ssh/$REMOTE_USERNAME/authorized_keys

scp .credentials root@$IP_ADDRESS:/home/$REMOTE_USERNAME/

ssh root @$IP_ADDRESS
