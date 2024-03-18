<?php
$code = $_POST['code'];

// Crée un fichier temporaire pour stocker le code Python


$filename = 'user.py';

// Écrit le code Python dans le fichier test.py
file_put_contents($filename, $code);

// Chemin du fichier test.py

$testPyFilePath = "test.py";

// Exécute le fichier test.py en utilisant la commande shell
$filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
$output = shell_exec("$filepath $testPyFilePath 2>&1");

//Supprimer le fichier

//unlink($filename);
// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {
    // Si oui, renvoie la sortie
    echo $output;
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}
?>
