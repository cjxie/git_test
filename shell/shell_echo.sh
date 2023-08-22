#!/bin/bash

echo hello
echo Enter a name

read name
echo $name is good name

echo -e "new line! \n"
echo it is a test

echo -e "echo cata \c"
echo "it is a test"

echo "it is a new test" > myfile

echo "单引号不进行转义"
echo '$name\"'

echo "显示命令执行结果："
echo `date`
