#!/bin/bash

function create(){

  python create.py $1 $2
  username="test"
  password="test"
  cd
  mkdir $1
  cd $1
  git init
  echo "# "$1" #">>README.md
  git add .
  git remote add origin "https://$username:$password@github.com/$username/$1"
  # if you have @ in the username or password then replace the above line with- git remote add origin "https://github.com/$username/$1"
  git commit -m "intital commit"
  git push -u origin master
}
