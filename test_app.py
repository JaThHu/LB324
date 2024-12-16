import pytest
from app import app

# Teste die Route, die die Addition der Zahlen vornimmt
def test_addition():
    client = app.test_client()  # Erstelle einen Test-Client
    response = client.post('/add', data={'num1': '3', 'num2': '5'})
    assert response.status_code == 200
    assert b'Summe: 8' in response.data  # Überprüfe, dass die Antwort die richtige Summe enthält

# Teste die Fehlerbehandlung für ungültige Eingaben
def test_invalid_input():
    client = app.test_client()
    response = client.post('/add', data={'num1': 'a', 'num2': '5'})
    assert response.status_code == 400  # Fehler bei der Eingabe
    assert b'Invalid input' in response.data  # Überprüfe, dass eine Fehlernachricht ausgegeben wird
