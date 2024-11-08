// Función para enviar el mensaje
async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const messages = document.getElementById("messages");

    if (!userMessage) return;

    // Añadir el mensaje del usuario en la ventana de mensajes
    const userMsgDiv = document.createElement("div");
    userMsgDiv.textContent = "Tú: " + userMessage;
    messages.appendChild(userMsgDiv);

    // Enviar el mensaje al backend
    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();

        // Mostrar la respuesta del bot
        const botMsgDiv = document.createElement("div");
        botMsgDiv.textContent = "Bot: " + data.response;
        messages.appendChild(botMsgDiv);
    } catch (error) {
        console.error('Error al comunicarse con el servidor:', error);
    }

    // Limpiar el campo de entrada
    document.getElementById('userMessage').value = "";
    messages.scrollTop = messages.scrollHeight;
}

// Función para detectar si se presiona la tecla "Enter"
document.getElementById("userMessage").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();  // Prevenir el salto de línea por defecto
        sendMessage();
    }
});
