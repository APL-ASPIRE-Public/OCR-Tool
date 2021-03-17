from pdf2image import convert_from_path
pages = convert_from_path('/Users/singhs2/Desktop/sample-pdf-file.pdf')

for page in pages:
    page.save('out.jpg', 'JPEG')