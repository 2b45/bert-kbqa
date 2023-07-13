import os


MODEL_PATH = "/data/workdir/models/bert-base-chinese/"

MODEL_NAME = os.path.join(MODEL_PATH, "pytorch_model.bin")
CONFIG_PATH = os.path.join(MODEL_PATH, "config.json")
VOB_PATH = os.path.join(MODEL_PATH, "vocab.txt")
