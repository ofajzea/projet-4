#!/bin/bash

conda create -n project_teledetection_02 python=3.11
conda activate project_teledetection_02
pip install -e .
python src/data_loading.py