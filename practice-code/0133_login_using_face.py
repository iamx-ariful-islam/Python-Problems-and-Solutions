# pip install pycgi
# pip install face-recognition

import cgi
from base64 import b64decode
import face_recognition


form_data  = cgi.FieldStorage()
face_match = 0

image    = form_data.getvalue('current_image')
email    = form_data.getvalue('email')
data_url = image

header, encoded = data_url.split(',', 1)
data = b64decode(encoded)

with open('image.png', 'wb') as file:
    file.write(data)
    
got_image = face_recognition.load_image_file('image.png')
existing_image = face_recognition.load_image_file('students/'+email+'.jpg')
got_image_facialfeatures = face_recognition.face_encodings(got_image)[0]

existing_image_faceialfeatures = face_recognition.face_encodings(existing_image)[0]

result = face_recognition.compare_faces([existing_image_faceialfeatures, got_image_facialfeatures])
face_match = 1 if result[0] else 0

print('Content-type: text/html')
print()


if face_match: print("<script>alert('welcome ", email, " ')</script>")
else: print("<script>alert('face not recognized')</script>")