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

action_endpoint:
  url: "http://localhost:5055/webhook"

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

## Output 
Im Folgenden sehen Sie ein Beispiel des Outputs dieses Chatbot-Gesprächs. Diese Darstellung zeigt, wie der Chatbot auf Benutzeranfragen mit Informationen zu medizinischen Diagnosen antwortet:
<img width="863" alt="Screenshot 2023-12-04 132323" src="https://github.com/itsmeeeeeee/chatbot_rasa/assets/96257594/d5df5979-adfc-4e01-9012-f1a905171c04">

## Ergebnisse

Rasa-Chatbot verwendet den DIET Classifier für die Intent-Erkennung und Entitätenextraktion. Die Leistung des Classifiers wurde ausführlich bewertet und die Ergebnisse sind im Detail in der Datei results/DIETClassifier_report.json festgehalten.  Die erzielte Accuracy liegt bei 97.07%

## Referenzen

1. Kaggle Disease Symptom Description Dataset: [src](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=symptom_Description.csv)
2. Towards Data Science Artikel über Rasa 2.0: [src](https://towardsdatascience.com/chatbots-made-easier-with-rasa-2-0-b999323cdde)
