#!/bin/bash

if [ $# -ne 1 ]; then
  exit 1
fi

i=0
while [ $i -lt $1 ];
do
  let i=$i+1
  if (($i % 15 == 0)); then
	echo 'fizzbuzz'
  elif (($i % 3 == 0)); then
	echo 'fizz'
  elif (($i % 5 == 0)); then
	echo 'buzz'
  else
	echo $i
  fi
done
exit 0
