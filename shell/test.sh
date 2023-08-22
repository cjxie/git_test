#!/bin/bash
echo "Hello woooorld"


your_name="mala"
echo $your_name
echo ${your_name}


# loop
for skill in Ada Coffe Action Java; do
	echo "I am good at ${skill}Script"
done

# ReadOnly Variable
my_name="Cj"
# readonly my_name
my_name="Bb"

# Delete Variable
my_name="waibi"
unset my_name
echo $my_name


# String
str='abcd123'

echo $str

echo "length of str is ${#str}."

echo "extract part of the string is ${str:1:5}"

echo `expr index "$str" 123`


# Array in shell
array=(123 231 312)

array[3]=1234

echo "1st element in array: ${array[0]}"
echo "4th element in array: "${array[3]}""
echo "All elements: ${array[@]}"




:<<EOF
this note will be commented out
it will not be shown on the screen

EOF can be replaced by ' and !

EOF
