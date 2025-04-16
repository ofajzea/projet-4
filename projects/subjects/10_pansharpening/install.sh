#!/bin/bash

conda create -n project_teledetection_10 python=3.11
conda activate project_teledetection_10
pip install -e .
python src/data_loading.py