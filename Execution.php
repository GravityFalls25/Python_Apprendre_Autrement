<?php
// Récupère le code Python envoyé par la requête AJAX
$code = $_POST['code'];
$contenu = $_POST['contenu'];


// Diviser la chaîne en fonction des balises <br>
$contenu = preg_split('/<br\s*\/?>/i', $contenu);


// Nettoyer chaque élément
foreach ($contenu as &$element) {
    $element = trim(strip_tags($element));
}

// Rejoindre les éléments en une seule chaîne, séparée par des virgules
$contenu = implode(',', $contenu);

// Crée un fichier temporaire pour stocker le code Python
$filename = 'execution.py';
$filename2 = 'user.py';
// si fichier temporaire :  $tempFile = tempnam(sys_get_temp_dir(), 'python_script_');
file_put_contents($filename2, $code);

// Exécute le code Python en utilisant la commande shell
// $filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
// $output = shell_exec("$filepath $filename $contenu 2>&1");

$output = shell_exec("C:\\Users\\thiba\\AppData\\Local\\Programs\\Python\\Python38\\python.exe $filename $contenu 2>&1");


// Pour supprimer le fichier temporaire 
//unlink($tempFile);
// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {
    // Si oui, renvoie la sortie
    echo utf8_encode($output);
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}
?>
