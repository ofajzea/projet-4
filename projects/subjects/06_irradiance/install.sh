#!/bin/bash

if [ $# -eq 0 ];
  then
  token=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
elif [ $# -gt 0 ];
  then
  token=$1
else
  echo "Usage: source $0 <token>  OR source $0"
  exit 1
fi

conda create -n project_teledetection_06 python=3.11
conda activate project_teledetection_06
pip install -e .
export HUGGINGFACE_TOKEN=token
python src/data_loading.py