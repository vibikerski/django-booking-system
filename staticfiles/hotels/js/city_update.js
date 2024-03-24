document.getElementById('country').addEventListener('change', function() {
    let countryId = this.value;
    let citySelect = document.getElementById('city-select');

    citySelect.innerHTML = '<option value="">All Cities</option>';

    if (countryId) {
        fetch(`/hotels/cities/${countryId}`)
        .then(response => response.json())
        .then(data => {
            data.forEach(city => {
                let option = document.createElement('option');
                option.value = city.id;
                option.textContent = city.name;
                citySelect.appendChild(option);
            });
        });
    }
});
