#!/bin/zsh

function regenzshrc(){
    rm ~/.zshrc
    for filename in $(find ~/.zshrc.d/ -type f -name "*.zsh"| sort)
    do
        echo \#$(basename $filename) >> ~/.zshrc
        cat $filename >> ~/.zshrc
        echo >> ~/.zshrc 
    done
    echo regened zshrc
    source ~/.zshrc
}

if [ -e ~/.zshrc ];then
    rm ~/.zshrc
fi
regenzshrc
echo regened zshrc
source ~/.zshrc
