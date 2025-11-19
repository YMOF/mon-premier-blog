<?php
session_start();
require_once 'db_connexion.php';
$db = dbconnect();

$nom = isset($_POST['lastname']) ? trim($_POST['lastname']) : null;
$prenom = isset($_POST['firstname']) ? trim($_POST['firstname']) : null;
$email = isset($_POST['email']) ? trim($_POST['email']) : null;
$telephone = isset($_POST['phone']) ? trim($_POST['phone']) : null;
$mot_de_passe = isset($_POST['password']) ? $_POST['password'] : null;

// Vérifications simples
if (!$nom || !$prenom || !$email || !$mot_de_passe) {
    $_SESSION['message'] = "Tous les champs sont obligatoires.";
    header('Location: inscription.php');
    exit();
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $_SESSION['message'] = "Adresse email invalide.";
    header('Location: inscription.php');
    exit();
}

// Hash du mot de passe
$mdp_hache = password_hash($mot_de_passe, PASSWORD_BCRYPT);

// Insertion en base
$sql = "INSERT INTO client (nom_cli, prenom_cli, telephone_cli, email_cli, mot_de_passe_cli)
        VALUES (:nom, :prenom, :telephone, :email, :mdp)";
$stmt = $db->prepare($sql);
$stmt->execute([
    ':nom' => $nom,
    ':prenom' => $prenom,
    ':telephone' => $telephone,
    ':email' => $email,
    ':mdp' => $mdp_hache
]);

$idClient = $db->lastInsertId();

// Création de la session utilisateur
$_SESSION['utilisateur'] = [
    'id' => $idClient,
    'prenom' => $prenom,
    'nom' => $nom,
    'email' => $email
];

// Message de bienvenue temporaire
$_SESSION['welcome_message'] = "Bienvenue, $prenom !";

header('Location: index.php');
exit();