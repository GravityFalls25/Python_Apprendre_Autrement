<?php
// Récupère le code Python envoyé par la requête AJAX
$code = $_POST['code'];

// Crée un fichier temporaire pour stocker le code Python
$tempFile = tempnam(sys_get_temp_dir(), 'python_script_');
file_put_contents($tempFile, $code);

// Exécute le code Python en utilisant la commande shell
$descriptorspec = array(
    0 => array("pipe", "r"),
    1 => array("pipe", "w"),
    2 => array("pipe", "w")
);

$process = proc_open("C:\\Users\\thiba\\AppData\\Local\\Programs\\Python\\Python38\\python.exe $tempFile", $descriptorspec, $pipes);

if (is_resource($process)) {
    // Lit les données de sortie jusqu'à la fin du processus
    while (!feof($pipes[1])) {
        $output = fgets($pipes[1]);
        echo $output;
        flush(); // Vide le tampon de sortie
    }
}

// Ferme les descripteurs de fichier
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);

// Ferme le processus
proc_close($process);

// Supprime le fichier temporaire
unlink($tempFile);
?>
