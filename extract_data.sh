#!/usr/bin/bash

data=$(curl https://www.amfiindia.com/spages/NAVAll.txt)

readarray -t lines <<<"$data"

IFS=";"

for line in "${lines[@]}"
do
	if [[ $line == *";"* ]]
	then
		read -a words <<<"$line"
		echo ${words[3]},${words[4]}
	fi
done > dataset.csv
