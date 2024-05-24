async function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const userMessage = userInput.value.trim();

    if (userMessage === '') return;

    const userMessageElement = document.createElement('div');
    userMessageElement.className = 'chat-message user';
    userMessageElement.innerText = userMessage;
    chatBox.appendChild(userMessageElement);

    userInput.value = '';

    try {
        const response = await fetch('game/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: new URLSearchParams({
                'guess': userMessage
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        const botMessageElement = document.createElement('div');
        botMessageElement.className = 'chat-message bot';
        botMessageElement.innerText = data.message;
        chatBox.appendChild(botMessageElement);
        chatBox.scrollTop = chatBox.scrollHeight;

        if (data.status === 'success' || data.status === 'game_over') {
            userInput.disabled = true;
            userInput.placeholder = "Le jeu est terminé.";
        }
    } catch (error) {
        console.error('Erreur :', error);
    }
}

function checkEnter(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
