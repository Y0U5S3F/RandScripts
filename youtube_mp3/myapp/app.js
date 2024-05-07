document.getElementById('submit').addEventListener('click', function(event) {
    event.preventDefault();

    let url = document.getElementById('link').value;

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url }),
    })
    .then(response => response.blob())
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'output.mp3';
        a.click();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});