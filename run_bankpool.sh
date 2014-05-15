#!/bin/sh
SERVICE='python ./run_p2pool.py --net bankcoin'

if ps ax | grep -v grep | grep "$SERVICE" > /dev/null
then
        echo "$SERVICE is already running!"
else
        screen -d -m -S screenbankcoin python ./run_p2pool.py --net bankcoin --give-author 0 --disable-upnp -f 1 -a BSYhvfF4BK2mjPhYMRGoKiVEVA5kBRadHx

	wait
fi
