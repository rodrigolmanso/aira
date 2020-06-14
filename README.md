# Box

## Arquitetura
### Ferramentas
- **Docker** - <https://www.docker.com/>
- **Docker Compose** - <https://docs.docker.com/compose/>
- **Portainer (Container Docker)** - <https://portainer.readthedocs.io/en/stable/deployment.html#quick-start>
- **Python 3.8.3** - <https://www.python.org/downloads/>
- **RabbitMQ (Container Docker)** - <https://hub.docker.com/_/rabbitmq>
- **WinSCP** - <https://winscp.net/eng/download.php>
- **Putty** - <https://www.putty.org/>

### Pacotes Python
- **Flask v1.1.1** - <https://palletsprojects.com/p/flask/>
- **Vosk v0.3.8** - <https://github.com/alphacep/vosk/>
- **pyttsx3 v2.88** - <https://pypi.org/project/pyttsx3/>
- **PyAudio v0.2.11** - <https://pypi.org/project/PyAudio/>
- **NumPy v1.16.6** - <https://pypi.org/project/numpy/>
- **Pandas v1.0.4** - <https://pypi.org/project/pandas/>
- **Pika Python AMQP Client Library v1.1.0** - <https://pypi.org/project/pika/>
- **Joblib v0.14.1** - <https://pypi.org/project/joblib/>

## Componentes da Solução
### BoxApp
### API Servidor
### API Machine Learning
### Treinamento do Modelo de Machine Learning

## Instruções de Instalação Servidor
### Windows
- [Instalar o Docker Desktop](https://docs.docker.com/docker-for-windows/install/).
- Executar o comando `docker-compose up` dentro da pasta raiz do projeto, onde se encontra o arquivo **docker-compose.yml** e o docker irá subir o RabbitMQ, a API do Serviço e a API do Machine Lerning.

## Instruções de Instalação BoxApp
### Windows
- Instalar o [Python 3.8.3 ](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe).
- Caso não instale o PyAudio através do script de instalação automática, [faça o download do pacote](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) e instale manualmente usando o comando pip install + nome do pacote baixado de acordo com a versão do Windows e do Python conforme instruções na [thread do stackoverflow](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14).
- Clonar o projeto.
- Executar o comando `pip3 install -r requirements.txt` na pasta **box-app**.
- Executar o comando `python voice_app.py` na pasta **box-app**.
### Raspberry Pi 3
- [Instalar o Raspberry Pi OS no cartão SD](https://www.raspberrypi.org/downloads/).
- Executar o comando `sudo apt install libespeak-dev pulseaudio python-pyaudio python3-pyaudio -y` para instalar as dependências do linux.
- Clonar o projeto.
- Executar o comando `pip3 install -r requirements.txt` na pasta **box-app**.
- Executar o comando `python voice_app.py` na pasta **box-app**.

## Referências
- <https://github.com/alphacep/vosk>
- <https://cassota.gitlab.io/pt/#projects>
- <https://ufpafalabrasil.gitlab.io/>
- <https://github.com/synesthesiam/pt-br_pocketsphinx-cmu>
- <https://www.rabbitmq.com/tutorials/tutorial-one-python.html>
- <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>
- <https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14>