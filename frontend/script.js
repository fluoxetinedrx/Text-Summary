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
  const formData = new FormData();
  formData.append("file", uploadedFile);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error(data.error);
      } else {
        inputText.value = data.text;
      }
    })
    .catch((error) => console.error("Error:", error));
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
  const response = await runPythonScript(textToSummarize);
  summaryOutput.textContent = response.summary;

  // Update statistics if available
  if (response.statistics) {
    updateStatistics(response.statistics);
  }
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
    return data;
  } catch (error) {
    console.error(error);
    return {
      summary: "An error occurred while fetching summary.",
      statistics: null,
    };
  }
}

// Function to update statistics
function updateStatistics(statistics) {
  const wordCountElement = document.querySelector(".word-count");
  const characterCountElement = document.querySelector(".characters");
  const reductionElement = document.querySelector(".reduction");

  const originalWordCount = statistics.original_word_count;
  const summaryWordCount = statistics.summary_word_count;

  const originalCharCount = statistics.original_char_count;
  const summaryCharCount = statistics.summary_char_count;

  const reduction = statistics.reduction;
  const contentBasedScore = statistics.content_based_score;

  // Update word count
  wordCountElement.querySelector(".number li:nth-child(1)").textContent =
    originalWordCount;
  wordCountElement.querySelector(".number li:nth-child(3)").textContent =
    summaryWordCount;
  wordCountElement.dataset.value = originalWordCount;

  // Update character count
  characterCountElement.querySelector(".number li:nth-child(1)").textContent =
    originalCharCount;
  characterCountElement.querySelector(".number li:nth-child(3)").textContent =
    summaryCharCount;
  characterCountElement.dataset.value = originalCharCount;

  // Update reduction
  reductionElement.querySelector(
    "p"
  ).textContent = `Content Score: ${contentBasedScore.toFixed(2)}%`;
  reductionElement.dataset.value = reduction.toFixed(2);
}
