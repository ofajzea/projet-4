#!/bin/bash

conda create -n project_teledetection_03 python=3.11
conda activate project_teledetection_03
pip install -e .
python src/data_loading.py