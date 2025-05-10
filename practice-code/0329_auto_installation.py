import os


os.environ['MESA_GL_VERSION_OVERRIDE'] = '2.1'

# install necessary libraries in a single command
def install(packages):
    os.system(f"pip install --user {' '.join(packages)}")


# list of required packages for install
packages = ["hl7", "psutil", "pillow"]
install(packages)