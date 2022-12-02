#!/bin/bash

part1() {
  join -j 2  <( cat input| sed 's/ //g' | sort | uniq -c) <(cat converter) | awk '{print $2*$3}' | paste -sd+ - | bc
}

part1
