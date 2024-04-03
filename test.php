<?php
// Récupère le code Python envoyé par la requête AJAX
$code = $_POST['code'];
$contenuHTML = $_POST['contenu'];

$importStart ='import mock' . "\n";
// Separations des informations des balises
preg_match_all('/<p>(.*?)<\/p>/', $contenuHTML, $matches);

// Récupère les textes extraits
$texteArray = $matches[1];

// Convertit le tableau en une chaîne JSON
$contenuJSON = json_encode($texteArray);

// Formatte la chaîne JSON pour qu'elle corresponde au format de liste Python
$contenuPython = str_replace('"', "'", $contenuJSON);

// Construction de la chaîne pour le début de la boucle
$loopStart = 'with mock.patch("builtins.input", side_effect=' . $contenuPython . '):' . "\n";

$indentation = "    "; 

// Sépare le code en lignes
$lines = explode("\n", $code);

// Prépare le nouveau code avec la boucle
$newCode = $importStart . $loopStart;
foreach ($lines as $line) {
    // Augmente l'indentation de chaque ligne pour la mettre dans la boucle
    $newCode .= $indentation . $line . "\n";
}

// Crée un fichier temporaire pour stocker le code Python
$filename = 'user.py';
// si fichier temporaire :  $tempFile = tempnam(sys_get_temp_dir(), 'python_script_');
file_put_contents($filename, $newCode);

// Exécute le code Python en utilisant la commande shell
// $filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
// $output = shell_exec("$filepath $tempFile 2>&1");

$output = shell_exec("C:\\Users\\thiba\\AppData\\Local\\Programs\\Python\\Python38\\python.exe $filename 2>&1");


// Pour supprimer le fichier temporaire unlink($tempFile);
// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {
    // Si oui, renvoie la sortie
    echo utf8_encode($output);
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}
?>
