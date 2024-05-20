let indiceCount = 0; // Variable pour enregistrer le nombre d'indices demandés
    
    document.getElementById('btnIndice').addEventListener('click', function() {
      const indices = [
'Premier indice: Multiplie chacune des valeurs pour obtenir le volume de flamme à éteindre\n\
',
'Deuxieme indice: Mutliplie le resultat par 100 pour obtenir la quantité d\'eau\n\
',
'Troisieme indice:\n\
Voici une solution possible pour une maison\n\
p_f_1 = int(input())\n\
x_m_1 = int(input())\n\
y_m_1 = int(input())\n\
z_m_1 = int(input())\n\
eau_1 = p_f_1*x_m_1*y_m_1*z_m_1\n\
print(f"Il faut apporter {eau_1*100}mL d\'eau pour la maison 1")\n\
\n\
Ensuite calcule la somme d\'eau\n\
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
"1\n\
5\n\
4\n\
2\n\
2\n\
3\n\
2\n\
1\n\
"
     ];

    const inputText = document.getElementById('inputText');
   
    const outputWords = [
"Il faut apporter 4000mL d'eau pour la maison 1\nIl faut apporter 1200mL d'eau pour la maison 2\nIl faut apporter 5200mL d'eau au total\n"
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
  
