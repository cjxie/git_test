#!/bin/bash
:<<EOF
shell传递参数
EOF

echo "shell 传递参数实例"
echo "Excuteable file name: $0"
echo "1st parameter: $1"
echo "2nd parameter: $2"

separator="******************"
echo -e "\n${separator}"

echo "# of parameters: $#"
echo "传递的参数作为一个字符串显示<\$* or \$@>: $*"
echo -e "\n${separator}"

echo "-- \S* demo --"
for i in "$*";
do
	echo $i
done

echo "-- \S@ demo --"
for i in "$@";
do
        echo $i
done

echo -e "\n${separator}"
