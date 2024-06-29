function openModal(counselorId) {
    const modal = document.getElementById('appointmentModal');
    const modalContent = document.getElementById('modalContent');
    modal.style.display = 'block';

    fetch(`/book_appointment/${counselorId}/`)
        .then(response => response.text())
        .then(html => {
            modalContent.innerHTML = html;
            setupFormSubmit();
        });
}

function closeModal() {
    const modal = document.getElementById('appointmentModal');
    modal.style.display = 'none';
}

function setupFormSubmit() {
    const form = document.getElementById('appointmentForm');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(form);
        const counselorId = form.dataset.counselorId;

        fetch(`/book_appointment/${counselorId}/`, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert(data.message);
                closeModal();
            }
        });
    });
}
function openModal(counselorId) {
    const modal = document.getElementById('appointmentModal');
    const modalContent = document.getElementById('modalContent');
    modal.style.display = 'block';
    setTimeout(() => modal.classList.add('show'), 10);

    fetch(`/book_appointment/${counselorId}/`)
        .then(response => response.text())
        .then(html => {
            modalContent.innerHTML = html;
            setupFormSubmit();
        });
}

function closeModal() {
    const modal = document.getElementById('appointmentModal');
    modal.classList.remove('show');
    setTimeout(() => modal.style.display = 'none', 300);
}

function redirectToBooking(counselorId) {
    window.location.href = `/book_appointment/${counselorId}/`;
}