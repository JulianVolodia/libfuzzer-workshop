#!/bin/bash

for i in `seq 1 20`;
do
echo "acknowledge" ;
./generate_testcases.py ;
./run_fuzzing.py | tee | grep -- "----";
if [[ $? -eq 0 ]];
then
echo yay; break;
else
echo ugh... ;
fi ;
echo -n "continue..." ;
sleep 1;
done
