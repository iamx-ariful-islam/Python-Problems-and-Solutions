# pip install redis

import redis


# connect to redis
client = redis.Redis(host='localhost', port=6379, db=0)

# increment the key 'unique_id' and get the new value
def generate_id():
    unique_id = client.incr('unique_id')
    return unique_id


# generate a new id
new_id = generate_id()
print(f'Generated ID: {new_id}')