#!/bin/bash

for i in {1..10} # Runs 10 times
do
    python3 main.py &
    PID=$! # Gets latest process' PID
    sleep 1 # Takes about one second for pygame to initialize
    sleep 120 # Sleeps for 120 seconds or two minutes
    screencapture -x static/screenshots/$i.jpg # Takes a screenshot and saves it in the screenshot folder with the trial name
    kill $PID # Kills the process based on PID
done