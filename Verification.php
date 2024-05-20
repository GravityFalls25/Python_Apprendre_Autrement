<?php
if(isset($_POST['code']) && isset($_POST['Gold']) && isset($_POST['Id'])) {
    $code = $_POST['code'];
    $gold = $_POST['Gold'];
    $id = $_POST['Id'];
    



// Crée un fichier temporaire pour stocker le code Python


$filename = 'user.py';

// Écrit le code Python dans le fichier test.py
file_put_contents($filename, $code);

// Chemin du fichier test.py

$testPyFilePath = "test_new_". $id. ".py";

// Exécute le fichier test.py en utilisant la commande shell
$filepath='C:\\Users\\"johan ruiz"\\AppData\\Local\\Programs\\Python\\Python310\\python.exe';
$output = shell_exec("$filepath $testPyFilePath $gold $id 2>&1");
#$output = shell_exec("C:\\Users\\thiba\\AppData\\Local\\Programs\\Python\\Python38\\python.exe $testPyFilePath $gold $id 2>&1");

//Supprimer le fichier

//unlink($filename);

echo $output;
}
?>
