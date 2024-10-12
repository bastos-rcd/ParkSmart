# ParkSmart

## Prérequis

- Docker
- Docker Compose

## Installation

1. Cloner le dépôt :

   ```bash
   git clone <URL-du-repo>
   cd mon-projet
   ```

2. Initialiser docker-compose :

   ```bash
   docker compose up --build
   ```

3. Start et stop les services :

   ```bash
   docker compose start
   docker compose stop
   ```

4. Accéder aux services :

   - MySQL : [localhost:3306](localhost:3306)
   - Mosquitto : [localhost:1883](localhost:1883)
   - Nginx : [localhost:8080](localhost:8080)
