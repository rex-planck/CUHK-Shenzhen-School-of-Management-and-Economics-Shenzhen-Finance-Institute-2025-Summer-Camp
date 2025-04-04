#date: 2024.9.26
#author：REXPLANCK
import hashlib

def hash_pair(left, right):
    return hashlib.sha256((left + right).encode()).hexdigest()

def build_merkle_tree(leaves):
    if len(leaves) % 2 != 0:
        leaves.append(leaves[-1])
    while len(leaves) > 1:
        temp = []
        for i in range(0, len(leaves), 2):
            temp.append(hash_pair(leaves[i], leaves[i+1]))
        leaves = temp
    return leaves[0]

leaves = [
    "R", "E", "X", "P", "L", "A", "N", "K"
]

leaves = [hashlib.sha256(leaf.encode()).hexdigest() for leaf in leaves]

merkle_root = build_merkle_tree(leaves)
print("Merkle Root:", merkle_root)