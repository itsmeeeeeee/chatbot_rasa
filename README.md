# Rasa Chatbot für medizinische Diagnosen

## Überblick
Dieser Chatbot wurde mithilfe von Rasa implementiert und mit einem spezialisierten Datensatz für medizinische Diagnosen erweitert. Der Datensatz, der von Kaggle bezogen wurde, enthält 40 Diagnosen mit entsprechenden Erklärungen.

## Wichtige Dateien

### Python-Skript für die Krankheitsbeschreibung (actions.py)
`ActionProvideDiseaseInfo` ist eine benutzerdefinierte Aktion in Python für den Rasa-Chatbot. Diese Klasse ermöglicht es dem Chatbot, Informationen über verschiedene Krankheiten bereitzustellen. Sie liest die Krankheitsbeschreibungen aus einer CSV-Datei und gibt die entsprechenden Informationen aus, wenn sie über den Dialogfluss des Chatbots aufgerufen wird.

### NLU und Story und Rules-Dateien
- **NLU-Datei (nlu.yml):** Hier werden Intents, Entities und Trainingsbeispiele für das NLU-Modell definiert.

- **Story-Datei (stories.yml):** Enthält die Dialogmuster, die der Chatbot für das Training des Dialogmanagementmodells verwendet.

- **Rules-Datei (rules.yml):** Definiert Regeln für den Chatbot, um bestimmte Aktionen unter spezifischen Bedingungen auszuführen.

### Domain-Datei (domain.yml)

Die Domain-Datei wurde erweitert, um die Krankheitsentitäten und die benutzerdefinierte Aktion `action_provide_disease_info` zu umfassen.

### Endpoints.yml
Die `endpoints.yml`-Datei wurde konfiguriert, um die Verbindung zum Action-Server herzustellen. Sie enthält die Zeile:
```
action_endpoint:
  url: "http://localhost:5055/webhook"
```

## Ausführung des bereitgestellten Chatbots

### Schritt 1: Ausführen des Action Servers
1. Öffnen Sie das Anaconda Prompt.
2. Navigieren Sie zum richtigen Verzeichnis Ihres Projekts.
3. Aktivieren Sie die Rasa-Umgebung mit `conda activate rasa_bot`.
4. Starten Sie den Action Server mit `rasa run actions`.

### Schritt 2: Training und Ausführung des Chatbots
1. Öffnen Sie ein neues Anaconda Prompt-Fenster.
2. Navigieren Sie erneut zum Projektverzeichnis.
3. Aktivieren Sie die Rasa-Umgebung mit `conda activate rasa_bot`.
4. Trainieren Sie den Chatbot mit `rasa train`.
5. Starten Sie den Chatbot mit `rasa shell` für eine interaktive Sitzung.

## Requirements 
Hier folgt eine Liste der erforderlichen Python-Pakete und deren Versionen, die für die Ausführung dieses Chatbots notwendig sind. Diese können mittels `pip install -r requirements.txt` installiert werden:

absl-py==1.4.0
aio-pika==8.2.3
aiofiles==23.2.1
aiogram==2.25.2
aiohttp==3.8.6
aiohttp-retry==2.8.3
aiormq==6.4.2
aiosignal==1.3.1
APScheduler==3.9.1.post1
astunparse==1.6.3
async-timeout==4.0.3
attrs==22.1.0
Babel==2.9.1
bidict==0.22.1
boto3==1.33.2
botocore==1.33.2
CacheControl==0.12.14
cachetools==5.3.2
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
cloudpickle==2.2.1
colorama==0.4.6
colorclass==2.2.2
coloredlogs==15.0.1
colorhash==1.2.1
confluent-kafka==2.3.0
cryptography==41.0.7
cycler==0.12.1
dask==2022.10.2
dnspython==2.3.0
docopt==0.6.2
fbmessenger==6.0.0
fire==0.5.0
flatbuffers==23.5.26
fonttools==4.45.1
frozenlist==1.4.0
fsspec==2023.10.0
future==0.18.3
gast==0.4.0
google-auth==2.23.4
google-auth-oauthlib==1.0.0
google-pasta==0.2.0
greenlet==3.0.1
grpcio==1.59.3
h11==0.14.0
h5py==3.10.0
httptools==0.6.1
humanfriendly==10.0
idna==3.6
importlib-metadata==6.8.0
jax==0.4.20
jmespath==1.0.1
joblib==1.2.0
jsonpickle==3.0.2
jsonschema==4.17.3
keras==2.12.0
kiwisolver==1.4.5
libclang==16.0.6
locket==1.0.0
magic-filter==1.0.12
Markdown==3.5.1
MarkupSafe==2.1.3
matplotlib==3.5.3
mattermostwrapper==2.2
ml-dtypes==0.3.1
msgpack==1.0.7
multidict==5.2.0
networkx==2.6.3
numpy==1.23.5
oauthlib==3.2.2
opt-einsum==3.3.0
packaging==20.9
pamqp==3.2.1
partd==1.4.1
Pillow==10.1.0
pluggy==1.3.0
portalocker==2.8.2
prompt-toolkit==3.0.28
protobuf==4.23.3
psycopg2-binary==2.9.9
pyasn1==0.5.1
pyasn1-modules==0.3.0
pycparser==2.21
pydantic==1.10.9
pydot==1.4.2
PyJWT==2.8.0
pykwalify==1.8.0
pymongo==4.3.3
pyparsing==3.1.1
pyreadline3==3.4.1
pyrsistent==0.20.0
python-crfsuite==0.9.9
python-dateutil==2.8.2
python-engineio==4.8.0
python-socketio==5.10.0
pytz==2022.7.1
pywin32==306
PyYAML==6.0.1
questionary==1.10.0
randomname==0.1.5
rasa==3.6.14
rasa-sdk==3.6.2
redis==4.6.0
regex==2022.10.31
requests==2.31.0
requests-oauthlib==1.3.1
requests-toolbelt==1.0.0
rocketchat-API==1.30.0
rsa==4.9
ruamel.yaml==0.17.21
ruamel.yaml.clib==0.2.8
s3transfer==0.8.1
sanic==21.12.2
Sanic-Cors==2.0.1
sanic-jwt==1.8.0
sanic-routing==0.7.2
scikit-learn==1.1.3
scipy==1.11.4
sentry-sdk==1.14.0
simple-websocket==1.0.0
six==1.16.0
sklearn-crfsuite==0.3.6
slack-sdk==3.26.0
SQLAlchemy==1.4.50
structlog==23.2.0
structlog-sentry==2.0.3
tabulate==0.9.0
tarsafe==0.0.4
tensorboard==2.12.3
tensorboard-data-server==0.7.2
tensorflow==2.12.0
tensorflow-estimator==2.12.0
tensorflow-hub==0.13.0
tensorflow-intel==2.12.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==2.3.0
terminaltables==3.1.10
threadpoolctl==3.2.0
toolz==0.12.0
tqdm==4.66.1
twilio==8.2.2
typing-utils==0.1.0
typing_extensions==4.8.0
tzdata==2023.3
tzlocal==5.2
ujson==5.8.0
urllib3==1.26.18
wcwidth==0.2.12
webexteamssdk==1.6.1
websockets==10.4
Werkzeug==3.0.1
wrapt==1.14.1
wsproto==1.2.0
yarl==1.9.3
zipp==3.17.0

## Output: hier wird der Output von Chat gespräch dargestellt
<img width="863" alt="Screenshot 2023-12-04 132323" src="https://github.com/itsmeeeeeee/chatbot_rasa/assets/96257594/568747d0-70f5-403f-b18e-7dd6df17fdf0">

## Referenzen

1. Kaggle Disease Symptom Description Dataset: [Kaggle Disease Symptom Description Dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=symptom_Description.csv)
2. Towards Data Science Artikel über Rasa 2.0: [Towards Data Science Artikel über Rasa 2.0](https://towardsdatascience.com/chatbots-made-easier-with-rasa-2-0-b999323cdde)
