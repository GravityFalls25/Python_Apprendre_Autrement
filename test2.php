<?php
if(isset($_POST['code']) && isset($_POST['Gold']) && isset($_POST['Id'])) {
    $code = $_POST['code'];
    $gold = $_POST['Gold'];
    $id = $_POST['Id'];
    // Faites ce que vous devez faire avec $code et $gold



// Crée un fichier temporaire pour stocker le code Python


$filename = 'user.py';

// Écrit le code Python dans le fichier test.py
file_put_contents($filename, $code);

// Chemin du fichier test.py

$testPyFilePath = "test_new.py";

// Exécute le fichier test.py en utilisant la commande shell
#$filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
#$output = shell_exec("$filepath $testPyFilePath 2>&1");
$output = shell_exec("C:\\Users\\thiba\\AppData\\Local\\Programs\\Python\\Python38\\python.exe $testPyFilePath $gold $id 2>&1");

//Supprimer le fichier

//unlink($filename);
// Vérifie si l'exécution a généré une sortie
if (!empty($output)) {

    
    // Le chemin vers api.php
    $filePath2 = 'api.php';

    // Lire le contenu actuel de api.php
    $fileContent2 = file_get_contents($filePath2);

    // Supposons que cette condition dépende d'une certaine logique
    // Ici, pour l'exemple, on met à jour le contenu à "True"
    // Vous pouvez remplacer cette partie par votre propre logique
    if ($output == "Correct\nCorrect\nCorrect\n") { // Votre condition ici
        $newContent2 = "<?php\necho \"True\"?>";
    } else {
        $newContent2 = "<?php\necho \"False\"?>";
    }
    // Écrire le nouveau contenu dans api.php
    file_put_contents($filePath2, $newContent2);

    




    // Si oui, renvoie la sortie
    echo $output;
} else {
    // Sinon, renvoie un message de succès
    echo "Code exécuté avec succès";
}

} else {
    echo "Données manquantes.";
}
?>
