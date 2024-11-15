from PIL import Image

imagem = Image.open('imagem.jpg')

nova_imagem = imagem.rotate(180)

nova_imagem.show()