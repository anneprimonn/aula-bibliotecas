from PIL import Image

imagem = Image.open('imagem.jpg')

nova_imagem = imagem.resize((500, 500))

nova_imagem.show()