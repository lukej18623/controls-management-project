document.addEventListener('DOMContentLoaded', function () {
    const criteriaSelect = document.querySelector('#criteria');
    const startDateField = document.querySelector('#start_date');
    const endDateField = document.querySelector('#end_date');
    const form = document.querySelector('#visualization-form');
    const alertContainer = document.getElementById('alert-container');

    function toggleDateFields() {
        if (criteriaSelect.value === 'date') {
            startDateField.parentElement.style.display = 'block';
            endDateField.parentElement.style.display = 'block';
        } else {
            startDateField.parentElement.style.display = 'none';
            endDateField.parentElement.style.display = 'none';
        }
    }

    // initial check to set the correct visibility on page load
    toggleDateFields();

    // toggle date fields based on criteria selection
    criteriaSelect.addEventListener('change', toggleDateFields);

    // handle form submission
    form.addEventListener('submit', function (event) {
        if (criteriaSelect.value === 'date') {
            const startDate = startDateField.value;
            const endDate = endDateField.value;

            if (!startDate || !endDate) {
                // if either date is left empty, alert user
                event.preventDefault();  // prevent form submission
                const alertDiv = document.createElement('div');
                alertDiv.className = 'alert alert-warning alert-dismissible fade show';
                alertDiv.role = 'alert';
                alertDiv.innerHTML = `
                    <strong>Warning!</strong> Please provide both start and end dates for date filtering.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                `;
                alertContainer.appendChild(alertDiv);
            }
        }
    })
});