# ARIA - Artificial Intelligence for Remote Access

## Arquitetura
### Ferramentas
- **Docker** - <https://www.docker.com/>
- **Docker Compose** - <https://docs.docker.com/compose/>
- **Portainer (Container Docker)** - <https://portainer.readthedocs.io/en/stable/deployment.html#quick-start>
- **Python 3.8.3** - <https://www.python.org/downloads/>
- **RabbitMQ (Container Docker)** - <https://hub.docker.com/_/rabbitmq>
- **WinSCP** - <https://winscp.net/eng/download.php>
- **Putty** - <https://www.putty.org/>
- **Postman** - <https://www.postman.com/>

### Pacotes Python
- **Flask v1.1.1** - <https://palletsprojects.com/p/flask/>
- **Vosk v0.3.8** - <https://github.com/alphacep/vosk/>
- **pyttsx3 v2.88** - <https://pypi.org/project/pyttsx3/>
- **PyAudio v0.2.11** - <https://pypi.org/project/PyAudio/>
- **NumPy v1.16.6** - <https://pypi.org/project/numpy/>
- **Pandas v1.0.4** - <https://pypi.org/project/pandas/>
- **Pika Python AMQP Client Library v1.1.0** - <https://pypi.org/project/pika/>
- **Joblib v0.14.1** - <https://pypi.org/project/joblib/>
- **Retry v0.9.2** - <https://pypi.org/project/retry/>
- **SciKit Learn v0.22.2.post1** - <https://pypi.org/project/scikit-learn/>
- **SciKit Plot v0.3.7** - <https://pypi.org/project/scikit-plot/>
- **dfply v0.3.3** - <https://pypi.org/project/dfply/>
- **dtreeviz v0.8.2** - <https://pypi.org/project/dtreeviz/>
- **MatPlotLib v3.2.1** - <https://pypi.org/project/matplotlib/>
- **Seaborn v0.10.1** - <https://pypi.org/project/seaborn/>



## Componentes da Solução
### ARIA (IA de Comunicação)
Esse é o apliativo principal, o engine que faz a comunicação com a plataforma, grava e recupera informações offline, faz o reconhecimento de voz e a sintetização das respostas e envia alertas recebidos pela plataforma para o motorista.
Pode ser executado no Windows ou Raspberry Pi 3b. É possível utilizar em outras plataformas mediante ajustes na configuração.
### API Servidor
API REST que possibilita a integração entre o aplicativo mobile, portal e do engine de comunicação (ARIA).
### API Machine Learning
API REST que possibilita a integração dos diversos sitemas com os modelos de Machine Learning treinados.
### Treinamento do Modelo de Machine Learning
Como o modelo não temos base histórica, optamos por gerar dados fake através do site [generatedata.com](https://www.generatedata.com/), onde geramos dados fake para o Brasil na seguinte composição:
- hipertenso = Boolean (0 - 1)
- diabetico = Boolean (0 - 1)
- km_rodado_dia = Numeric Range (0 - 1000)
- media_horas_sono = Numeric Range (0 - 24)
- media_agua_diaria = Numeric Range (0 - 3)
- cigarros_fumados = Numeric Range (0 - 60)
- horas_descanso = Numeric Range (0 - 24)
- ansiedade_detectada = Boolean (0 - 1)
- latitude = Latitude/Longitude (latitude)
- longitude = Latitude/Longitude (longitude)
- acidente = Boolean (0 - 1)

#### Treinamento do modelo usando Python
- Executar o comando `pip3 install -r requirements.txt` para instalar as dependências.
- Executar o comando `python aria_training_model.py` na pasta **training-model**

#### Treinamento do modelo usando o [COLAB](https://colab.research.google.com/)
- Abrir o arquivo **ARIA_Training_Model.ipynb** no [COLAB](https://colab.research.google.com/).
- Enviar os arquivos de suporte workflow.jpg, treinamento overview.jpg e aria_data.csv que estão na pasta **training-model**.
- Executar tudo.
- Será gerado um arquivo com o nome 'naive_bayes.joblib' contendo o dump do classificador Naive Bayes.

## Instruções de Instalação Servidor
### Windows
- [Instalar o Docker Desktop](https://docs.docker.com/docker-for-windows/install/).
- Executar o comando `docker-compose up` dentro da pasta raiz do projeto, onde se encontra o arquivo **docker-compose.yml** e o docker irá subir o RabbitMQ, a API do Serviço e a API do Machine Lerning.

## Instruções de Instalação ARIA
### Windows
- Instalar o [Python 3.8.3 ](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe).
- Caso não instale o PyAudio através do script de instalação automática, [faça o download do pacote](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) e instale manualmente usando o comando pip install + nome do pacote baixado de acordo com a versão do Windows e do Python conforme instruções na [thread do stackoverflow](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14).
- Clonar o projeto.
- Executar o comando `pip3 install -r requirements.txt` na pasta **aria-app**.
- Executar o comando `python voice_app.py` na pasta **aria-app**.
### Raspberry Pi 3
- [Instalar o Raspberry Pi OS no cartão SD](https://www.raspberrypi.org/downloads/).
- Executar o comando `sudo apt install libespeak-dev pulseaudio python-pyaudio python3-pyaudio -y` para instalar as dependências do linux.
- Clonar o projeto.
- Executar o comando `pip3 install -r requirements.txt` na pasta **aria-app**.
- Executar o comando `python voice_app.py` na pasta **aria-app**.
- __ATENÇÃO: É necessário possuir um microfone usb e uma caixa de som ligada na Raspberry para que o projeto seja executado corretamente__.

## Referências
- <https://github.com/alphacep/vosk>
- <https://cassota.gitlab.io/pt/#projects>
- <https://ufpafalabrasil.gitlab.io/>
- <https://github.com/synesthesiam/pt-br_pocketsphinx-cmu>
- <https://www.rabbitmq.com/tutorials/tutorial-one-python.html>
- <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>
- <https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14>
- <https://www.generatedata.com/>
- <https://colab.research.google.com/>