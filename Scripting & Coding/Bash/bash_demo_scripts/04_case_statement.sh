#!/bin/bash
# Case statement
echo "Enter a number between 1-3:"
read num
case $num in
    1) echo "One";;
    2) echo "Two";;
    3) echo "Three";;
    *) echo "Invalid";;
esac
