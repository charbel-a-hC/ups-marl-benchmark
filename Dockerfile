#FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime
#FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime
FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-runtime

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y software-properties-common

RUN apt-get install -y python3.7 \
    python3-pip \
    python3.7-venv \
    python3.7-dev \
    python3.7-distutils \
    curl \
    vim \
    git

# Adjust default python3 version to required version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
# Update pip3 version
RUN python3 -m pip install --upgrade pip

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=/root/.local/bin:$PATH
RUN poetry config virtualenvs.create false

WORKDIR /ups-marl-benchmark
COPY pyproject.toml .
COPY Makefile .
RUN make env-docker
