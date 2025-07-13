#!/bin/bash
# For loop and while loop
echo "For loop 1 to 5:"
for i in {1..5}; do
    echo $i
done

echo "While loop 1 to 5:"
i=1
while [ $i -le 5 ]; do
    echo $i
    i=$((i+1))
done
