document.getElementById('orderForm').addEventListener('submit', function (e) {
    const submitButton = document.getElementById('submitButton');
    submitButton.disabled = true;
    submitButton.textContent = 'Отправка...';
});