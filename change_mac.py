import re
import time
import subprocess
from subprocess import Popen, PIPE
from datetime import datetime


# =======================================================================================
# File Name: change_mac.py
# Creation Date: 4/11/2016
# Last Modified:
# Author: AStormOfCrickets
# Contact Info: astormofcrickets@thinkinginreverse.com
# ///////////////////////////////////////////////////////////////////////////////////////
# VERSION 0.1 BETA CODE
# ///////////////////////////////////////////////////////////////////////////////////////
# Purpose: The purpose of this code is to convert my chgMac bash script to run in a more
# extensible python framework. The chgMac script randomizes the MAC address with a list
# of valid OUIs so that it pairs a random OUI with a randomized NIC address and is
# designed to be run with a simple root cron job at startup.
#
# Version 0.1
#
# =======================================================================================


def main():
    cfg_file_loc = ".change_mac.config"
    log_file_name = "log_file_loc"
    log_start_msg = "-------- change_mac.py has started execution on"
    log_end_msg = "-------- change_mac.py has ended execution on"

    log_file_loc = _read_config_(log_file_name, cfg_file_loc)
    if log_file_loc == -1:
        print "The change_mac.py script has failed to open the configuration file."
        return 1
    elif log_file_loc == 1:
        print("The change_mac.py script has failed to find the configuration value: \"" +
              log_file_name + "\" in the configuration file.")
        return 1

    _log_msg_(log_start_msg, log_file_loc)


def _read_config_(
        cfg_var_name, cfg_file_loc):
    # Read configuration values from the config file
    conf_var = ""

    try:
        cfg_file = open(cfg_file_loc, 'r')
    except IOError:
        return -1

    for line in cfg_file:
        cmd, var = line.split("=")
        if cmd == cfg_var_name:
            conf_var = var
            break
    if not conf_var:
        cfg_file.close()
        return 1
    else:
        cfg_file.close()
        return conf_var


def _log_msg_(
        msg, file_loc):
    # Write the msg to the log file.
    month = str(datetime.now().month).zfill(2)
    day = str(datetime.now().day).zfill(2)
    year = str(datetime.now().year)

    try:
        log_file = open(file_loc, 'a')
    except IOError:
        print ("The change_mac.py script has failed to open its log file.")
        return 1

    log_msg_lst = [msg, " ", month, "/", day, "/", year, " at ", time.strftime(
        "%H:%M:%S"), "\n"]

    out_msg = "".join(log_msg_lst)
    log_file.write(out_msg)
    log_file.close()


main()
