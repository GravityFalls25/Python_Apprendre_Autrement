$(document).ready(function() {
    // Initialise l'éditeur de code
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/python");

    // Définit une fonction pour exécuter le code
    function executerCode() {
        // Récupère le code Python de l'éditeur
        var code = editor.getValue();

        // Envoie le code au serveur via AJAX
        $.ajax({
            url: 'script_python_php.php',
            type: 'POST',
            data: { code: code },
            success: function(response) {
                // Affiche la réponse du serveur dans une zone de résultat
                $('#resultat').text(response);
            },
            error: function(xhr, status, error) {
                // Gère les erreurs de la requête AJAX
                console.error('Erreur AJAX : ', status, error);
            }
        });
    }

    // Associe la fonction d'exécution au bouton "Exécuter"
    $('#btn-executer').click(function() {
        executerCode();
    });
});
