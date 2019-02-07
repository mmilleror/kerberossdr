#/bin/sh!

sudo kill $(ps aux | grep 'rtl' | awk '{print $2}')
#sudo killall -s 9 rtl*
sudo pkill rtl_daq
sudo pkill sim
sudo pkill sync
sudo pkill gate
sudo pkill python3
