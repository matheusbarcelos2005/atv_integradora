const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send-btn");
const responseSection = document.getElementById("response-section");
const responseContent = document.getElementById("response-content");
const errorSection = document.getElementById("error-section");
const errorMessage = document.getElementById("error-message");

sendButton.addEventListener("click", handleSend);

async function handleSend() {
    const message = messageInput.value.trim();
    hideAll();

    if (!message) {
        showError("Digite uma mensagem antes de enviar.");
        return;
    }

    setLoading(true);
    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
        const data = await response.json();

        if (!response.ok) {
            showError(data.error || "Erro desconhecido.");
            return;
        }

        showResponse(data);
    } catch (err) {
        showError("Falha de rede ao enviar a mensagem.");
    } finally {
        setLoading(false);
    }
}

function setLoading(loading) {
    sendButton.disabled = loading;
    sendButton.textContent = loading ? "Enviando..." : "Enviar";
}

function showResponse(data) {
    responseContent.textContent = data.content;
    responseSection.classList.remove("hidden");
}

function showError(message) {
    errorMessage.textContent = message;
    errorSection.classList.remove("hidden");
}

function hideAll() {
    responseSection.classList.add("hidden");
    errorSection.classList.add("hidden");
}
