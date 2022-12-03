#!/bin/bash

part1() {
  join -j 2  <( cat input| sed 's/ //g' | sort | uniq -c) <(cat converter1 | grep -v "#") | awk '{print $2*$3}' | paste -sd+ - | bc
}

part2() {
   join -j 2  <( cat input| sed 's/ //g' | sort | uniq -c) <(cat converter2 | grep -v "#"| sort -k 2) | awk '{print $2, $3}' | sort -k 2 | join -j 2 <(cat converter1 | grep -v "#") - | awk '{print $2*$3}' | paste -sd+ - | bc
}

part1
part2
