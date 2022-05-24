#!bin/bash

docker run -it --rm --gpus=all -v ${PWD}:/ups-marl-benchmark -p 8888:8888 ups-marl-benchmark
