
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
      "Lors de tes tests si tu veux voir ce que ton code va afficher appuie sur ce bouton",
      "Si tu pense que ton code est fini et correct alors appuie sur ce bouton pour soumettre ton code",
      "\"Mais comment savoir ce que je dois coder ?\" me diras-tu",
      "Et bien pour le savoir, tu devras cliquer sur ce bouton",
      "Tu aura alors une explication complete de la situation et sur ce que tu dois faire",
      "Clique maintenant sur ce bouton",
      "Ici tu aura une explication plus technique sur les outils que tu peux utiliser",
      "Passons à l'onglet suivant",
      "Ici tu aura un exemple de ce que ton programme doit pouvoir afficher",
      "Attention à ce que ton programme affiche soit absolument identique à ce qui marqué dans cet onglet donc vérifie bien que tu utilises les majuscules ou les symboles aux bons endroits",
      "Et enfin voila le dernier onglet celui des indices",
      "Si jamais une des quetes est trop compliquée et que tu te retrouve coincé alors tu peux demander des indices ici",
      "Ces indices ne sont malheureusement pas gratuit et les reveler fera baisser ton score mais c'est toujours mieux que de rester coincé n'est-ce pas ?",
      "C'est tout pour le rappel, c'est maintenant à toi de jouer"
           ];
    if (indiceDial===1){
      document.getElementById('editor').style="height: 500px;border-radius: 10px; box-shadow: 0 0 0 1vh rgba(255, 0, 0, 0);animation: blinker 2.5s linear infinite;";
      document.getElementById('assistant-virtuel').style.boxShadow="0 0 0 max(100vh, 100vw) rgba(0, 0, 0, 0)";
    }
    if (indiceDial===2){
      document.getElementById('editor').style="height: 500px;border-radius: 10px;";
      document.getElementById('btn-executer').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('btn-executer').style.animation="blinker 2.5s linear infinite";
    }
    if (indiceDial===3){
      document.getElementById('btn-executer').style.removeProperty('box-shadow');
      document.getElementById('btn-executer').style.removeProperty('animation');
      document.getElementById('btn-verifier').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('btn-verifier').style.animation="blinker 2.5s linear infinite";
    }
    if (indiceDial===5){
      document.getElementById('btn-verifier').style.removeProperty('box-shadow');
      document.getElementById('btn-verifier').style.removeProperty('animation');
      document.getElementById('btn-assistant').style.visibility="hidden";
      document.getElementById('btn_info_sup').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('btn_info_sup').style.animation="blinker 2.5s linear infinite";
      document.getElementById('btn_info_sup').addEventListener('click',function(){
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial]
        document.getElementById('btn-assistant').style.visibility="visible";
        document.getElementById('btn_info_sup').style.removeProperty('box-shadow');
        document.getElementById('btn_info_sup').style.removeProperty('animation');
        indiceDial++;
      },{once:true});
    }
    if (indiceDial===7){
      document.getElementById('btn-assistant').style.visibility="hidden";
      document.getElementById('aide-tab').addEventListener('click',function(){
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
        indiceDial++;
        document.getElementById('btn-assistant').style.visibility="visible";
        document.getElementById('aide-tab').style.removeProperty('box-shadow');
        document.getElementById('aide-tab').style.removeProperty('animation');
      },{once:true});
      document.getElementById('aide-tab').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('aide-tab').style.animation="blinker 2.5s linear infinite";
    }
    if (indiceDial===9){
      document.getElementById('btn-assistant').style.visibility="hidden";
      document.getElementById('output-tab').addEventListener('click',function(){
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
        indiceDial++;
        document.getElementById('btn-assistant').style.visibility="visible";
        document.getElementById('output-tab').style.removeProperty('box-shadow');
        document.getElementById('output-tab').style.removeProperty('animation');
      },{once:true});
      document.getElementById('output-tab').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('output-tab').style.animation="blinker 2.5s linear infinite";
    }
    if (indiceDial===12){
      document.getElementById('btn-assistant').style.visibility="hidden";
      document.getElementById('indice-tab').addEventListener('click',function(){
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
        indiceDial++;
        document.getElementById('btn-assistant').style.visibility="visible";
        document.getElementById('indice-tab').style.removeProperty('box-shadow');
        document.getElementById('indice-tab').style.removeProperty('animation');
      },{once:true});
      document.getElementById('indice-tab').style.boxShadow="0 0 0 1vh rgba(255, 0, 0, 0)";
      document.getElementById('indice-tab').style.animation="blinker 2.5s linear infinite";
    }
    if (indiceDial === dialogue.length-1){
      document.getElementById('btn-assistant').innerText = "Fin";
    }
    if (indiceDial === dialogue.length){
      document.getElementById('assistant-virtuel').remove();
    }
    if (indiceDial < dialogue.length) {
        document.getElementById('assistant-dialogue').innerText = dialogue[indiceDial] ;
        indiceDial++;
      }
    
  });
