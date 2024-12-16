# Schritt 1: Verwende ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Schritt 2: Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Schritt 3: Kopiere die Anforderungen-Datei in das Arbeitsverzeichnis
COPY requirements.txt /app/

# Schritt 4: Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Schritt 5: Kopiere den gesamten Code in den Container
COPY . /app/

# Schritt 6: Exponiere den Port, auf dem die Flask-App läuft
EXPOSE 5000

# Schritt 7: Definiere den Befehl zum Starten der Flask-App
CMD ["python", "app.py"]
