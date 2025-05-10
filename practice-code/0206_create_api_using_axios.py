# pip install axios

import axios

api = axios.create(
    {
        'baseURL': '/api',
        'headers': {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
    },
)

print(api)