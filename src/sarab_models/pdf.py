from pdf2image import convert_from_path
pages = convert_from_path('/Users/wyattja1/Downloads/tester.pdf')

for page in pages:
    page.save('out.jpg', 'JPEG')