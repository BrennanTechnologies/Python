    
"""Shuffle list x in place, and return None.

Optional argument random is a 0-argument function returning a
random float in [0.0, 1.0); if it is the default None, the
standard random.random will be used.

"""

randbelow = _randbelow
for i in reversed(range(1, len(x))):
	# pick an element in x[:i+1] with which to exchange x[i]
	j = randbelow(i + 1)
	x[i], x[j] = x[j], x[i]