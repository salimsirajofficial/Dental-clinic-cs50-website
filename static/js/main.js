/**
 * BrightSmile Dental Clinic - Main JavaScript
 * Handles common interactive features
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize tooltips if Bootstrap tooltips are used
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href.length > 1) {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Password strength indicator (if needed)
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(function(input) {
        if (input.id === 'password' && !input.id.includes('confirm')) {
            input.addEventListener('input', function() {
                const password = this.value;
                const strength = checkPasswordStrength(password);
                // You can add visual feedback here if needed
            });
        }
    });

    // Date picker enhancements
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        // Set minimum date to today if not already set
        if (!input.hasAttribute('min')) {
            const today = new Date().toISOString().split('T')[0];
            input.setAttribute('min', today);
        }

        // Prevent selecting past dates
        input.addEventListener('change', function() {
            const selectedDate = new Date(this.value);
            const today = new Date();
            today.setHours(0, 0, 0, 0);

            if (selectedDate < today) {
                alert('Please select a future date.');
                this.value = '';
            }
        });
    });

    // Time slot availability check (placeholder for future implementation)
    function checkTimeSlotAvailability(date, time) {
        // This would typically make an AJAX call to the backend
        // to check if the time slot is available
        return true;
    }

    // Helper function to check password strength
    function checkPasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (password.match(/[a-z]+/)) strength++;
        if (password.match(/[A-Z]+/)) strength++;
        if (password.match(/[0-9]+/)) strength++;
        if (password.match(/[$@#&!]+/)) strength++;
        return strength;
    }

    // Console log for debugging (remove in production)
    console.log('BrightSmile Dental Clinic - Frontend loaded successfully');
});

// Utility function to format dates
function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// Utility function to format time
function formatTime(timeString) {
    const [hours, minutes] = timeString.split(':');
    const hour = parseInt(hours);
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const displayHour = hour % 12 || 12;
    return `${displayHour}:${minutes} ${ampm}`;
}


