#!/bin/bash

conda create -n project_teledetection_05 python=3.11
conda activate project_teledetection_05
pip install -e .
export HUGGINGFACE_TOKEN=$1
python src/data_loading.py