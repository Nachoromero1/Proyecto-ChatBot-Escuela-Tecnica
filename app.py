from flask import Flask, request, jsonify
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import random
from flask_cors import CORS
import nltk

# Descargar datos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

ps = PorterStemmer()  # Inicializar el PorterStemmer

# Definir las respuestas
responses = {
    "saludos": {
        "patterns": ["hola", "hello", "hi", "hey", "qué tal", "buenas"],
        "responses": ["¡Hola! ¿En qué puedo ayudarte?", "¡Hey! ¿Cómo andás?", "Hola, ¿cómo puedo asistirte hoy?"]
    },
    "programación": {
        "patterns": ["programación", "python", "javascript", "código", "coding"],
        "responses": [
            "Python es un excelente lenguaje de programación para principiantes y expertos.",
            "JavaScript se usa principalmente en el desarrollo web. ¿Te gustaría saber más?",
            "¿Necesitás ayuda con algún problema de código específico?"
        ]
    },
    "historia": {
        "patterns": ["historia", "history", "pasado", "histórico"],
        "responses": [
            "La Segunda Guerra Mundial tuvo lugar de 1939 a 1945.",
            "¿Sabías que la Revolución Francesa comenzó en 1789?",
            "La Primera Guerra Mundial fue de 1914 a 1918. ¿Querés saber algo más específico?"
        ]
    },
    "salud": {
        "patterns": ["salud", "health", "ejercicio", "bienestar"],
        "responses": [
            "Hacer ejercicio regularmente es esencial para la salud.",
            "Beber suficiente agua al día ayuda a mantener el cuerpo hidratado.",
            "Recuerda visitar al médico regularmente para un chequeo."
        ]
    },
    "entretenimiento": {
        "patterns": ["película", "movie", "entretenimiento", "música", "series"],
        "responses": [
            "Algunas de las series populares actualmente son 'The Witcher' y 'Stranger Things'.",
            "La película 'Inception' es un clásico moderno del cine de ciencia ficción.",
            "La música es una excelente forma de relajarse. ¿Te gusta algún género en particular?"
        ]
    },
    "expresiones_argentinas": {
        "patterns": ["che", "mate", "quilombo", "pibe", "mina", "boludo"],
        "responses": [
            "¡El mate es un clásico! Nada mejor para acompañar una charla.",
            "¿Sabías que 'quilombo' viene de la palabra para las comunidades de esclavos en Brasil?",
            "Ser 'boludo' depende de la situación, ¡pero a veces es un cumplido en Argentina!",
            "En Argentina, decimos 'pibe' o 'mina' para referirnos a chicos y chicas de manera coloquial."
        ]
    },
    "escuela_tecnica_monteros": {
        "patterns": ["escuela técnica", "escuela monteros", "tecnica monteros", "escuela n1 monteros"],
        "responses": [
            "La Escuela Técnica N°1 de Monteros es una institución educativa con especialidades en mecánica e informatica.",
            "En la Técnica N°1 de Monteros, los estudiantes aprenden tanto teoría como práctica en talleres especializados.",
            "La Escuela Técnica N°1 de Monteros es reconocida por formar técnicos con habilidades en mecánica, electricidad e informatica."
        ]
    },
    "cultura_argentina": {
        "patterns": ["fútbol", "asado", "empanadas", "alfajores", "tango"],
        "responses": [
            "El asado argentino es una tradición y una excusa perfecta para juntarse en familia o con amigos.",
            "El fútbol es casi una religión en Argentina. ¿Tenés algún equipo favorito?",
            "El tango es un género musical nacido en Buenos Aires, ¡ideal para quienes disfrutan bailar!",
            "Los alfajores son un clásico argentino. Si no los probaste aún, ¡te estás perdiendo de algo bueno!"
        ]
    },
    "despedida": {
        "patterns": ["adiós", "bye", "goodbye", "nos vemos", "chau"],
        "responses": ["¡Hasta luego!", "Adiós, ¡que tengas un buen día!", "Nos vemos, cuídate.", "Chau, ¡nos vemos la próxima!"]
    },
    "costumbres_locales": {
        "patterns": ["siesta", "mate", "fiesta", "costumbres argentinas"],
        "responses": [
            "La siesta es sagrada en muchas partes del país, especialmente después de un buen almuerzo.",
            "El mate es un ritual diario en Argentina, perfecto para acompañar cualquier conversación.",
            "Las fiestas en Argentina suelen empezar tarde y terminar a la madrugada. ¡Se pasa genial!",
            "Las costumbres argentinas están llenas de reuniones, asados, y mucha buena onda."
        ]
    }
}


import re

# Función para determinar la intención usando búsqueda con expresiones regulares
def get_intent(user_message):
    # Convertir el mensaje a minúsculas para hacer la búsqueda más consistente
    user_message = user_message.lower()

    # Buscar patrones en cada categoría
    for intent, data in responses.items():
        for pattern in data['patterns']:
            # Si el patrón está en el mensaje del usuario, devolver el intent
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_message):
                return intent
    return None

# Definir la ruta /chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', "")

    intent = get_intent(user_message)
    response = random.choice(responses[intent]['responses']) if intent else "Lo siento, no entiendo esa pregunta. ¿Podrías reformularla?"

    return jsonify({"response": response})

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
