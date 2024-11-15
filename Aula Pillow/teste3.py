from PIL import Image, ImageEnhance

imagem = Image.open("imagem.jpg")
enhancer = ImageEnhance.Color(imagem)
imagem_saturada = enhancer.enhance(2.0)  # Aumenta a saturação
imagem_saturada.show()
