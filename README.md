# Bert-BiLSTM-CRF-pytorch


使用谷歌预训练bert做字嵌入的BiLSTM-CRF序列标注模型

本模型使用谷歌预训练bert模型（https://github.com/google-research/bert）， 
同时使用pytorch-pretrained-BERT (https://github.com/huggingface/pytorch-pretrained-BERT)

- SLTK [https://github.com/liu-nlper/SLTK](https://github.com/liu-nlper/SLTK)


准备数据格式参见data

模型参数可以在config中进行设置

运行代码

/usr/local/miniconda3/bin/python main.py train --use_cuda=False --batch_size=10  

pytorch.bin  百度网盘链接   链接:https://pan.baidu.com/s/160cvZXyR_qdAv801bDY2mQ 提取码:q67r 

作者也是新手，很希望看到的大家能够提意见，共同学习
