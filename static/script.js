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
    chatBox.innerHTML += `<div class="mensagem usuario"> ${mensagem} </div><br>`;
    chatBox.innerHTML += `<div class="mensagem bot"> ${dados.response} </div><br>`;

    input.value = '';
    
    chatBox.scrollTop = chatBox.scrollHeight;
}

function verificaEnter(event) {
    if (event.key === "Enter") {
        enviarMensagem();
    }
}