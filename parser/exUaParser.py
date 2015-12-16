from logger.logger import Logger
from lxml import etree


class BaseParser(Logger, object):
    def __init__(self):
        super(BaseParser, self).__init__()
        self.__pool = {self.__class__.__name__: None}
        try:
            from lxml import etree
        except ImportError:
            self.logger.error('Coudn\'t import lxml-> etree library! Please install it!')
            return

    def __call__(self, *args, **kwargs):
        return self.__pool[self.__class__.__name__]

    def __getitem__(self, item):
        return self.__pool.get(item)

    def __setitem__(self, key, value):
        self.__pool[key] = value

    def parse(self, path, attrib, stream):
        _parser = etree.HTMLParser()
        _doc = etree.parse(stream, _parser)
        _local_list = []

        for item in _doc.findall(path):
            if item.text:
                try:
                    _text = item.text
                except UnicodeEncodeError:
                    self.logger.warning('Unicode cast problem! continue...')
                    continue

                self.logger.info(u'found item -> {}'.format(_text))
                _local_dict = {}
                for attr in attrib:
                    _local_dict.update({attr: item.attrib[attr]})

                _local_dict.update({'name': _text})
                _local_list.append(_local_dict)
        self.__pool[self.__class__.__name__] = _local_list


class ItemParser(BaseParser):
    def __init__(self):
        super(ItemParser, self).__init__()


class PageParser(BaseParser):
    def __init__(self):
        super(PageParser, self).__init__()


class CategoryParser(BaseParser):
    def __init__(self, stream=None):
        super(CategoryParser, self).__init__()
        self.category_regexp = '//table[@class="menu"]/tr/td[@class="menu_text"]/a'
        self.category_attribute = ['href']
        self._items = []
        self.stream = stream

    def __get_items(self):
        self.parse(path=self.category_regexp, attrib=self.category_attribute, stream=self.stream)
        self._items = self()
        return self._items

    @property
    def items(self):
        return self._items or self.__get_items()

