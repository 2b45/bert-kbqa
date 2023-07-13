import os

# data/result

MODEL_PATH = "/data/workdir/models/bert-base-chinese/"
MODEL_NAME = os.path.join(MODEL_PATH, "pytorch_model.bin")
CONFIG_PATH = os.path.join(MODEL_PATH, "config.json")
VOB_PATH = os.path.join(MODEL_PATH, "vocab.txt")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 


NER_BERT_MODEL_PATH = os.path.join(PROJECT_DIR, "result", "best_ner.bin")
SIM_BERT_MODEL_PATH = os.path.join(PROJECT_DIR, "result", "best_sim.bin")
