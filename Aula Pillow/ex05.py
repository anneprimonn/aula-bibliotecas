from PIL import Image

imagem = Image.open("imagem.jpg")

#imagem preto e branco
imagem_pb = imagem.convert("L")  # 'L' é o modo de imagem em escala de cinza

imagem_pb.show()
