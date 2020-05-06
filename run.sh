#!bin/bash

if [ -n "$1" ]
    then
        python3 render.py $1.template
        open $1.html
        rm $1.html
else
    echo "No parameters found. Go for name of the file without extension. Ex:
    myCV"
fi