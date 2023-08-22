#!/bin/bash

# shell function

<<EOF
[ function ] funname [()]

{

	action;
	
	[return int;]

}
EOF

demoFun()
{
	echo "my first shell function"	
}

echo "-----Start Function-----"
demoFun
echo "-----Function Done-----"


# Use $? toget the last return from function
funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $[aNum+anotherNum]
}
funWithReturn
echo "The sum of two inputs is $?"


# 向函数内部传递参数，通过$n的形式来获取参数的数值， !! n>=10, must use ${n}来获取参数.
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 ! --- not true"
    echo "第十个参数为 ${10} ! --- "
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个! --- {\$#}"
    echo "作为一个字符串输出所有参数 $* ! --- {\$*}"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
