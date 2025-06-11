document.getElementById("textForm").addEventListener("submit", function(event) {
    let inputText = document.getElementById("textInput").value;
    if (!inputText.trim()) {
        alert("Please enter some text before submitting!");
        event.preventDefault();
    }
});