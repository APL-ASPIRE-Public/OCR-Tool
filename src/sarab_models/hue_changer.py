from PIL import Image, ImageEnhance

im = Image.open("/Users/singhs2/Downloads/blurry.jpg")
layer = Image.new('RGB', im.size, 'cyan') 
output = Image.blend(im, layer, 0.5)
output.save('output.jpg')
