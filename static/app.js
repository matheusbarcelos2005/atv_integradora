const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send-btn");
const responseSection = document.getElementById("response-section");
const responseContent = document.getElementById("response-content");
const errorSection = document.getElementById("error-section");
const errorMessage = document.getElementById("error-message");

sendButton.addEventListener("click", async () => {
    const message = messageInput.value.trim();
    
    // Esconde as seções de resposta e de erro antes de iniciar
    responseSection.classList.add("hidden");
    errorSection.classList.add("hidden");

    if (!message) {
        errorMessage.textContent = "Por favor, digite uma mensagem antes de enviar.";
        errorSection.classList.remove("hidden");
        return;
    }

    // Desabilita o botão enquanto envia
    sendButton.disabled = true;
    sendButton.textContent = "Enviando...";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json" 
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();

        if (response.ok) {
            responseContent.textContent = data.content;
            responseSection.classList.remove("hidden");
        } else {
            errorMessage.textContent = data.error || "Ocorreu um erro desconhecido.";
            errorSection.classList.remove("hidden");
        }
    } catch (err) {
        errorMessage.textContent = "Falha na conexão de rede ao enviar a mensagem.";
        errorSection.classList.remove("hidden");
    } finally {
        // Reabilita o botão
        sendButton.disabled = false;
        sendButton.textContent = "Enviar";
    }
});
