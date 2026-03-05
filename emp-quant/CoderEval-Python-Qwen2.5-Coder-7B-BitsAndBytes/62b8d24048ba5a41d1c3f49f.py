import functools
import time

class TTLCache(functools._lru_cache_wrapper):
    def __init__(self, maxsize, ttl, timer, typed):
        super().__init__(maxsize, typed)
        self.ttl = ttl
        self.timer = timer
        self.cache_info = functools.LRUCacheInfo(0, 0, maxsize, 0)

    def __getitem__(self, key):
        now = self.timer()
        while True:
            try:
                expire_time, result = self.cache[key]
                if now < expire_time:
                    return result
                del self.cache[key]
            except KeyError:
                break
        raise KeyError(key)

    def __setitem__(self, key, value):
        now = self.timer()
        expire_time = now + self.ttl
        self.cache[key] = (expire_time, value)
        self.cache_info.hits += 1

    def __delitem__(self, key):
        super().__delitem__(key)
        self.cache_info.misses += 1

    def clear(self):
        super().clear()
        self.cache_info.hits = 0
        self.cache_info.misses = 0

    @property
    def cache_info(self):
        return self._cache_info

    @cache_info.setter
    def cache_info(self, value):
        self._cache_info = value

ttl_cache = functools.lru_cache_factory(TTLCache)