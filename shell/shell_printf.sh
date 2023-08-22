#!/bin/bash

printf "Hello, here is tutorial of printf command\n"

printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg
printf "%-10s %-8s %-4.2f\n" Cj M 66.1223

printf "\n"

printf "\" and \' are the same.\n"
printf "%5d %5s\n" 1 "abc"
printf '%5d %5s\n' 1 'abc'

printf %s abc def

# only specify one format for parameters, extra parameters will still output the info in that format
printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j

printf "123\a 123\b 123\c 123\f 123\n"

printf "123\r123" 

printf "234\t234\t\n456\t3521\t\n"

printf "234\v234\v456\v3521\v"

