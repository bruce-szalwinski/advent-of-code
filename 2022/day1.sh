#!/bin/bash

awk -v RS= '{print > ("whatever-" NR ".txt")}' input1

calories_by_elf() {
  for i in $(ls whatever*)
  do
    calories=$(cat $i | paste -sd+ -|bc)
    echo $i $calories
  done
}

top_elf() {
  calories_by_elf | sort -k 2 -n -r | head -1
}

top_three_elves() {
  calories_by_elf | sort -k 2 -n -r | head -3 | awk '{print $2}' | paste -sd+ - | bc
}

top_elf
top_three_elves


