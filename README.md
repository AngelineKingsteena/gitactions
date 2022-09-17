SSH
<br>
 When you first create the server instance, you may or may not have the ssh server running. If it is not running, you can install it first. On Ubuntu/Debian, you can use the following command:
<br>
sudo apt install openssh-server
<br>
Next, we create a ssh key pair on our local machine with which we will access the server. From your local user home directory:
<br>
`mkdir .ssh`

`ssh-keygen`

`cd .ssh`

`less id_rsa.pub`

Copy this content to the following file authorized_keys in the webserver:

`mkdir .ssh`

vim authorized_keys #if vim is not present, you can use other editors or install it using `sudo apt install vim`

copy the content and quit (shift+colon> wq -> enter)

chmod 600 authorized_keys

We need to edit the following fields in the file /etc/ssh/sshd_config on the server (say using vim):

Port choose something other than 22 (opttional)

PermitRootLogin no (changed from prohibit-password)

PubkeyAuthentication yes (already defaults to this)

PasswordAuthentication no (disable it for security)

Restart the ssh server. In Ubuntu/Debian this is achieved by
`sudo systemctl restart ssh`

Firewall
A basic firewall such as ufw can help provide a layer of security.
Install and run it using the following commands (Ubuntu/Debian):

`sudo apt install ufw`

`sudo ufw allow [PortNumber]` #here it is 22 or another port that you chose for ssh

`sudo ufw enable`

`sudo ufw status verbose` #this should show what the firewall is doing
