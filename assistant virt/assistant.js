
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
        alert('Pas plus de '+indices.length+' indices disponibles.');
      }
    });


    const inputWords = [
"\n\
"
     ];

    const inputText = document.getElementById('inputText');
   
    const outputWords = [
'Je vais bien'
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
  document.getElementById('btn-assistant').addEventListener('click', function() {
    const dialogue = [
      "Il semblerait que tu aies perdu la memoire alors laisse moi te reexpliquer comment ca fonctionne",
      "Ici sera où ta magie prendra forme. C'est ici que tu vas coder",
      "\"Mais comment savoir ce que je dois coder ?\" me diras-tu",
      "Et bien pour le savoir, tu devras cliquer sur ce bouton",
      "non",
      "non2",
      "non3"
           ];
    if (indiceDial===1){
      document.getElementById('editor').style="height: 500px;border-radius: 10px; box-shadow: 0 0 0 1vh rgba(255, 0, 0, 0);animation: blinker 2.5s linear infinite;";
      document.getElementById('assistant-virtuel').style.boxShadow="0 0 0 max(100vh, 100vw) rgba(0, 0, 0, 0)";
    }
    if (indiceDial===3){
      document.getElementById('btn-assistant').style.visibility="hidden";
      document.getElementById('editor').style="height: 500px;border-radius: 10px;";
      document.getElementById('btn_info_sup').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('btn_info_sup').style.animation="blinker 2.5s linear infinite";
      document.getElementById('btn_info_sup').addEventListener('click',function(){
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
        indiceDial++;
        document.getElementById('btn-assistant').style.visibility="visible";
      },{once:true});
    }
    if (indiceDial===4){}
    if (indiceDial===5){}
    if (indiceDial===6){}
    if (indiceDial < dialogue.length) {
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
        indiceDial++;
      }
  });
