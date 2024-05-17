const summarizeButton = document.getElementById("btn-ph");
const inputText = document.getElementById("input-text");
const summaryOutput = document.getElementById("summary-output");

function clearPlaceholder() {
  const placeholderText = document.getElementById("input-text").placeholder;
  if (placeholderText) {
    document.getElementById("input-text").placeholder = "";
  }
}

function addPlaceholder() {
  const inputText = document.getElementById("input-text").value;
  if (!inputText) {
    document.getElementById("input-text").placeholder =
      "Enter your input text here...";
  }
}

function handleFileUpload(files) {
  if (files.length === 0) {
    return;
  }

  const uploadedFile = files[0];
  const fileName = uploadedFile.name;

  const inputText = document.getElementById("input-text");
  inputText.value = fileName;

  const deleteButton = document.getElementById("delete-file");
  deleteButton.disabled = false;

  deleteButton.addEventListener("click", function () {
    inputText.value = "";
    this.disabled = true; // Disable the button again
  });
}

const panels = document.querySelector(".js-panel");
const modal = document.querySelector(".js-modal");
const modalClose = document.querySelector(".js-modal-close");

function showStatistics() {
  modal.classList.add("open");
}

function hideStatistics() {
  modal.classList.remove("open");
}
panels.addEventListener("click", showStatistics);

modalClose.addEventListener("click", hideStatistics);

summarizeButton.addEventListener("click", async () => {
  const textToSummarize = inputText.value;
  const summaryText = await runPythonScript(textToSummarize);
  summaryOutput.textContent = summaryText;
});

async function runPythonScript(textToSummarize) {
  try {
    const response = await fetch("/summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: textToSummarize,
      }),
    });
    const data = await response.json();
    return data.summary;
  } catch (error) {
    console.error(error);
    return "An error occurred while fetching summary.";
  }
}
