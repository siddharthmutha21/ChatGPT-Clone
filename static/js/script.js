sendButton.addEventListener("click", sendMessage);

questionInput.addEventListener('keypress', function(event) {
    if (event.keyCode === 13 || event.key === "Enter") {
        sendMessage();
    }
});

async function sendMessage() {
    const questionInputValue = document.getElementById("questionInput").value;
    document.getElementById("questionInput").value = "";
    document.querySelector(".right2").style.display = "block";
    document.querySelector(".right1").style.display = "none";

    question1.innerHTML = questionInputValue;
    question2.innerHTML = questionInputValue;

    // Get the answer and populate it!
    let result = await postData("/api", { "question": questionInputValue });
    solution.innerHTML = result.answer;
}

// Example POST method implementation:
async function postData(url = "", data = {}) {
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    });
    return response.json();
}
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("loginForm").addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent form submission
      
      // Fetch form data
      const formData = new FormData(this);

      // Send form data to Flask route using fetch API
      fetch("/index", {
          method: "POST",
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          if (data.message === "Login Successful") {
              window.location.href = "/dashboard"; // Redirect to dashboard on successful login
          } else {
              document.getElementById("errorMessage").innerText = data.message; // Show error message
          }
      })
      .catch(error => {
          console.error("Error:", error);
      });
  });
});