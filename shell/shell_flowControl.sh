#!/bin/bash

ct=1
for i in $*
do
	echo "Input$ct is $i"
	# ct++
	ct=$[ct + 1]

done

int=1
while(( $int<=5 ))
do
    echo $int
    let int++
done

echo '按下 <CTRL-D> 退出'
echo -n '输入你最喜欢的网站名: '
while read FILM
do
    echo "是的！$FILM 是一个好网站"
done


# case (switch)
echo "Enter a num in between 1 and 5"
read num
case $num in
	1|2|3|4|5) echo "input is $num"
	;;
	*) echo "input is gt 5 and lt 1"
	;;
esac


