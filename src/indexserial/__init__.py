import os
from io import BytesIO

import torch


class IndexDumper:
    def __init__(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        self._f = open(filepath, 'wb')

    def dump(self, item) -> int:
        i = self._f.tell()
        torch.save(item, self._f)
        return i

    def dumpAll(self, ls: list) -> list:
        return [self.dump(i) for i in ls]

    def __del__(self):
        if not self._f.closed: self._f.close()


class IndexLoader:
    def __init__(self, filepath: str, index: list, device=None):
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = torch.device(device)

        self._index = sorted(set(index))
        self._f = filepath

    def load(self, i, toIndices=False):
        if toIndices: i = self._index.index(i)

        with open(self._f, 'rb') as f:
            f.seek(self._index[i])
            if i + 1 < len(self._index):
                buf = BytesIO(f.read(self._index[i + 1] - self._index[i]))
            else:
                buf = BytesIO(f.read())
            return torch.load(buf, self.device)

    def loadAll(self):
        with open(self._f, 'rb') as f:
            r = []
            for i in range(len(self._index)):
                if i + 1 < len(self._index):
                    buf = BytesIO(f.read(self._index[i + 1] - self._index[i]))
                else:
                    buf = BytesIO(f.read())
                r.append(torch.load(buf, self.device))
            return r


def indexDumpAll(ls, filepath) -> list:
    return IndexDumper(filepath).dumpAll(ls)


def indexLoadAll(filepath, index, device=None) -> list:
    return IndexLoader(filepath, index, device).loadAll()
