#!/bin/bash
#
# [https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem?isFullScreen=true]
#

read x
read y

if test $x -gt $y; then
  echo X is greater than Y
elif test $x -lt $y; then
  echo X is less than Y
elif test $x -eq $y; then
  echo X is equal to Y  
fi
