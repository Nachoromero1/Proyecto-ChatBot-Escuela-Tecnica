async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const messages = document.getElementById("messages");

    if (!userMessage) return;

    const userMsgDiv = document.createElement("div");
    userMsgDiv.textContent = "Tú: " + userMessage;
    messages.appendChild(userMsgDiv);

    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();

        const botMsgDiv = document.createElement("div");
        botMsgDiv.textContent = "Bot: " + data.response;
        messages.appendChild(botMsgDiv);
    } catch (error) {
        console.error('Error al comunicarse con el servidor:', error);
    }

    document.getElementById('userMessage').value = "";
    messages.scrollTop = messages.scrollHeight;
}

document.getElementById("userMessage").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});
