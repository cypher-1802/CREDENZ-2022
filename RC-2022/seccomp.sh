#!/bin/sh
pip3 install -r requirements.txt
sudo apt-get install autoconf libtool gperf
pip3 install cython
git clone https://github.com/seccomp/libseccomp
cd libseccomp
sudo chmod +x autogen.sh
./autogen.sh
./configure
make
sudo make install
cd src/python/
sed -i 's/version.*/version = "2.4.4",/' setup.py
python3 setup.py install
cd ../..
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
export LD_LIBRARY_PATH
cd ..
