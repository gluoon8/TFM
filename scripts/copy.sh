#!/bin/bash

# Script to copy a file to all the directories in the current directory
# Change the file name and the directories as needed


for directorio in *; do
  if [ -d "$directorio" ]; then
    cp INCAR "$directorio"
  fi
done