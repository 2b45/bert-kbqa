# bert-kbqa
- https://github.com/2b45/bert-kbqa/blob/pytorch/model/bert_lstm_crf.py


## 构造数据集

> 通过 1_split_data.py 切分数据
> 通过 2-construct_dataset_ner.py 构造命名实体识别的数据集
> 通过 3-construct_dataset_attribute.py 构造属性相似度的数据集
> 通过 4-print-seq-len.py 看看句子的长度
> 通过 5-triple_clean.py 构造干净的三元组
> 通过 6-load_dbdata.py 通过创建数据库 和 上传数据

## 模型准备

```
CRF_Model.py  条件随机场模型
BERT_CRF.py  bert+条件随机场
NER_main.py  训练命令实体识别的模型
SIM_main.py  训练属性相似度的模型
test_NER.py  测试命令实体识别
test_SIM.py 测试属性相似度
test_pro.py  测试整个项目
```

主要依赖版本：

torch.__version__    1.2.0

transformers.__version__   2.0.0


带有命令运行的py文件的命令都在 该py文件的最上方



## 操作

```
## 训练 ner
/usr/local/miniconda3/bin/python \
    ./ner_main.py \
    --data_dir ./data/ner_data/ \
    --vob_file /data/workdir/models/bert-base-chinese/vocab.txt \
    --model_config /data/workdir/models/bert-base-chinese/config.json \
    --pre_train_model /data/workdir/models/bert-base-chinese/pytorch_model.bin  \
    --output_dir ./data/result \
    --max_seq_length 64 \
    --do_train  \
    --train_batch_size 32   \
    --eval_batch_size 256 \
    --gradient_accumulation_steps 4 \
    --num_train_epochs 15


## sim main
/usr/local/miniconda3/bin/python \
    sim_main.py \
    --data_dir ./data/sim_data/ \
    --vob_file /data/workdir/models/bert-base-chinese/vocab.txt \
    --model_config /data/workdir/models/bert-base-chinese/config.json \
    --pre_train_model /data/workdir/models/bert-base-chinese/pytorch_model.bin  \
    --max_seq_length 64 \
    --do_train  \
    --train_batch_size 32   \
    --eval_batch_size 256   \
    --gradient_accumulation_steps 4 \
    --num_train_epochs 15

```
