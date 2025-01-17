

const popupGenerate =document.querySelectorAll("#generateSudokuButton").forEach(button => {
    button.addEventListener("click", () => openPopup("popupGenerate"));
});
const popupSolution = document.getElementById("viewSolution").addEventListener("click", () => {
    openPopup("viewSolutionPopup");
});


// Single window onclick event handler to close any popup if clicked outside
window.onclick = function(event) {
    

    if (event.target === popupGenerate) {
        closePopup("popupGenerate");
    } else if (event.target === popupSolution) {
        closePopup("viewSolutionPopup");
    }
};

// Function to open the popup
function openPopup(popupId) {
    const popup = document.getElementById(popupId);
    if (popup) {
        popup.style.display = 'block';
    }
}

// Function to close the popup
function closePopup(popupId) {
    const popup = document.getElementById(popupId);
    if (popup) {
        popup.style.display = 'none';
    }
}

// Function to update the Sudoku board cells with new data
function updateSudokuBoard(puzzle) {
    const cells = document.getElementsByClassName('#sudoku-grid .cell');
    cells.forEach((cell, index) => {
        const row = Math.floor(index / 9);
        const col = index % 9;
        cell.textContent = puzzle[row][col] > 0 ? puzzle[row][col] : '';
    });
}
function updateSudokuBoard(puzzle) {
    const cells = document.getElementsByClassName('#sudoku-grid-solution .solution-cell');
    cells.forEach((cell, index) => {
        const row = Math.floor(index / 9);
        const col = index % 9;
        cell.textContent = puzzle[row][col] > 0 ? puzzle[row][col] : '';
    });
}
document.addEventListener('DOMContentLoaded', function() {
    const inputElement = document.getElementById('single-digit-input');

    inputElement.addEventListener('input', function() {
        if (this.value.length > 1) {
            this.value = this.value.slice(0, 1);
        }
    });
});