# hash를 hash하자

from hashlib import sha256

prev_hash = b'AI'
for _ in range(3):
    print(prev_hash.hex())
    prev_hash = sha256(prev_hash).digest()
print(prev_hash.hex())