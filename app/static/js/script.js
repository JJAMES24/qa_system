document.getElementById('qa-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const question = document.getElementById('question').value;
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        const base64Content = e.target.result.split(',')[1];  // Extract base64 part

        const payload = {
            question: question,
            file: {
                filename: file.name,
                content: base64Content
            }
        };

        fetch('/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            if (data.document_answer && data.wikipedia_answer) {
                const qaContainer = document.getElementById('qa-container');
                qaContainer.innerHTML = `
                    <div class="qa-item">
                        <p><strong>Document Answer:</strong> ${data.document_answer}</p>
                        <p><strong>Wikipedia Answer:</strong> ${data.wikipedia_answer}</p>
                    </div>
                `;
            } else {
                console.error('Invalid response data:', data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    reader.readAsDataURL(file);  // Read as base64
});
