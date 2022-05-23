#!bin/bash

docker run -it --rm -v ${PWD}:/ups-marl-benchmark -p 8888:8888 ups-marl-benchmark
