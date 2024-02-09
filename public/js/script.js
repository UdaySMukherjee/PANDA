//Get reference to our submit button and chatbot field
const submit = document.getElementById("submit");
const responseField = document.getElementById("response");
const userInput = document.getElementById("user-input");
const chatHistory = document.getElementById("chat-history");
const loading = document.getElementById("spinner");

const classes = ["depression", "anxiety", "normal", "ocd", "ptsd", "Schizophrenia", "Bipolar Disorder", "Panic Disorder and Agoraphobia", "Social Anxiety", "Emotional Disorder", "Borderline Personality Disorder"];
const class_counts = {};

// Initialize class_counts object with 0 counts for each class
classes.forEach(className => {
    class_counts[className] = 0;
});

function printInitialMessages() {
    const initialMessages = [
        "DR.PANDA: Hi there! I'm here to chat with you. Feel free to share your thoughts or concerns. If you'd like, you can mention any mental health-related experiences.",
        "DR.PANDA: Type 'bye' when you're ready to end the conversation."
    ];
    initialMessages.forEach(message => {
        const historyElement = document.createElement('div');
        historyElement.innerHTML = `<li class="list-group-item">${message}</li>`;
        chatHistory.append(historyElement);
    });
}

async function analyzeUserResponse(userInput) {
    const response = await fetch('/chat', {
      method: 'POST',
      body: JSON.stringify({
        model: "gpt-3.5-turbo-0613",
        messages: [
          {
            "role": "user",
            "content": `Please classify the following user response into one of the following classes: depression, anxiety, normal, OCD, PTSD, schizophrenia, bipolar disorder, panic disorder and agoraphobia, social anxiety, emotional disorder, borderline personality disorder and give result in these classes only:\n\n${userInput} `,
          }
        ],
        temperature: 0.6,
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const responseData = await response.json();
    let message = responseData.result[0].message.content;
    const historyElement = document.createElement('div');
    historyElement.innerHTML = `<li class="list-group-item">${message}</li>`;
    chatHistory.append(historyElement);
}

// function printClassPercentages() {
//     let percentagesMessage = "\nChatbot: Here are the probable mental health conditions identified along with their percentages:\n";
//     // Count the occurrences of each class
//     const class_counts = {};
//     classified_classes.forEach(className => {
//         if (className in class_counts) {
//             class_counts[className]++;
//         } else {
//             console.log(`Warning: Unexpected classification '${className}'. Ignoring for counting.`);
//         }
//     });
//     // Calculate the total number of responses
//     const total_responses = classified_classes.length;

//     for (const [className, count] of Object.entries(class_counts)) {
//         if (count > 0) {
//             const percentage = (count / total_responses) * 100;
//             percentagesMessage += `${className}: ${percentage.toFixed(2)}%\n`;
//         }
//     }
//     const historyElement = document.createElement('div');
//     historyElement.innerHTML = `<li class="list-group-item">${percentagesMessage}</li>`;
//     chatHistory.append(historyElement);
// }


function printGoodbyeMessage() {
    const goodbyeMessage = "DR.PANDA: Thank you for sharing. Take care and goodbye!";
    const historyElement = document.createElement('div');
    historyElement.innerHTML = `<li class="list-group-item">${goodbyeMessage}</li>`;
    chatHistory.append(historyElement);
    analyzeUserResponse(fullUserInput);
}

let fullUserInput = ''; 

const generateResponse = async () => {

    loading.classList.remove("visually-hidden");
    submit.classList.add("visually-hidden");
    const input = userInput.value.trim();
    const isGoodbye = input.toLowerCase().includes("bye");
    
    // Concatenate the input to the fullUserInput variable
    fullUserInput += input + ' ';

    if (isGoodbye) {
        console.log("Saving conversation history...");
        printGoodbyeMessage();
    }
    
    const response = await fetch('/chat', {
        method: 'POST',
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{"role": "user", "content": input}],
            temp: 0.6
        }), 
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const responseData = await response.json();
    let message = responseData.result[0].message.content;
    console.log(message);

    userInput.value = "";

    const historyElement = document.createElement('div');
    historyElement.innerHTML = `<li class="list-group-item">${username}: ${input}</li>
    <li class="list-group-item"> DR.PANDA: ${message}</li>`;
    chatHistory.append(historyElement);

    // Stop loading spinner
    loading.classList.add("visually-hidden");
    submit.classList.remove("visually-hidden");

}

//Assign onclick method
window.onload = printInitialMessages;
submit.onclick = generateResponse;