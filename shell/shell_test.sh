#!/bin/bash

num1=100
num2=100

res1=$[num1+num2]
res2=`expr $num1 + $num2`

echo "res1= ${res1}, res2= ${res2}"

# 逻辑判断 vs test command
echo "[ \$res1 == \$res2 ] = test \$res1 = \$num2"
