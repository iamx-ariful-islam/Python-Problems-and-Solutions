# pip install pillow

from PIL import Image


# funcation to create images file to pdf file
def images_to_pdf(filename, output_file_name):
    images = []
    for file in filename:
        img = Image.open(file)
        img = img.convert('RGB')
        images.append(img)

        # add all file into one file
        images[0].save(output_file_name, save_all=True, append_images=images[1:])


# call the function with parameters
images_to_pdf(['1.png', '2.png', '3.jpg'], 'output.pdf')