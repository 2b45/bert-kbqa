import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

# data/result
TRIPLE_DIR = os.path.join(PROJECT_DIR, "data", "DB_Data/clean_triple.csv")


MODEL_PATH = "/data/workdir/models/bert-base-chinese/"
MODEL_NAME = os.path.join(MODEL_PATH, "pytorch_model.bin")
CONFIG_PATH = os.path.join(MODEL_PATH, "config.json")
VOB_PATH = os.path.join(MODEL_PATH, "vocab.txt")


NER_BERT_MODEL_PATH = os.path.join(PROJECT_DIR, "data/result", "best_ner.bin")
SIM_BERT_MODEL_PATH = os.path.join(PROJECT_DIR, "data/result", "best_sim.bin")


