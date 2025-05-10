import secrets

token = secrets.token_hex(100) # you can use any number of hex token size

print(token)


'''output:

66c75879868a2fc2037c58b1c9ea93c8c540c0f2c9dcbefe641056a5172d1c4e9f020044c4b75e9025c9e0afed566d8592d9e25f26537326393af9e13e7cc35570f465d623950bb025866ed387ce0278b8171619e2ee7a9d7b2b52c778e6ff695d38fccb
'''