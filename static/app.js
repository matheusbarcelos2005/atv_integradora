const promptInput = document.getElementById("prompt");
const sendButton = document.getElementById("send-btn");
const responseSection = document.getElementById("response-section");
const responseContent = document.getElementById("response-content");
const responseMeta = document.getElementById("response-meta");
const errorSection = document.getElementById("error-section");
const errorMessage = document.getElementById("error-message");

sendButton.addEventListener("click", handleSend);

async function handleSend() {
    const prompt = promptInput.value.trim();
    hideAll();

    if (!prompt) {
        showError("Digite um prompt antes de enviar.");
        return;
    }

    setLoading(true);
    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt }),
        });
        const data = await response.json();

        if (!response.ok) {
            showError(data.error || "Erro desconhecido.");
            return;
        }

        showResponse(data);
    } catch (err) {
        showError("Falha de rede ao enviar o prompt.");
    } finally {
        setLoading(false);
    }
}

function setLoading(loading) {
    sendButton.disabled = loading;
    sendButton.textContent = loading ? "Enviando..." : "Enviar";
}

function showResponse(data) {
    responseMeta.textContent = `Modelo: ${data.model} - Tokens: ${data.tokens_used}`;
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
