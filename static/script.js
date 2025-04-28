async function enviarMensagem() {
    const input = document.getElementById("user-input");
    const erroDiv = document.getElementById("erro-mensagem");
    const mensagem = input.value.trim();

    if (!mensagem) {
        erroDiv.textContent = "Assim não, furioso! Digite uma mensagem antes de enviar.";
        input.style.border = "2px solid red";
        return;
    }

    erroDiv.textContent = "";
    input.style.border = "none";

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

document.getElementById("user-input").addEventListener("input", () => {
    document.getElementById("erro-mensagem").textContent = "";
    document.getElementById("user-input").style.border = "none";
});