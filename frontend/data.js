function showTarifs(
	price1h,
	price2h,
	price3h,
	price4h,
	price24h,
	price_pmr,
	price_sub_resident,
	price_sub_no_resident
) {
	alert(
		`Price 1h : ${price1h}€\nPrice 2h : ${price2h}€\nPrice 3h : ${price3h}€\nPrice 4h : ${price4h}€\nPrice 24h : ${price24h}€\nPrice PMR : ${price_pmr}€\nResident subscription : ${price_sub_resident}€\nResident no subscription : ${price_sub_no_resident}€`
	);
}

document.addEventListener("DOMContentLoaded", function () {
	const map = L.map('map').setView([43.6, 1.43], 13);
	L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',
		{
			maxZoom: 18,
			attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
		}
	).addTo(map);

	fetch('/api/parkings')
		.then(response => response.json())
		.then(data => {
			data.forEach(parking => {
				L.marker([parking.lat, parking.lon])
					.addTo(map)
					.bindPopup(`
						<i style=font-size:20px>
							${parking.public === "1" ? "Public" : "Private"} |
						</i>
						<i style=font-size:15px>
						${parking.free === "1" ? "Free" : "Paying"}
				  		</i>
						<br>
						<strong>${parking.name}</strong>
						<br>
						Adress : ${parking.address}
						<br>
						<hr>
                  		- Cars : <b>${parking.free_cars}</b> free<br>
						- Relay place : <b>${parking.free_pr}</b> free<br>
						- Reduced mobility : <b>${parking.free_pmr}</b> free<br>
						- Electric cars : <b>${parking.free_elec_cars
						}</b> free<br>
						- Bikes : <b>${parking.free_bycicles}</b> free<br>
						- 2 electric wheels : <b>${parking.free_two_wheels_elec}</b> free<br>
						- Car sharing : <b>${parking.free_autoshare}</b> free<br>
						- 2 motorized wheels : <b>${parking.free_two_wheels}</b> free<br>
						- Carpooling : <b>${parking.free_covoit}</b> free<br>
						- Leased : <b>${parking.free_amodies}</b> free<br>
						- Minute stops : <b>${parking.free_stop_minute}</b> free<br>
                  		<hr>
                  		<button onclick="showTarifs(${parking.price_1h}, ${parking.price_2h}, ${parking.price_3h
						}, ${parking.price_4h}, ${parking.price_24h}, ${parking.price_pmr}, ${parking.price_sub_resident
						}, ${parking.price_sub_no_resident})">PRICES</button>
					`);
			});
		})
		.catch(error => console.error('Error fetching data:', error));
});