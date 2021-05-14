#!/bin/sh

while true; do
    >/demo/demofile.txt
    date >> /demo/demofile.txt;
    sleep 1;
done 
