def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	self.assertPending()
	self.assertEqual(self.lru.prev, self.lru.next)
	self.assertEqual(self.lru.prev, self.lru.next)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.assertEqual(self.lru.prev.prev, self.lru.next)
	self.assertEqual(self.lru.next.next, self.lru.prev)
	self.