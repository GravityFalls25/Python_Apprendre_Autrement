
let indiceCount = 0; // Variable pour enregistrer le nombre d'indices demandés
    
    document.getElementById('btnIndice').addEventListener('click', function() {
      const indices = [
'Premier indice: Ici il suffit d\'ecrire le message qu\'elle t\'a dit\n\
',
'Deuxieme indice: Si tu écris un texte, n\'ouvblie pas les "\n\
',
'Troisieme indice:\n\
print("Je vais bien")\n\
',
      ];
      
      if (indiceCount < indices.length) {
        document.getElementById('indiceText').innerText += indices[indiceCount] + '\n';
        indiceCount++;
        console.log(indiceCount);
      } else {
        alert('Pas plus de trois indices disponibles.');
      }
    });


    const inputWords = [
"\n\
",
"\n\
",
"\n\
"
     ];

    const inputText = document.getElementById('inputText');
   
    const outputWords = [
'Je vais bien', '', ''
    ];
    let currentIndex = 0; // Indice du mot actuellement affiché
  
    const outputText = document.getElementById('outputText');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
  
    function displayWord(index) {
      outputText.innerText = outputWords[index];
      inputText.innerText = inputWords[index];
    }
  
    displayWord(currentIndex);
  
    prevBtn.addEventListener('click', function() {
      if (currentIndex > 0) {
        currentIndex--;
        displayWord(currentIndex);
      }
    });
  
    nextBtn.addEventListener('click', function() {
      if (currentIndex < outputWords.length - 1) {
        currentIndex++;
        displayWord(currentIndex);
      }
    });
// Fonction pour récupérer les paramètres de l'URL
function getQueryParams() {
    const queryParams = {};
    const queryString = window.location.search.substring(1);
    const params = queryString.split('&');
    for (let param of params) {
      const [key, value] = param.split('=');
      queryParams[key] = decodeURIComponent(value);
    }
    return queryParams;
  }

  // Utilisation de la fonction pour récupérer les paramètres
  const queryParams = getQueryParams();
  console.log(queryParams); // Affiche les paramètres dans la console du navigateur

  // Récupérer la valeur du paramètre "id"
  const idValue = queryParams.id;
  console.log('Valeur de "id" :', idValue); // Affiche la valeur de "id" dans la console

  // Exemple d'utilisation : Afficher la valeur de "id" dans une alerte
  if (idValue) {
    alert('La valeur de "id" est : ' + idValue);
    // Vous pouvez utiliser idValue pour effectuer des actions spéciales en fonction de la valeur de "id"
  }
  


document.querySelectorAll('button').forEach(button => {
    button.addEventListener('mouseenter', function() {
        const description = this.getAttribute('data-assistant'); // Assurez-vous d'ajouter cet attribut à vos boutons
        document.getElementById('texte-description').textContent = description;
    });

    button.addEventListener('mouseleave', function() {
        document.getElementById('texte-description').textContent = 'Cliquez sur un bouton pour obtenir des informations.';
    });
});
