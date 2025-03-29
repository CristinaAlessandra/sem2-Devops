FROM python:3

WORKDIR /usr/src/app

# Copiar o requirements.txt e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

EXPOSE 80
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
