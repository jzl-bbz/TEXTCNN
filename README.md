# TEXTCNN
基于TextCNN对tnews_public集进行文本分类。

数据说明：  
  实验数据集 tnews_public 由笔者的实验指导人提供。该数据集包含 4 个 json 文件：labels.json、train.json、dev.json 和 test.json。labels.json 有 15 行记录，表示数据集中头条新闻的所有类别。另外三个文件用于模型的训练和测试，它们的结构一致，每行记录都包含 4 个字段，即标签号、标签描述、新闻标题和关键词。train 集包含 53360 条记录，dev 集包含 5000 条记录，test 集包含 5000 条记录。
  
训练：  
  python train.py --train --config cnn.ini

测试：  
  python test.py --config cnn.ini
