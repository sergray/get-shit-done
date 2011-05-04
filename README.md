# get-shit-done.py - is the python clone of the get-shit-done php script
get-shit-done is an easy to use command line program that blocks websites known to distract us from our work.

After cloning this repository, put it in your $PATH and ensure it is executable.

Execute it as root because it modifies your hosts file and restarts your network daemon.

## To get-shit-done
`sudo get-shit-done work`

## To no longer get-shit-done
`sudo get-shit-done play`

### SITE_LIST
Add or remove elements of this array for sites to block or unblock.

### RESTART_NETWORK
Update this variable with the path to your network daemon along with any parameters needed to restart it.

### HOST_FILE
Update this variable to point to the location of your hosts file. Make sure it is an absolute path.

