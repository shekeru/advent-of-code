#!/bin/bash

base=$(pwd)
for year in */; do
  for day in $year*/; do
    cd "$base/$day" && ghc "Solution.hs" -O2
    echo $day && time "./Solution.exe" > /dev/null 2>&1;
    time python3 Solution.py > /dev/null 2>&1;
  done
done
