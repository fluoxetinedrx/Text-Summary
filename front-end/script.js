const summarizeButton = document.getElementById('summarize-button');
const inputText = document.getElementById('input-text');
const lengthSelect = document.getElementById('length-select');
const summaryOutput = document.getElementById('summary-output');

summarizeButton.addEventListener('click', async () => {
    const textToSummarize = inputText.value;
    const selectedLength = lengthSelect.value;

    const response = await fetch('https://api.example.com/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: textToSummarize,
            length: selectedLength
        })
    });

    const data = await response.json();
    const summaryText = data.summary;

    summaryOutput.textContent = summaryText;
});