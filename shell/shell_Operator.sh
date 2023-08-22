#!/bin/bash

val=`expr 2+2`
echo "Sum of two number:val=expr 2+2 = $val"

echo "Sum of two number:val=expr 2 + 2 = `expr 2 + 2`"

a=10
b=21

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
	echo "a=b"
fi	
if [ $a != $b ]
then
	echo "a!=b"
fi	

echo " "

if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
if [ $a -ne $b ]
then
   echo "$a -ne $b: a 不等于 b"
else
   echo "$a -ne $b : a 等于 b"
fi
if [ $a -gt $b ]
then
   echo "$a -gt $b: a 大于 b"
else
   echo "$a -gt $b: a 不大于 b"
fi
if [ $a -lt $b ]
then
   echo "$a -lt $b: a 小于 b"
else
   echo "$a -lt $b: a 不小于 b"
fi
if [ $a -ge $b ]
then
   echo "$a -ge $b: a 大于或等于 b"
else
   echo "$a -ge $b: a 小于 b"
fi
if [ $a -le $b ]
then
   echo "$a -le $b: a 小于或等于 b"
else
   echo "$a -le $b: a 大于 b"
fi


echo -e "\n"

if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a == $b: a 等于 b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a 小于 100 且 $b 大于 15 : 返回 true"
else
   echo "$a 小于 100 且 $b 大于 15 : 返回 false"
fi
if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a 小于 100 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 100 或 $b 大于 100 : 返回 false"
fi
if [ $a -lt 5 -o $b -gt 100 ]
then
   echo "$a 小于 5 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 5 或 $b 大于 100 : 返回 false"
fi

echo " [ expr1 -o expr2 ] = [[ expr1 || expr2 ]]"
echo " [ expr1 -a expr2 ] = [[ expr1 && expr2 ]]"


echo "characters operator"
a="abc"
b="edf"

if [ -z $a ] 
then
	echo " -z $a : 字符串长度为0"
else
	echo " -z $a : 字符串长度不为0"
fi

if [ -n $a ]
then
        echo " -n $a : 字符串长度不为0"
else
        echo " -n $a : 字符串长度为0"
fi

echo "File test operators"

file="./test.sh"

if [ -r $file ]
then
	echo "Readable"
else
	echo "Unreadable"
fi

echo "		[ -? \$file]
	-r Readability
	-w Writability
	-x Excutability
	-s Size > 0
	-e Existence
	-f Normal file
	-d Directory
	"
