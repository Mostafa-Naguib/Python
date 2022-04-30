from PIL import Image

theImage = Image.open(r"C:\Users\moust\Desktop\Jerusalem.jpg")
theImage.show()


crop = (50, 50, 500, 500)
x = theImage.crop(crop)

x.show()

y = theImage.convert("L")
y.show()
