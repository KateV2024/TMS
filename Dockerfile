FROM jenkins/jenkins:2.492.1-jdk17
USER root
# Обновляем пакеты и устанавливаем lsb-release
RUN apt-get update && apt-get install -y lsb-release
# Добавляем официальный GPG-ключ Docker
# Add the official Docker GPG key
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
    https://download.docker.com/linux/debian/gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
    https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && apt-get install -y docker-ce-cli
USER jenkins