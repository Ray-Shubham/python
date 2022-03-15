#!/bin/bash


if [ -e dummy.txt ]
then
git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/Ray-Shubham/python.git
else
echo "Not pushed"
fi
