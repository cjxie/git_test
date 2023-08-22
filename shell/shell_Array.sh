#!/bin/bash

my_array=(A B "C" D)
for i in ${my_array[*]};
do
	echo ${i}
done

echo "4th element is ${my_array[3]}"


echo "关联数组(hash map)"

declare -A site=(["google"]="www.google.com" ["runoob"]="www.runoob.com" ["taobao"]="www.taobao.com")

echo ${site[*]}
echo "Keys of array: ${!site[*]}"
echo "# of elements: ${#site[*]}"
site["123"]="www.123.com"

echo ${site[@]}
echo "Keys of array: ${!site[@]}"
echo "# of elements: ${#site[@]}"
