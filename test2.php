<?php
// Chemin du fichier test.py
$testPyFilePath = "test.py";

// Exécute le fichier test.py en utilisant la commande shell
$output = shell_exec("C:\\Users\\thiba\\AppData\\Local\\Programs\\Python\\Python38\\python.exe $testPyFilePath 2>&1");

// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {
    // Si oui, renvoie la sortie
    echo $output;
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}
?>
