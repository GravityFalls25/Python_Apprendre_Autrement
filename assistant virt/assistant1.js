
let indiceCount = 0; // Variable pour enregistrer le nombre d'indices demandés
    
    document.getElementById('btnIndice').addEventListener('click', function() {
      const indices = [
'Premier indice: Tu dois afficher l\'addition des differents types de champignons\n\
',
'Deuxieme indice: Si tu écris un texte, n\'oublie pas les ", si tu veux afficher la valeur d\'une variable tu peux mettre un f avant les guillemets puis mettre le nom de la varible dans des {} dans le print\n\
',
'Troisieme indice:\n\
print(f"la quantité de champignons recolté vaut en total {a1+a2+a3}")\n\
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
"3\n\ 5\n\ 1\n\
",
"5\n\ 87\n\ 2\n\
",
"37\n\ 53\n\ 8\n\
"
     ];

    const inputText = document.getElementById('inputText');
   
    const outputWords = [
'9', '94', '98'
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
  

  let indiceDial=0;
  document.getElementById('btn-assistant').addEventListener('click', function(){
    const dialogue = [
      "Il semblerait que tu aies perdu la memoire alors laisse moi te reexpliquer comment ca fonctionne",
      ""
    ];
  if (indiceDial < dialogue.length) {
    document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
    indiceDial++;
  }
});
