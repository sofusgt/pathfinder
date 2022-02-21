#!/bin/bash
input="reverse-cities.txt"
while IFS= read -r line
do
  python3 get-nodes-in-city.py $line
done < "$input"