import hashlib
import json
import time

# 验证交易的函数
def isValid(tx):
    balance = {}
    for input in tx['inputs']:
        if input['address'] not in balance or balance[input['address']] < input['amount']:
            return False
        balance[input['address']] -= input['amount']
    for output in tx['outputs']:
        if output['address'] not in balance:
            balance[output['address']] = 0
        balance[output['address']] += output['amount']
    return True

# 创建区块的函数
def create_block(previous_hash, transactions):
    block = {
        'index': len(blockchain) + 1,
        'timestamp': time.time(),
        'transactions': transactions,
        'proof': 0,  # 简单起见，这里不计算实际的proof
        'previous_hash': previous_hash
    }
    block['hash'] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
    return block

# 示例交易数据
transactions = [
    {'inputs': [{'address': 'Alice', 'amount': 5}], 'outputs': [{'address': 'Bob', 'amount': 5}]},
    {'inputs': [{'address': 'Bob', 'amount': 3}], 'outputs': [{'address': 'Alice', 'amount': 3}]}
]

# 创世区块
genesis_block = {
    'index': 1,
    'timestamp': time.time(),
    'transactions': [],
    'proof': 0,
    'previous_hash': '0',
    'hash': hashlib.sha256(json.dumps({
        'index': 1,
        'timestamp': time.time(),
        'transactions': [],
        'proof': 0,
        'previous_hash': '0'
    }, sort_keys=True).encode()).hexdigest()
}

# 区块链初始化
blockchain = [genesis_block]

# 验证交易并创建区块
valid_transactions = [tx for tx in transactions if isValid(tx)]
new_block = create_block(genesis_block['hash'], valid_transactions)

# 将新创建的区块添加到区块链中
blockchain.append(new_block)

# 打印区块链
for block in blockchain:
    print(json.dumps(block, indent=4))