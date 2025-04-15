# Usa uma imagem base Python oficial com versão 3.9
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia primeiro o arquivo de requisitos para aproveitar o cache de camadas
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto para o container
COPY . .

# Expõe a porta que o Flask vai rodar (normalmente 5000)
EXPOSE 5000

# Comando para rodar a aplicação usando Gunicorn (produção)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
