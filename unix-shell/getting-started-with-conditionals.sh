#!/bin/bash
#
# [https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem?isFullScreen=true]
#

read ch

if test $ch = 'Y' -o $ch = 'y'  ; then
  echo YES
elif test $ch = 'N' -o $ch = 'n'; then
  echo NO
fi
