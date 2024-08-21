

// fetches a word and its two definitions 
function fetchWord() {
    const difficulty = document.getElementById('difficulty').value;

    console.log('Difficulty selected:', difficulty)
    // uses fetch API to get the data from /get_word endpoint
    fetch(`/get_word?difficulty=${difficulty}`)
        .then(response => response.json()) // parsing as json
        .then(data => {
            console.log('Data fetched:', data);
            // gets the html element with id word
            const wordElement = document.getElementById('word');
            // sets the elements text content to the word we just got
            wordElement.textContent = data.word;

            // gets html element for choices and displays it
            const choicesDiv = document.getElementById('choices');
            choicesDiv.style.display = 'block';

            // creates and poppulates array with right and wrong anser
            const choices = [data.definition, data.incorrect_definition]; 
            // shuffles which is which
            choices.sort(() => Math.random() - 0.5);

            // gets html element for buttons
            const choiceA = document.getElementById('choiceA');
            const choiceB = document.getElementById('choiceB');

            // sets elements text content to the shuffles choices
            // [0] and [1] are the two choices which were shuffled about
            choiceA.textContent = choices[0];
            choiceB.textContent = choices[1];

            // click event handlers for both buttons
            choiceA.onclick = () => checkAnswer(choiceA, data.definition);
            choiceB.onclick = () => checkAnswer(choiceB, data.definition);
        })
        .catch(error => console.error('Error fetching word:', error));
}

// here we check if they are correct
function checkAnswer(button, correctDefinition) {
    // if they chose right
    if (button.textContent === correctDefinition) {
        alert('Correct answer');
        // if they chose wrong
    } else {
        // giving them the right answer now
        alert('Incorrect answer, the correct answer is: ' + correctDefinition);
    }
}


// Set up event listener for the Start Quiz button
document.getElementById('start-btn').addEventListener('click', function() {
    console.log('Start Quiz button clicked');  // Log button click
    fetchWord();
});


// Show difficulty section when the page loads
document.getElementById('difficulty-section').style.display = 'block';

// Event listener for hints button
document.getElementById('hints-btn').addEventListener('click', function() {
    // Get the current word from the quiz
    const word = document.getElementById('word').textContent.trim();
    
    if (word) {
        // Fetch synonyms for the current word
        fetch(`/get_synonyms?word=${word}`)
            .then(response => response.json()) // parsing as json
            .then(data => {
                const synonymsDiv = document.getElementById('synonyms');
                // if there are any synonyms 
                if (data.synonyms.length > 0) {
                    // Display the synonyms in the synonyms div
                    synonymsDiv.innerHTML = `<p>Synonyms: ${data.synonyms.join(', ')}</p>`;
                } else {
                    synonymsDiv.innerHTML = `<p>No synonyms found.</p>`;
                }
            })
            .catch(error => {
                console.error('Error fetching synonyms:', error);
            });
    }
});







