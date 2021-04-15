function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

 /*

const chatbotOutput = document.getElementById('chatbotOutput');
const chatbotInput = document.getElementById('chatbotInput');
const submitButton = document.getElementById('submitButton');

submitButton.onclick = userSubmitEventHandler;
chatbotInput.onkeyup = userSubmitEventHandler;

function userSubmitEventHandler(event) {
    if (
        (event.keyCode && event.keyCode === 13) ||
        event.type === 'click'
    ) {
        chatbotOutput.innerText = 'thinking...';
        askChatBot(chatbotInput.value);
    }
}

function askChatBot(userInput) {
    const myRequest = new Request('/', {
        method: 'POST',
        body: userInput
    });

    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('HTTP error, status = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        chatbotInput.value = '';
        chatbotOutput.innerText = text;
    }).catch((err) => {
        console.error(err);
    });
}

 */