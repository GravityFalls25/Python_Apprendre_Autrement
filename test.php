<?php
// Récupère le code Python envoyé par la requête AJAX
$code = $_POST['code'];

// Crée un fichier temporaire pour stocker le code Python
$tempFile = tempnam(sys_get_temp_dir(), 'python_script_');
file_put_contents($tempFile, $code);

// Exécute le code Python en utilisant la commande shell
$filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
$output = shell_exec("$filepath $tempFile 2>&1");

// Supprime le fichier temporaire
unlink($tempFile);

// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {
    // Si oui, renvoie la sortie
    echo $output;
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}
?>
