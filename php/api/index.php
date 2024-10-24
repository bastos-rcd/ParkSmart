<?php
header('Content-Type: application/json');

// Connexion à la base de données
$host = 'mysql';
$dbname = 'ParkSmart';
$user = 'admin';
$pass = 'admin';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $stmt = $pdo->query('SELECT * FROM Parking');
    $parkings = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Retourne les données au format JSON
    echo json_encode($parkings);
} catch (PDOException $e) {
    echo json_encode(['error' => $e->getMessage()]);
}
?>