from PIL import Image
image = Image.open("original.png")
image = image.resize((112,112),Image.ANTIALIAS)
image.save(fp="icon112.png")

image = image.resize((56,56),Image.ANTIALIAS)
image.save(fp="icon56.png")

image = image.resize((28,28),Image.ANTIALIAS)
image.save(fp="icon28.png")

image = image.resize((12,12),Image.ANTIALIAS)
image.save(fp="icon12.png")
