<?php
// Chemin du fichier test.py
$testPyFilePath = "test.py";

// Exécute le fichier test.py en utilisant la commande shell
$filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'
$output = shell_exec("$filepath $testPyFilePath 2>&1");

// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {
    // Si oui, renvoie la sortie
    echo $output;
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}
?>
