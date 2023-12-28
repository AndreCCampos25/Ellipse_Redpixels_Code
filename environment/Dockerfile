# hash:sha256:f36501613241c2152bb753de754db43823ee651242f3c69818b333db9e0ed598
FROM registry.codeocean.com/codeocean/miniconda3:4.9.2-cuda11.7.0-cudnn8-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ffmpeg=7:4.2.7-0ubuntu0.1 \
        libsm6=2:1.2.3-1 \
        libxext6=2:1.3.4-0ubuntu1 \
    && rm -rf /var/lib/apt/lists/*

RUN conda install -y \
        jupyter==1.0.0 \
    && conda clean -ya

RUN pip install -U --no-cache-dir \
    pip==23.3.2
RUN pip install -U --no-cache-dir \
    matplotlib==3.7.4 \
    numpy==1.24.4 \
    opencv-python==4.8.1.78 \
    scikit-learn==1.3.2 \
    scipy==1.10.1
