import base64


def ReadFile(fPath):
    fL = open(fPath, 'rb')
    data = fL.read()
    fL.close()
    return data
    
def WriteFile(fPath, data):
    fL = open(fPath, 'wb')
    fL.write(data)
    fL.close()

def test(fPath = 'google.png'):
    data = base64.b64encode(ReadFile(fPath) + '\n'.encode() + ReadFile('action_file.py'))
    WriteFile('google2.png', base64.b64decode(data))

test()