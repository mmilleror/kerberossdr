#!/bin/bash

echo "Starting Hydra offline test"
rm _receiver/C/gate_control_fifo
mkfifo _receiver/C/gate_control_fifo

rm _receiver/C/sync_control_fifo
mkfifo _receiver/C/sync_control_fifo

#python3 _GUI/hydra_main_window.py &
./_receiver/C/sim  2>log_err_sim 1| ./_receiver/C/sync 2>log_err_sync 1| ./_receiver/C/gate 2>log_err_gate 1| python3 _GUI/hydra_main_window.py

