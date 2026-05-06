function sendQuestion() {

    const input = document.getElementById("questionInput");
    const chatBox = document.getElementById("chatBox");

    const question = input.value.trim();

    if(question === "") return;

    // User Message

    const userMessage = document.createElement("div");

    userMessage.classList.add("user-message");

    userMessage.innerText = question;

    chatBox.appendChild(userMessage);

    // Fake AI Response

    setTimeout(() => {

        const botMessage = document.createElement("div");

        botMessage.classList.add("bot-message");

        botMessage.innerText =
            "🤖 AI response will appear here after backend integration.";

        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;

    },1000);

    input.value = "";
}