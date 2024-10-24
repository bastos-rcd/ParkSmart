DROP TABLE IF EXISTS Parking;

CREATE TABLE Parking
(
    id VARCHAR(12) PRIMARY KEY,
    lon DOUBLE NOT NULL,
    lat DOUBLE NOT NULL,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    public BOOLEAN NOT NULL,
    free BOOLEAN NOT NULL,
    max_height DOUBLE NOT NULL,
    price_pmr DOUBLE NOT NULL,
    price_1h DOUBLE NOT NULL,
    price_2h DOUBLE NOT NULL,
    price_3h DOUBLE NOT NULL,
    price_4h DOUBLE NOT NULL,
    price_24h DOUBLE NOT NULL,
    price_sub_resident DOUBLE NOT NULL,
    price_sub_no_resident DOUBLE NOT NULL,
    cars INTEGER NOT NULL,
    free_cars INTEGER NOT NULL,
    free_cars_average INTEGER NOT NULL,
    pr INTEGER NOT NULL,
    free_pr INTEGER NOT NULL,
    free_pr_average INTEGER NOT NULL,
    pmr INTEGER NOT NULL,
    free_pmr INTEGER NOT NULL,
    free_pmr_average INTEGER NOT NULL,
    elec_cars INTEGER NOT NULL,
    free_elec_cars INTEGER NOT NULL,
    free_elec_cars_average INTEGER NOT NULL,
    bycicles INTEGER NOT NULL,
    free_bycicles INTEGER NOT NULL,
    free_bycicles_average INTEGER NOT NULL,
    two_wheels_elec INTEGER NOT NULL,
    free_two_wheels_elec INTEGER NOT NULL,
    free_two_wheels_elec_average INTEGER NOT NULL,
    autoshare INTEGER NOT NULL,
    free_autoshare INTEGER NOT NULL,
    free_autoshare_average INTEGER NOT NULL,
    two_wheels INTEGER NOT NULL,
    free_two_wheels INTEGER NOT NULL,
    free_two_wheels_average INTEGER NOT NULL,
    covoit INTEGER NOT NULL,
    free_covoit INTEGER NOT NULL,
    free_covoit_average INTEGER NOT NULL,
    amodies INTEGER NOT NULL,
    free_amodies INTEGER NOT NULL,
    free_amodies_average INTEGER NOT NULL,
    stop_minute INTEGER NOT NULL,
    free_stop_minute INTEGER NOT NULL,
    free_stop_minute_average INTEGER NOT NULL
);