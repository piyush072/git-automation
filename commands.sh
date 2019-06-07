#!/bin/bash

function create(){
  mkdir $1
  cd $1
  username="username"
  python create.py $1
  git init
  echo "# "$1" #">>readme.md
  git add .
  git remote add origin "https://github.com/$username/$1"
  git commit -m "intital commit"
  git push -u origin master
}
