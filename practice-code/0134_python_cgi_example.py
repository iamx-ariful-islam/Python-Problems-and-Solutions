import cgi

# send an HTTP header indicating the content type as HTML
print("Content-type: text/html\n\n")

print("<html><body style='text-align:center;'>")

print("<h1 style='color: green;'>Python < 3.13</h1>")

# parse form data submitted via the CGI script
form = cgi.FieldStorage()

# check if the "name" field is present in the form data
if form.getvalue("name"):
    # if present, retrieve the value and display a personalized greeting
    name = form.getvalue("name")
    print("<h2>Hello, " + name + "!</h2>")
    print("<p>Thank you for using our script.</p>")

# check if the "happy" checkbox is selected
if form.getvalue("happy"):
    print("<p>Yayy! We're happy too! ????</p>")

if form.getvalue("sad"):
    print("<p>Oh no! Why are you sad? ????</p>")

# close the HTML document
print("</body></html>")