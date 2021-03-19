#!/bin/bash
filename=$1
while read line; do
# reading each line
python3 SecretFinder.py -i $line
done < $filename
