import os
from argparse import ArgumentParser
from configparser import ConfigParser
import torch

# 和cnn.ini有关，继承了ConfigParse类，用到里面的方法和属性，最后这个Config可以像一个对象被使用（里面的参数）
class Config(ConfigParser):
    def __init__(self, config_file):
        raw_config = ConfigParser()
        raw_config.read(config_file)
        self.cast_values(raw_config)

    def cast_values(self, raw_config):
        for section in raw_config.sections():
            for key, value in raw_config.items(section):
                val = None
                if type(value) is str and value.startswith("[") and value.endswith("]"):
                    val = eval(value)
                    setattr(self, key, val)
                    continue
                for attr in ["getint", "getfloat", "getboolean"]:
                    try:
                        val = getattr(raw_config[section], attr)(key)
                        break
                    except:
                        val = value
                setattr(self, key, val)


def parse_config():
    parser = ArgumentParser(description="Text CNN")
    parser.add_argument('--config', dest='config', default='CONFIG')
    # action='store_true') # for debug
    parser.add_argument('--train', dest="train", action="store_true",default=False) # 稍微改了改，体会了ArgumentParser.--tyn
    # action='store_true') # for debug
    parser.add_argument('--test', dest="test", default=True)
    parser.add_argument('-v', '--verbose', default=False)

    # 获得运行程序时传入的参数
    args = parser.parse_args()
    print("args: ", args)
    config = Config(args.config)

    config.train = args.train   # True或False
    config.test = args.test     # True或False
    config.verbose = args.verbose   # False或True
    config.device = torch.device("cuda" if torch.cuda.is_available() and not config.no_cuda else "cpu") # "cuda"或"cpu"

    print(torch.cuda.is_available())

    return config   # 和上方的注释呼应

