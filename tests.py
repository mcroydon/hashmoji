from hashmoji import hashmoji, IncompatibleDigest, InvalidByteLength
import hashlib, unittest

class MockBadDigest(object):
	digest_size = -1
	def digest(self):
		pass

class HashmojiTestCase(unittest.TestCase):

	def test_basic(self):
		result = hashmoji(hashlib.sha1(b"This is my test string."))
		self.assertEqual(result, '📱 🔢 📩 🚦📲')

	def test_bytes(self):
		mybytes = b'\x916\xb8|\x1b\xf7&\xaa\x92(;OQX\x95^w\x1c\xb2\xd6\xbe\xb9_\x8b\xcf\xdcO\xa3\x8f\xcf\xdbq\x89\xd0\nF\xce1\x81\xca\xdd\x15\xf4\xe1\x10\x807\x19\x1b\x0f\xe8\x86\x08\xf7O\x19\xf1\x16\xf3\x93\x97\xfa{\x81'
		self.assertEqual(len(mybytes), 64)
		self.assertEqual(len(mybytes) % 4, 0)
		result = hashmoji(mybytes)
		self.assertEqual(result, '🏆 💙 🌀 🍒 🕕 🐯 💃 🎡 ⚡ 🔙 🚐 ➗ 🐟 ➡ 👍🏭')

	def test_bad_bytes(self):
		mybytes = b'\x001'
		self.assertRaises(InvalidByteLength, hashmoji, mybytes)

	def test_bad_digest(self):
		self.assertRaises(IncompatibleDigest, hashmoji, MockBadDigest())

def test_suite():
	suite = unittest.makeSuite(HashmojiTestCase)
	return suite

if __name__ == '__main__':
    unittest.main()
