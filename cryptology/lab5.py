
p = 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627  # 一个大素数
alpha = 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729  # 一个原根

def generate_private_key():
    import random
    return random.randint(1, p-2)

def calculate_public_key(private_key):
    return pow(alpha, private_key, p)

def calculate_shared_key(public_key, private_key):
    return pow(public_key, private_key, p)

alice_private_key = generate_private_key()
alice_public_key = calculate_public_key(alice_private_key)
print(f"Alice to Bob:: {alice_public_key}")

bob_private_key = generate_private_key()
bob_public_key = calculate_public_key(bob_private_key)
print(f"Bob to Alice:: {bob_public_key}")

alice_shared_key = calculate_shared_key(bob_public_key, alice_private_key)
print(f"Result (Alice view): {alice_shared_key}")

bob_shared_key = calculate_shared_key(alice_public_key, bob_private_key)
print(f"Result (Bob view): {bob_shared_key}")


