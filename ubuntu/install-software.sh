#!/bin/bash

#install pwntools
sudo apt install python-pip
pip install pwntools

#install pwndbg, includge ROPgadget
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

#install libcsearcher and libc-database
git clone https://github.com/lieanu/LibcSearcher.git
cd LibcSearcher
python setup.py develop
cd libc
./get # get all libc

#install one_gadget
sudo apt install ruby
sudo gem install one_gadget

#install angr
sudo apt-get install python3-dev libffi-dev build-essential virtualenvwrapper
mkdir ~/.virtualenvs
echo -e "export WORKON_HOME=~/.virtualenvs\nsource /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
mkvirtualenv --python=/usr/bin/python3 angr && pip install angr
workon OR lsvirtualenv #list all virualenvs
mkvirtualenv angr #create and activate virtualenv, named angr
workon angr #activate virutalenv
deactivate #deactivate virualenv
rmvirtualenv angr #remove virtualenv

#install pin https://software.intel.com/en-us/articles/pin-a-binary-instrumentation-tool-downloads
cd source/tools/ManualExamples
make inscount0.test TARGET=intel64
make inscount2.test TARGET=intel64
cp /mnt/hgfs/snippet/ctf/re/tracecount.cpp ~/Downloads/pin-3.7-97619-g0d0c92f4f-gcc-linux/source/tools/ManualExamples
make tracecount.test TARGET=intel64

#https://blog.csdn.net/qq_35859258/article/details/79594009
root#wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add

#install kali tools https://www.linuxidc.com/Linux/2018-11/155269.htm
git clone https://github.com/LionSec/katoolin
https://github.com/rikonaka/katoolin4china

#TODO install sage http://www.sagemath.org/download-linux.html





cd ~/
# change sourse to ustc
echo "I suggest you modify the /etc/apt/sources.list file to speed up the download."
echo "Press Enter to continue~"
read test
#sudo  sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
# change sourse —— deb-src 
sudo sed -i 's/# deb-src/deb-src/' "/etc/apt/sources.list"
# change pip source
mkdir ~/.pip
echo -e "[global]\nindex-url = https://pypi.douban.com/simple/\n[install]\ntrusted-host = pypi.douban.com" >  ~/.pip/pip.conf
# support 32 bit
dpkg --add-architecture i386
sudo apt-get update
# sudo apt-get -y install lib32z1
sudo apt-get -y install libc6-i386
# maybe git？
sudo apt-get -y install git gdb
# install pwndbg
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
# install peda
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
# download the libc source to current directory(you can use gdb with this example command: directory ~/glibc-2.24/malloc/)
sudo apt-get source libc6-dev
# install pwntools
sudo apt-get -y install python python-pip
pip install pwntools
# install one_gadget
sudo apt-get -y install ruby
sudo gem install one_gadget
# download 
git clone https://github.com/niklasb/libc-database.git ~/libc-database
echo "Do you want to download libc-database now(Y/n)?"
read input
if [[ $input = "n" ]] || [[ $input = "N" ]]; then
	echo "you can cd ~/libc-database and run ./get to download the libc at anytime you want"
else
	cd ~/libc-database && ./get
fi
echo "========================================="
echo "=============Good, Enjoy it.============="
echo "========================================="
