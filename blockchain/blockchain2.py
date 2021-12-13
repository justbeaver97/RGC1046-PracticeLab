# block을 만들자

from hashlib import sha256

blockchain = []

def make_AI_block():
    data = 'AI'
    prev_hash = b''
    current_hash = make_hash(data, prev_hash)
    blockchain.append((data,prev_hash,current_hash))
    return 0
    
def make_hash(data: str, prev_hash: bytes):
    return sha256(data.encode() + prev_hash).digest()

def add_block(data: str):
    _, _, prev_hash = blockchain[-1]
    current_hash = make_hash(data, prev_hash)
    blockchain.append((data, prev_hash, current_hash))
    
def show_blockchain():
    for i, (data, prev_hash, current_hash) in enumerate(blockchain):
        print(f'블록 {i}\n{data}\n{prev_hash.hex()}\n{current_hash.hex()}')

def verify_blockchain():
    for i in range(1, len(blockchain)):
        data, prev_hash, current_hash = blockchain[i]
        last_data, last_prev_hash, last_current_hash = blockchain[i-1]
        
        if prev_hash != last_current_hash:
            print(f"블록 {i} 이전 해시 != 블록 {i-1} 현 해시. \n"
                  f"{prev_hash.hex()} != \n {last_current_hash.hex()}")
            return False
        if last_current_hash != (temp := make_hash(last_data, last_prev_hash)):
            print(f"블록 {i-1} 검증 실패. \n"
                  f"{last_current_hash.hex()} != \n{temp.hex()}")
            return False
        if current_hash != (temp := make_hash(data, prev_hash)):
            print(f"블록 {i}, 검증 실패. \n"
                  f"{current_hash.hex()} != \n{temp.hex()}")
            return False
    return True

make_AI_block()
add_block("Artificial Intelligence")
add_block("in the")
add_block("Future Society")
show_blockchain()
print("\n",verify_blockchain())

# modify block1 
blockchain[1] = ('at the', blockchain[0][2], make_hash('at the', blockchain[0][2]))
show_blockchain()
print()
print(verify_blockchain())