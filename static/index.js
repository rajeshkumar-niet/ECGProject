
const response = await fetch('/process', {  // local route, not localhost:5000
    method: 'POST',
    body: formData
});

function showSection(id) {
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => section.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}

async function handleSubmit() {
    const fileInput = document.querySelector('input[type="file"]');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file first.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:5000/process', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        alert('Your ECG has been processed successfully. You can now download it if needed.');

        // Optional: you can store the response for later download
        // const blob = await response.blob();
        // window.processedBlob = blob;

    } catch (error) {
        alert('Error processing file: ' + error.message);
    }
}
