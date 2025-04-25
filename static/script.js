async function enviarMensagem() {
    const input = document.getElementById("user-input");
    const mensagem = input.value;

    const resposta = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: mensagem})
    });

    const dados = await resposta.json();

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>Você:</strong> ${mensagem}</p>`;
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${dados.response}</p>`;

    input.value = '';
}