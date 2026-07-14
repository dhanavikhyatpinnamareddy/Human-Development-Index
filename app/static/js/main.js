// Form Validation and Loading State
document.addEventListener('DOMContentLoaded', function () {
    
    // Bootstrap Form Validation
    const forms = document.querySelectorAll('.needs-validation');

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                // If valid, show loading state
                const submitBtn = form.querySelector('.submit-btn');
                const btnText = submitBtn.querySelector('.btn-text');
                const loader = submitBtn.querySelector('.loader');

                if (submitBtn && btnText && loader) {
                    submitBtn.disabled = true;
                    btnText.classList.add('d-none');
                    loader.classList.remove('d-none');
                }
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Gauge Animation (for result page)
    const progressBar = document.querySelector('.progress-bar');
    if (progressBar) {
        const targetWidth = progressBar.getAttribute('data-target');
        setTimeout(() => {
            progressBar.style.width = targetWidth + '%';
        }, 300); // slight delay for visual effect
    }
});
