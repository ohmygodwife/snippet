sudo chmod 777 /mnt/hgfs
#first uncomment "user_allow_other" in /etc/fuse.conf
echo "vmhgfs-fuse -o allow_other .host:/ctf /mnt/hgfs" >> ~/.profile