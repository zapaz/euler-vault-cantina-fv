#!/bin/sh
# This is a script to run certoraRun on all .conf files in the certora/confs directory

for conf_file in certora/confs/*.conf
do
  certoraRun "$conf_file"
done