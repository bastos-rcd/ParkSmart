document.addEventListener('DOMContentLoaded', function () {
	fetch('/api/parkings')
		.then(response => response.json())
		.then(data => {
			data.forEach(parking => {
				console.log(parking);
			});
		})
		.catch(error => console.error('Error fetching data:', error));
});