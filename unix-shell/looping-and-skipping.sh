#!/bin/bash
#
# [https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem?isFullScreen=true]
#

for i in $(seq 100); do if test $(expr $i % 2) == 1 ; then echo $i; fi; done
