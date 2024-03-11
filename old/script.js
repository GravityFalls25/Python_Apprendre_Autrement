function verifierCode() {
    var code = document.getElementById("codeInput").value;
    // Le code caché est 1234. Dans une application réelle, ce code devrait être vérifié côté serveur.
    if (code == "1234") {
        alert("Félicitations! Vous avez trouvé le code et vous êtes échappé.");
        // Ici, vous pouvez rediriger l'utilisateur vers une autre page ou afficher un message de succès plus élaboré.
    } else {
        alert("Code incorrect. Essayez encore.");
    }
}
