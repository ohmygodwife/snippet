#!/bin/sh
for i in `seq 500`
do
    cp small fake
    sleep 0.000001
    rm fake
    ln -s big fake
    rm fake
done