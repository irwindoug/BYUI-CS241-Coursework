#!/bin/bash

number=0

read -p "Enter a number > " number

echo "Number is $number"
if [ $((number % 2)) -eq 0 ]; then
    echo "Number is even"
else
    echo "Number is odd"
fi 