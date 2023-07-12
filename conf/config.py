# coding=utf-8
import os 
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BERT_MODEL_PATH = "/data/workdir/models/bert-base-chinese/"


class Config(object):
    def __init__(self):
        self.label_file = os.path.join(PROJECT_DIR, './data/tag.txt')
        self.train_file = os.path.join(PROJECT_DIR, './data/train.txt')
        self.dev_file = os.path.join(PROJECT_DIR, './data/dev.txt')
        self.test_file = os.path.join(PROJECT_DIR, './data/test.txt')

        self.vocab = os.path.join(BERT_MODEL_PATH, "vocab.txt")
        self.max_length = 300
        self.use_cuda = False
        self.gpu = 0
        self.batch_size = 50
        self.bert_path = BERT_MODEL_PATH
        self.rnn_hidden = 500
        self.bert_embedding = 768
        self.dropout1 = 0.5
        self.dropout_ratio = 0.5
        self.rnn_layer = 1
        self.lr = 0.0001
        self.lr_decay = 0.00001
        self.weight_decay = 0.00005
        self.checkpoint = os.path.join(BERT_MODEL_PATH, "result")
        self.optim = 'Adam'
        self.load_model = False
        self.load_path = None
        self.base_epoch = 100

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return '\n'.join(['%s:%s' % item for item in self.__dict__.items()])


if __name__ == '__main__':

    con = Config()
    con.update(gpu=8)
    print(con.gpu)
    print(con)
