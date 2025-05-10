# pip install pillow

from PIL import Image


inp_flName = 'input_file.jpg' # Enter input file name
out_flName = 'output_file.png' # Enter output file name

ImgFL = Image.open(inp_flName)
rgba  = ImgFL.convert("RGBA")
datas = rgba.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0: newData.append((255, 255, 255))
    elif item[0] == 255 and item[1] == 255 and item[2] == 255: newData.append((0, 0, 0)) 
    else: newData.append(item)
rgba.putdata(newData)
rgba.save(out_flName, "PNG")