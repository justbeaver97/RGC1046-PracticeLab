import hashlib

h = hashlib.sha256()
h.update(b'AI')
print(h.hexdigest())