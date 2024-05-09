const summarizeButton = document.getElementById('btn-ph');
const inputText = document.getElementById('input-text');
const summaryOutput = document.getElementById('summary-output');

function clearPlaceholder() {
    const placeholderText = document.getElementById("input-text").placeholder;
    if (placeholderText) {
      document.getElementById("input-text").placeholder = "";
    }
  }
  
  function addPlaceholder() {
    const inputText = document.getElementById("input-text").value;
    if (!inputText) {
      document.getElementById("input-text").placeholder = "Enter your input text here...";
    }
  }  

summarizeButton.addEventListener('click', async () => {
    const textToSummarize = inputText.value;
    const summaryText = await runPythonScript(textToSummarize);
    summaryOutput.textContent = summaryText;
});

async function runPythonScript(textToSummarize) {
    try {
        const response = await fetch('/summary', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: textToSummarize
            })
        });
        const data = await response.json();
        return data.summary;
    } catch (error) {
        console.error(error);
        return 'An error occurred while fetching summary.';
    }
}