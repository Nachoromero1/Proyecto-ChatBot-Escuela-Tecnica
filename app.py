from flask import Flask, request, jsonify
import random
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# Diccionario de intenciones y respuestas específico para la Escuela Técnica N°1 de Monteros
responses = {
    "historia_escuela": {
        "patterns": ["historia", "fundación", "fundada", "origen", "misión"],
        "responses": [
            "La Escuela Técnica N°1 de Monteros fue fundada en el año 1953, y desde entonces ha formado a generaciones de técnicos en diversas áreas.",
            "La misión de la Escuela Técnica N°1 de Monteros es ofrecer educación técnica de calidad, preparando a los estudiantes para enfrentar los desafíos del ámbito laboral y promover el desarrollo industrial de la región."
        ]
    },
    "especialidades": {
        "patterns": ["especialidades", "carreras", "ofrecen", "enseñan"],
        "responses": [
            "En la Escuela Técnica N°1 de Monteros, se imparten especialidades como Mecánica, Electrónica, Informática, y Electricidad, brindando una formación técnica integral.",
            "En la especialidad de Informática, los estudiantes aprenden programación, redes y desarrollo de software, además de realizar proyectos de desarrollo de aplicaciones y manejo de sistemas."
        ]
    },
    "instalaciones_talleres": {
        "patterns": ["instalaciones", "talleres", "laboratorios"],
        "responses": [
            "La Escuela Técnica N°1 de Monteros cuenta con talleres de última tecnología donde los estudiantes realizan prácticas de mecánica, electricidad y electrónica, permitiéndoles aplicar los conocimientos teóricos de forma práctica.",
            "Sí, la escuela tiene varios laboratorios de informática equipados con computadoras y herramientas de software modernas, donde los estudiantes practican programación, diseño gráfico y mantenimiento de redes."
        ]
    },
    "actividades_extracurriculares": {
        "patterns": ["actividades", "extracurriculares", "competiciones", "torneos"],
        "responses": [
            "La escuela ofrece actividades extracurriculares como clubes de robótica, torneos de matemáticas, ferias de ciencia y tecnología, y programas de extensión para que los estudiantes exploren sus intereses.",
            "Los estudiantes de la Escuela Técnica N°1 de Monteros participan en competiciones nacionales de robótica, olimpiadas de matemática y ferias de ciencias, donde han obtenido reconocimientos en varias ocasiones."
        ]
    },
    "docentes_comunidad": {
        "patterns": ["docentes", "profesores", "comunidad"],
        "responses": [
            "La Escuela Técnica N°1 de Monteros cuenta con docentes experimentados en cada especialidad, son reconocidos por su dedicación y experiencia en el área de la mecánica e informática.",
            "La comunidad de la Escuela Técnica N°1 de Monteros es unida y activa, con estudiantes y docentes comprometidos en el desarrollo académico y personal. Se organizan eventos donde participan alumnos, exalumnos y familias."
        ]
    },
    "vinculacion_industria": {
        "patterns": ["convenios", "empresas", "industria", "prácticas"],
        "responses": [
            "La Escuela Técnica N°1 de Monteros colabora con empresas locales e industrias, ofreciendo pasantías para que los estudiantes puedan adquirir experiencia práctica en el campo laboral.",
            "Los estudiantes realizan prácticas en empresas donde desarrollan proyectos reales, aplicando sus conocimientos en situaciones prácticas. Esto les permite estar mejor preparados para ingresar al mercado laboral."
        ]
    },
    "proyectos_logros": {
        "patterns": ["proyectos", "logros", "premios", "destacados"],
        "responses": [
            "Entre los proyectos destacados, los estudiantes han creado un sistema de automatización para talleres y un robot para competiciones. Estos logros muestran su creatividad y habilidades técnicas.",
            "La escuela ha recibido varios premios en olimpiadas de ciencias y tecnología. En 2022, un grupo de estudiantes ganó el primer lugar en la competencia de robótica nacional."
        ]
    }
    
    
}


def get_intent(user_message):   
    user_message = user_message.lower()
    for intent, data in responses.items():
        for pattern in data['patterns']:
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_message):
                return intent
    return None

def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent]["responses"])
    else:
        return "Lo siento, no entiendo esa pregunta. ¿Podrías reformularla?"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', "")
    intent = get_intent(user_message)
    response = get_response(intent)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
