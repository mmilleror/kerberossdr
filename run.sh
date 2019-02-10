#!/bin/bash

BUFF_SIZE=256 #Must be a power of 2. Normal values are 128, 256, 512

sudo sh -c "echo 0 > /sys/module/usbcore/parameters/usbfs_memory_mb"

echo "Starting KerberosSDR"

sudo kill $(ps aux | grep 'rtl' | awk '{print $2}')
sudo pkill rtl_daq
sudo pkill sim
sudo pkill sync
sudo pkill gate
sudo pkill python3

sleep 1

sudo mount -osize=30m tmpfs /ram -t tmpfs

rm _receiver/C/gate_control_fifo
mkfifo _receiver/C/gate_control_fifo

rm _receiver/C/sync_control_fifo
mkfifo _receiver/C/sync_control_fifo

rm _receiver/C/rec_control_fifo
mkfifo _receiver/C/rec_control_fifo

#nice -n -20 ./_receiver/C/rtl_daq 2>log_err_rtl_daq 1| ./_receiver/C/sync 2>log_err_sync 1| ./_receiver/C/gate 2> log_err_gate 1| python3 _GUI/hydra_main_window.py > log_dsp&
curr_user=$(whoami)
sudo chrt -r 51 ./_receiver/C/rtl_daq $BUFF_SIZE 2>log_err_rtl_daq 1| sudo chrt -r 50 ./_receiver/C/sync $BUFF_SIZE 2>log_err_sync 1| sudo chrt -r 50 ./_receiver/C/gate $BUFF_SIZE 2> log_err_gate 1| python3 _GUI/hydra_main_window.py $BUFF_SIZE&
#sudo chrt -r 51 ./_receiver/C/rtl_daq 2>log_err_rtl_daq 1| sudo chrt -r 50 ./_receiver/C/sync 2>log_err_sync 1| sudo chrt -r 50 ./_receiver/C/gate 2> log_err_gate 1| sudo nice -n -20 sudo -u $curr_user python3 _GUI/hydra_main_window.py&

#sudo php -S 192.168.4.1:80 -t _webDisplay >&- 2>&-
