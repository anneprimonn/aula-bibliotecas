from PIL import Image, ImageFilter

imagem = Image.open("imagem.jpg")

imagem_desfocada = imagem.filter(ImageFilter.BLUR)

imagem_desfocada.show()
