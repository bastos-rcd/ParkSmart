FROM php:8.0-fpm

RUN docker-php-ext-install pdo pdo_mysql

WORKDIR /var/www/html

COPY . .

EXPOSE 9000