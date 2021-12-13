# PoW을 만들자

from hashlib import sha256

blockchain = []
difficulty = 4

def add_AI_block():
    data = 'AI'
    prev_hash = ''
    nonce, current_hash = make_hash(data, prev_hash, difficulty)
    blockchain.append((data,prev_hash,difficulty, nonce, current_hash))
    return 0
    
def make_hash(data: str, prev_hash: bytes, difficulty_: int):
    new_hash = ' ' * difficulty_
    checker = '0' * difficulty_
    nonce = 0
    while new_hash[:difficulty_] != checker:
        new_hash = sha256((data + str(nonce) + prev_hash).encode()).hexdigest()
        nonce += 1 
    return nonce, new_hash

def add_block(data, prev_hash, difficulty_, nonce, current_hash):
    blockchain.append((data, prev_hash, difficulty_, nonce, current_hash))
    
def add_normal_block(data: str):
    _, _, _, _, prev_hash = blockchain[-1]
    nonce, current_hash = make_hash(data, prev_hash, difficulty)
    add_block(data, prev_hash, difficulty, nonce, current_hash)
    
def show_blockchain():
    for i, (data, prev_hash, difficulty_, nonce, current_hash) in enumerate(blockchain):
        print(f'블록 {i}\n'
              f'{data}, {difficulty_}, {nonce}\n'
              f'{prev_hash}\n'
              f'{current_hash}')

def verify_blockchain():
    for i in range(1, len(blockchain)):
        data, prev_hash, difficulty_, nonce, current_hash = blockchain[i]
        last_data, last_prev_hash, last_difficulty, last_nonce, last_current_hash = blockchain[i-1]
        
        if prev_hash != last_current_hash:
            print(f"블록 {i} 이전 해시 != 블록 {i-1} 현 해시. \n"
                  f"{prev_hash} != \n {last_current_hash}")
            return False
        if (last_nonce, last_current_hash) != (temp := make_hash(last_data, last_prev_hash, last_difficulty)):
            show_verify_failed(i-1, last_nonce, last_current_hash, temp[0], temp[1])
            return False
        if (nonce, current_hash) != (temp := make_hash(data, prev_hash, difficulty_)):
            show_verify_failed(i, nonce, current_hash, temp[0], temp[1])
            return False
    return True

def show_verify_failed(block_num, ori_nonce, ori_hash, new_nonce, new_hash):
    print(f"블록 {block_num} 검증 실패 \n"
          f"{ori_nonce} != {new_nonce} \n"
          f"{ori_hash} != \n{new_hash}")

add_AI_block()
add_normal_block("Artificial Intelligence")
add_normal_block("in the")
add_normal_block("Future Society")
show_blockchain()
print()
print(verify_blockchain())

# modify block1 
blockchain[1] = ('at the', blockchain[0][4],blockchain[0][2], *make_hash('at the', blockchain[0][4], blockchain[0][2]))
show_blockchain()
print()
print(verify_blockchain())