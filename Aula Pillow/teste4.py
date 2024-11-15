from PIL import Image, ImageEnhance

imagem = Image.open("imagem.jpg")
enhancer = ImageEnhance.Brightness(imagem)
imagem_brilho = enhancer.enhance(1.5)  # Aumenta o brilho
imagem_brilho.show()
