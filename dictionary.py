class Dictionary:
    """思考エンジンの辞書クラス。

    クラス変数:
    DICT_RANDOM -- ランダム辞書のファイル名
    DICT_PATTERN -- パターン辞書のファイル名

    プロパティ:
    random -- ランダム辞書
    pattern -- パターン辞書
    """

    DICT_RANDOM = 'dics/random.txt'
    DICT_PATTERN = 'dics/pattern.txt'

    def __init__(self):
        """ファイルから辞書の読み込みを行う。"""
        with open(Dictionary.DICT_RANDOM, encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

        self._pattern = []
        with open(Dictionary.DICT_PATTERN, encoding='utf-8') as f:
            for line in f:
                pattern, phrases = line.strip().split('\t')
                if pattern and phrases:
                    self._pattern.append({'pattern': pattern,
                                          'phrases': phrases})

    @property
    def random(self):
        """ランダム辞書"""
        return self._random

    @property
    def pattern(self):
        """パターン辞書"""
        return self._pattern