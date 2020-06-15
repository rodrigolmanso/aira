# AIRA - Artificial Intelligence for Remote Access
A AIRA é um dispositivo ativado por comando de voz.
Dotado de inteligência artificial, ela se conecta à rede de dados e é capaz de trazer informações ao motorista com um único comando.
Mais do que isso, a AIRA aprende conversando e interagindo com o motorista, mapeia suas preferências, tais como pontos de parada favoritos, rotas mais utilizadas e informações mais importantes para o motorista enquanto está no trecho.
Além disso, permite que o motorista tenha um parceiro digital, com quem pode interagir e registrar sua rotina e através da nossa IA aprendemos sobre essa rotina e apoiamos o motorista.

O AIRA nasceu a partir do Hackathon da CCR ocorrido entre os dias 12 e 14 de junho de 2020 e continua em desenvolvimento.

## O Problema
Segundo revista Exame, de 2008 a 2014 a frota de caminhões cresceu 5% ao ano, o dobro do ritmo do mercado de transportes. No período, as estradas brasileiras ganharam 770.000 novos caminhões com juros subsidiados. Segundo dados informados pela consultoria NTC & Logística durante a greve de 2018, o Brasil tem cerca de 2 milhões de caminhões em atividade, num excesso de 300.000 caminhões.
Na estrada, o caminhoneiro que corta o Brasil para transportar a carga tem enfrentado desafios que vão além de problemas mecânicos no veículo ou do tempo para entregar a mercadoria como problemas de saúdes, sono, segurança, entre outras. Desde o surgimento da pandemia, muitos desses profissionais foram contaminados ou mortos pela Covid-19, e seus problemas persistiram mesmo que a pandemia seja eliminada.
Dados inéditos de pesquisas feitas no ano passado por duas das maiores concessionárias de rodovias do País com milhares de caminhoneiros mostram que 79% deles estão com excesso de peso ou obesos (na população em geral, esse índice é de 72%), 35% têm colesterol e/ou glicemia em níveis elevados e um terço dorme seis horas ou menos por noite.
O trabalho do caminhoneiro é, muitas vezes, solitário. Com longas jornadas, longe de amigos e família, alguns sintomas de depressão podem surgir e trazer consigo diversos efeitos negativos para a saúde.Alguns dos sintomas possíveis são a ansiedade, mudanças frequentes de humor, perda de interesse ou prazer nas atividades, solidão, tristeza, irritabilidade, isolamento social, insônia, falta de concentração, abuso de substâncias, falta de apetite, entre outros.
Conhecendo essas dores e o nosso público criamos o Canvas.


## Equipe
- Adriana Walter  (https://www.linkedin.com/in/adrianawalter/)
- Luciana Rodrigues (https://www.linkedin.com/in/luciana-rodrigues-a8451aa3/)
- Rodrigo Luís Manso (https://www.linkedin.com/in/rodrigolmanso/)
- Zilceano Fonseca (https://www.linkedin.com/in/zilceano/)

## Recursos Adicionais
- [Confira nosso Pitch](https://github.com/rodrigolmanso/aira/blob/master/docs/Pitch%20-%20Hackathon%20CCR.pptx.pdf)
- [Business Model Canvas](https://github.com/rodrigolmanso/aira/blob/master/docs/Canvas.jpeg)
- [Matriz SWOT](https://github.com/rodrigolmanso/aira/blob/master/docs/Matriz%20SWOT.jpeg)
- [Acompanhe nosso canal no YouTube](https://www.youtube.com/channel/UCgg001IYpbgHg4oWtc-C5jQ)

![](https://github.com/rodrigolmanso/aira/blob/master/docs/Canvas.jpeg)
![](https://github.com/rodrigolmanso/aira/blob/master/docs/Matriz%20SWOT.jpeg)

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
### AIRA (IA de Comunicação)
Esse é o apliativo principal, o engine que faz a comunicação com a plataforma, grava e recupera informações offline, faz o reconhecimento de voz e a sintetização das respostas e envia alertas recebidos pela plataforma para o motorista.
Além disso, é o responsável por detectar uma frase de pânico e enviar um alerta em caso de assalto ou perigo para o motorista. Esse alerta é enviado silenciosamente, garantindo a segurança física do motorista.
Pode ser executado no Windows ou Raspberry Pi 3b. É possível utilizar em outras plataformas mediante ajustes na configuração.

### Info Consumer (Módulo de Inteligência)
Serviço que monitora a fila de informações do sistema. É o responsável por analisar as informações coletadas do veículo e informações fornecidas pelo motorista utilizando um modelo treinado de Machine Learning. Caso seja detectado um risco de acidente, este módulo envia para o motorista um alerta, solicitando que ele efetue uma parada para descanso.

### API Servidor
API REST que possibilita a integração entre o aplicativo mobile, portal e do engine de comunicação (AIRA).

### API Machine Learning
API REST que possibilita a integração dos diversos sitemas com os modelos de Machine Learning treinados.

### Portal
Portal contendo diversos dashboards e gráficos para acompanhamento dos dados coletados. [Clique aqui para visuaiizar o Portal em funcionamento](http://airaportal.com/airaportal/examples/index.html).

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
- Executar o comando `python aira_training_model.py` na pasta **training-model**

#### Treinamento do modelo usando o [COLAB](https://colab.research.google.com/)
Caso queira apenas visualizar os dados, acesse o [AIRA_Training_Model.ipynb diretamente no COLAB](https://colab.research.google.com/drive/1BbErRU33SPoHRKk_GlvjS4t2iuzJWHf-?usp=sharing).
- Abrir o arquivo **AIRA_Training_Model.ipynb** no [COLAB](https://colab.research.google.com/).
- Enviar os arquivos de suporte workflow.jpg, treinamento overview.jpg e aira_data.csv que estão na pasta **training-model**.
- Executar tudo.
- Será gerado um arquivo com o nome 'naive_bayes.joblib' contendo o dump do classificador Naive Bayes.

## Instruções de Instalação Servidor

### Windows
- [Instalar o Docker Desktop](https://docs.docker.com/docker-for-windows/install/).
- Executar o comando `docker-compose up` dentro da pasta raiz do projeto, onde se encontra o arquivo **docker-compose.yml** e o docker irá subir o RabbitMQ, a API do Serviço e a API do Machine Lerning.

## Instruções de Instalação AIRA

### Windows
- Instalar o [Python 3.8.3 ](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe).
- Caso não instale o PyAudio através do script de instalação automática, [faça o download do pacote](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) e instale manualmente usando o comando pip install + nome do pacote baixado de acordo com a versão do Windows e do Python conforme instruções na [thread do stackoverflow](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14).
- Clonar o projeto.
- Executar o comando `pip3 install -r requirements.txt` na pasta **aira-app**.
- Executar o comando `python voice_app.py` na pasta **aira-app**.

### Raspberry Pi 3
- [Instalar o Raspberry Pi OS no cartão SD](https://www.raspberrypi.org/downloads/).
- Executar o comando `sudo apt install libespeak-dev pulseaudio python-pyaudio python3-pyaudio -y` para instalar as dependências do linux.
- Clonar o projeto.
- Executar o comando `pip3 install -r requirements.txt` na pasta **aira-app**.
- Executar o comando `python voice_app.py` na pasta **aira-app**.
- __ATENÇÃO: É necessário possuir um microfone usb e uma caixa de som ligada na Raspberry para que o projeto seja executado corretamente__.

## Referências Técnicas
- <https://github.com/alphacep/vosk>
- <https://cassota.gitlab.io/pt/#projects>
- <https://ufpafalabrasil.gitlab.io/>
- <https://github.com/synesthesiam/pt-br_pocketsphinx-cmu>
- <https://www.rabbitmq.com/tutorials/tutorial-one-python.html>
- <https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world>
- <https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14>
- <https://www.generatedata.com/>
- <https://colab.research.google.com/>

## Referências de Negócio
- <https://exame.com/economia/o-brasil-tem-caminhoes-em-excesso-e-tera-ainda-mais/#:~:text=No%20per%C3%ADodo%2C%20as%20estradas%20brasileiras,num%20excesso%20de%20300.000%20caminh%C3%B5es.>
- <https://g1.globo.com/to/tocantins/noticia/2020/05/11/caminhoneiros-nao-param-durante-a-pandemia-e-24-sao-diagnosticados-com-covid-19-no-tocantins.ghtml>
- <https://www.em.com.br/app/noticia/economia/2018/06/03/internas_economia,964081/caminhoneiros-sofrem-com-saude-precaria.shtml>
- <http://www.automotivebusiness.com.br/abinteligencia/pdf/estudo_frota_completo.pdf>
- <https://www.automotivebusiness.com.br/noticia/29128/frota-circulante-passara-de-60-milhoes-em-2020>
- <http://avepbrasil.com.br/blog/saude-dos-caminhoneiros/>
