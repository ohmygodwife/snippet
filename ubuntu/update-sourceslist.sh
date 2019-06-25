#mv /etc/apt/sources.list /etc/apt/sources.list.bkp
Codename=$( (lsb_release -a)|awk '{print $2}'|tail -n 1 )
echo "\
deb http://ftp.sjtu.edu.cn/ubuntu/ $Codename main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ $Codename-backports main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ $Codename-proposed main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ $Codename-security main multiverse restricted universe
deb http://ftp.sjtu.edu.cn/ubuntu/ $Codename-updates main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ $Codename main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ $Codename-backports main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ $Codename-proposed main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ $Codename-security main multiverse restricted universe
deb-src http://ftp.sjtu.edu.cn/ubuntu/ $Codename-updates main multiverse restricted universe "> /etc/apt/sources.list
apt-get update