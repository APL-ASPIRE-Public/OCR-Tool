from PIL import Image, ImageOps

def invert(image):     
  im = Image.open(image)
  im_invert = ImageOps.invert(im)
  im_invert.save('/Users/wyattja1/Downloads/digit_one_invert.jpg', quality=95)
invert('/Users/wyattja1/Desktop/OCR-Tool/src/josh_models/Handwritten_Digits/digit_one.jpg')