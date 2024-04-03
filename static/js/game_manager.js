const guessForm = document.getElementById('guess-form');
const guessInput = document.getElementById('guess-input');
const gridContainer = document.getElementById('grid-container');
const wordId = document.getElementById('word-id');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

guessForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const guess = guessInput.value.toUpperCase();
  guessInput.value = ''; // Clear guess input after submit

  const word_id = wordId.value;

  // Make a fetch request to the Django view for guess handling
  const response = await fetch('handle-guess', {
    method: 'POST',
    body: JSON.stringify({ guess, word_id }),
    headers: { 'Content-Type': 'application/json', "X-CSRFToken": csrftoken }
  });

  if (!response.ok) {
    console.error('Error submitting guess:', response.statusText);
    return;
  }

  const colorList = await response.json();

  // Update the grid with the new attempt and color list
  updateGrid(guess, colorList);
});

function updateGrid(guess, colorList) {
    const newRow = document.createElement('tr');

    // Iterate through guess and color list to create cells
    for (let i = 0; i < guess.length; i++) {
        const cell = document.createElement('td');
        cell.textContent = guess[i];
        cell.classList.add(colorList["color_list"][i]);
        newRow.appendChild(cell);
    }

    gridContainer.appendChild(newRow);
}
