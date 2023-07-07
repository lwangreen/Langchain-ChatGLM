from chinese_text_splitter import ChineseTextSplitter
from configs.model_config import SENTENCE_SIZE


class GKLocalChineseSplitter(ChineseTextSplitter):
    def __init__(self, pdf: bool = False, sentence_size: int = SENTENCE_SIZE, **kwargs):
        super.__init__(**kwargs)
    
        