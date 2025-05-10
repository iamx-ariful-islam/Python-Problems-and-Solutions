import hashlib


# encode the input string to bytes and hash using SHA-256
def generate_hash_id(input_string):
    sha256_hash = hashlib.sha256(input_string.encode()).hexdigest()
    return sha256_hash


# example usage
url     = 'https://example.come/some-page'
hash_id = generate_hash_id(url)
print(f'Hash-Based ID: {hash_id}')


'''output:

Hash-Based ID: df5f35dde822797469c877f6efb158a314cff68982ac601976bfea014bfb217b
'''