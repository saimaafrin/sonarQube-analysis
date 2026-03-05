from collections import Mapping

class MappingNode(Mapping):
    def __init__(self, *args, **kwargs):
        self._data = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    @staticmethod
    def _merge(a, b):
        if isinstance(a, Mapping) and isinstance(b, Mapping):
            return MappingNode({**a, **b})
        else:
            return b

    def merge(self, other):
        return MappingNode({k: self._merge(v, other[k]) for k, v in self.items()} | {k: other[k] for k in other.keys() - self.keys()})