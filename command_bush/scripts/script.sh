#!/bin/bash

cd /c/cource_qa/TEST
cd homework
mkdir {11,22,33}
cd /c/cource_qa/TEST/homework/33
touch file11.txt file22.txt file33.txt file44.json file55.json
mkdir {11,22,33}
ls -la /c/cource_qa/TEST/homework
cd ..
cd /c/cource_qa/TEST/homework/33
mv file44.json file55.json /c/cource_qa/TEST/homework/22