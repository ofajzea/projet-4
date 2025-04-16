#!/bin/bash

conda create -n project_teledetection_06 python=3.11
conda activate project_teledetection_06
pip install -e .
export HUGGINGFACE_TOKEN=$1
python src/data_loading.py