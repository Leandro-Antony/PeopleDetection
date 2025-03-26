from ultralytics import YOLO

#Carrega um modelo
modelo = YOLO("yolo11n.pt")

#Treina o modelo
resultados_treino = modelo.train(
    data = "coco8.yaml", #caminho para o dataset
    epochs = 100, #número de treinos
    imgsz = 640, #tamanho da imagem
    device = "cpu" #dispositivo que vai rodar(device=0 or device=0,1,2,3 or device=cpu)
)

#Avalia a performance do modelo na configuração de validação
metricas = modelo.val()

#Pratica detecção de objetos em uma imagem
resultados = modelo(r"imgs\threepersons.jpeg")
resultados[0].show()

#Exporta o modelo como um arquivo ONNX (Open Neural Network Exchange)
path = modelo.export(format = "onnx")