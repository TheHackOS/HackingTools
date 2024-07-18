# Etapa de construcción (builder image)
FROM ubuntu:20.04 AS builder-image

# Evitar que las instalaciones interactúen con el usuario
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3 python3-pip \  
  && rm -rf /var/lib/apt/lists/*

RUN apt-get install --no-install-recommends -y \
        curl \
        iputils-ping \
        iproute2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo y copiar los archivos necesarios
WORKDIR /app
COPY requirements.txt .

# Instalar dependencias Python usando pip
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al directorio de trabajo
COPY . .

