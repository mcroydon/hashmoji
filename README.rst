========
Hashmoji
========

Hashmoji is a simple Python 3 program and library for visualizing content hashes as emoji.

About
=====

Hashmoji is really just an executable joke.  It is not intended to be secure or meet the needs of Serious
Business.  But it's fun alpha-quality stuff that you may enjoy.

Installation
============

Make sure you have `Python 3 <http://www.python.org/getit/>`_ installed.  On Mac OS X you can install
Python 3 via homebrew::

	brew update
	brew install python3

Once you have Python 3 installed you can clone this repository and install it::

	git clone git@github.com:mcroydon/hashmoji.git
	cd hashmoji
	python3 setup.py install

Or if you have `PIP <http://www.pip-installer.org/>`_ (recommended)::

	pip3 install hashmoji


You may also want to consider installing Hashmoji in a `Virtualenv <http://www.virtualenv.org/>`_.

Command-line usage
==================

Hashmoji ships as both an executable utility and as a Python module that you can use to visualize output from
`hashlib <http://docs.python.org/3/library/hashlib.html>`_ or any bytes object divisible by 4 bytes.

To use hashmoji similar to sha1sum::

	$ hashmoji.py README.rst 
	🐹 🌈 🆎 😊🔢

To see all available options, please run ``hashmoji.py --help``::

	$ hashmoji.py --help
	Usage: hashmoji.py [options] FILE

	Options:
  	--version             show program's version number and exit
  	-h, --help            show this help message and exit
  	-a ALGORITHM, --algorithm=ALGORITHM
                          Use ALGORITHM from hashlib.  Choices:
                          ['dsaEncryption', 'mdc2', 'ecdsa-with-SHA1', 'DSA-
                          SHA', 'SHA', 'SHA256', 'SHA512', 'sha384', 'SHA224',
                          'sha512', 'dsaWithSHA', 'sha1', 'ripemd160', 'MDC2',
                          'DSA', 'sha', 'RIPEMD160', 'sha256', 'SHA384', 'MD4',
                          'md5', 'sha224', 'md4', 'SHA1', 'MD5']
  	-t, --text            Read the file in text mode (default).
  	-b, --binary          Read the file in binary mode.
  	-e ENCODING, --encoding=ENCODING
                          Encoding to be used for text.  (default is utf-8)

You can use a specific hash algorithm based on the algorithms available to hashlib::

	$ hashmoji.py -a sha512 README.rst 
	👵 🚁 😮 🕞 🇩🇪 🔶 🌊 🚫 🎍 🔞 ✔ 🆚 🎁 🚜 🍢🎋

Hashmoji has only been tested on Mac OS X 10.8 in Terminal.app.  It definitely doesn't work inside a screen session.  Trust me.

Library usage
=============

Hashmoji is designed to work with either a bytes object or a `hashlib digest <http://docs.python.org/3/library/hashlib.html>`_::

	>>> from hashmoji import hashmoji
	
	# Use with hashlib
	>>> import hashlib
	>>> hashmoji(hashlib.sha1(b"This is my test string."))
	'📱 🔢 📩 🚦📲'

	# Use with bytes as long as the bytes are divisible by 4 bytes
	>>> mybytes = b'\x916\xb8|\x1b\xf7&\xaa\x92(;OQX\x95^w\x1c\xb2\xd6\xbe\xb9_\x8b\xcf\xdcO\xa3\x8f\xcf\xdbq\x89\xd0\nF\xce1\x81\xca\xdd\x15\xf4\xe1\x10\x807\x19\x1b\x0f\xe8\x86\x08\xf7O\x19\xf1\x16\xf3\x93\x97\xfa{\x81'
	>>> len(mybytes)
	64
	>>> len(mybytes) % 4
	0
	>>> hashmoji(mybytes)
	'🏆 💙 🌀 🍒 🕕 🐯 💃 🎡 ⚡ 🔙 🚐 ➗ 🐟 ➡ 👍🏭'

License
=======

Hashmoji is released under a 3-clause BSD license.
