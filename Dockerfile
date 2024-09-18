#imagem 
FROM python:3.9-slim

#diretorio
WORKDIR /app

#dependencia
COPY requirements.txt .

#instala
RUN pip install -r requirements.txt

#aplicação
COPY . .

#executar
CMD ["python", "app.py"] 