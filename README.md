# ParkSmart

**ParkSmart** is an interactive web application that allows real-time visualization of available parking spaces in Toulouse on a map. This project combines IoT technologies with web services to provide an intuitive parking management solution.

## Technologies Used

- **MQTT** : Used to collect real-time parking data (availability, status).
- **Python** : Backend language used to process data and interact with the database.
- **MySQL** : Database for storing parking information (location, availability, etc.).
- **Nginx** : Web server to deploy the application.
- **Docker** : Used to orchestrate and isolate the different services.

## Prerequisites

Before installing and running this project, ensure you have the following installed on your machine:

- Docker
- Docker Compose
- Mosquitto
- MySQL Client
- Python 3.0 or higher
- Paho-MQTT
- MySQL Connector

## Installation

1. Clone the repository :

   ```bash
   git clone https://github.com/bastos-rcd/ParkSmart.git
   cd ParkSmart
   ```

2. Run Docker Compose to set up the environment :

   ```bash
   docker compose up --build
   ```

3. Start and stop services :

   ```bash
   docker compose start
   docker compose stop
   ```

4. Initialize the database :

   ```bash
   docker exec -it mysql bash
   mysql -u root -p ParkSmart < /docker-entrypoint-initdb.d/init_db.sql
   ```

5. Run simulation :

   ```bash
   cd python
   python3 start.py
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/bastos-rcd/ParkSmart/blob/master/LICENSE) file for more details.
