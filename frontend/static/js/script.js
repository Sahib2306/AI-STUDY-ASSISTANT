document.addEventListener("DOMContentLoaded", () => {
    const pdfUpload = document.getElementById("pdfUpload");
    if (pdfUpload) {
        pdfUpload.addEventListener("change", async (event) => {
            const file = event.target.files[0];
            if (!file) return;

            const chatBox = document.getElementById("chatBox");
            
            const loadingMsg = document.createElement("div");
            loadingMsg.classList.add("bot-message");
            loadingMsg.innerText = "⏳ Uploading and processing PDF...";
            chatBox.appendChild(loadingMsg);
            chatBox.scrollTop = chatBox.scrollHeight;

            const formData = new FormData();
            formData.append("file", file);

            try {
                const response = await fetch("http://127.0.0.1:5000/upload", {
                    method: "POST",
                    body: formData
                });
                const data = await response.json();
                
                if (response.ok) {
                    loadingMsg.innerText = "✅ " + data.message;
                } else {
                    loadingMsg.innerText = "❌ Error: " + data.error;
                }
            } catch (err) {
                loadingMsg.innerText = "❌ Upload failed: " + err.message;
            }
        });
    }
});

async function sendQuestion() {

    const input = document.getElementById("questionInput");
    const chatBox = document.getElementById("chatBox");

    const question = input.value.trim();

    if(question === "") return;

    // User Message

    const userMessage = document.createElement("div");

    userMessage.classList.add("user-message");

    userMessage.innerText = question;

    chatBox.appendChild(userMessage);

    input.value = "";

    // Loading Message

    const loadingMessage = document.createElement("div");

    loadingMessage.classList.add("bot-message");

    loadingMessage.innerText = "⏳ Thinking...";

    chatBox.appendChild(loadingMessage);

    chatBox.scrollTop = chatBox.scrollHeight;

    // API CALL

    try {
        const response = await fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();
        
        if (response.ok) {
            loadingMessage.innerText = "🤖 " + data.answer;
        } else {
            loadingMessage.innerText = "❌ " + (data.answer || data.error || "An error occurred");
        }
    } catch (err) {
        loadingMessage.innerText = "❌ Error connecting to server: " + err.message;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}