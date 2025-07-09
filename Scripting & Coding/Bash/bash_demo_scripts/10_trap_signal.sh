#!/bin/bash
# Trap example
trap "echo Caught SIGINT, exiting safely...; exit" SIGINT
echo "Press Ctrl+C to test trap"
while true; do
    sleep 1
done
