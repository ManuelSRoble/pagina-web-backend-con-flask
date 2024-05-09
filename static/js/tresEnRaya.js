const celdas = document.querySelectorAll(".celda");
const estadoTexto = document.querySelector("#estadoTexto");
const btnReiniciar = document.querySelector("#btnReiniciar");
const condicionesGanar = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2]
];
let opciones = ["", "", "", "", "", "", "", "", ""];
let jugadorActual = "X";
let enEjecucion = false;

iniciarJuego();

function iniciarJuego(){
   celdas.forEach(celda => celda.addEventListener("click", celdaClicada));
   btnReiniciar.addEventListener("click", reiniciarJuego);
   estadoTexto.textContent = `${jugadorActual}'s turno`; 
   enEjecucion = true;
}
function celdaClicada(){
   const indiceCelda = this.getAttribute("indiceCelda");

   if(opciones[indiceCelda] != "" || !enEjecucion){
      return; // no hacer nada
   }

   // de lo contrario
   actualizarCelda(this, indiceCelda);
   verificarGanador();
}
function actualizarCelda(celda, indice){
   opciones[indice] = jugadorActual;
   celda.textContent = jugadorActual;
}
function cambiarJugador(){
   jugadorActual = (jugadorActual == "X") ? "O" : "X";
   estadoTexto.textContent = `${jugadorActual}'s turn`;
}
function verificarGanador(){
   let rondaGanada = false;

   for(let i = 0; i < condicionesGanar.length; i++){
       const condicion = condicionesGanar[i];
       const celdaA = opciones[condicion[0]];
       const celdaB = opciones[condicion[1]];
       const celdaC = opciones[condicion[2]];

       if(celdaA == "" || celdaB == "" || celdaC == ""){
          continue;
       }
       if(celdaA == celdaB && celdaB == celdaC){
          rondaGanada = true;
          break;
       }
   }

   if(rondaGanada){
       estadoTexto.textContent = `${jugadorActual} ¡gana!`;
       enEjecucion = false;
   }
   else if(!opciones.includes("")){
       estadoTexto.textContent = "¡Empate!";
       enEjecucion = false;
   }
   else{
       cambiarJugador(); 
   }
}
function reiniciarJuego(){
   jugadorActual = "X";
   opciones = ["", "", "", "", "", "", "", "", ""];
   estadoTexto.textContent = `${jugadorActual}'s turno`;
   celdas.forEach(celda => celda.textContent = "");
   enEjecucion = true;
}


/*const cells = document.querySelectorAll(".cell");
const statusText = document.querySelector("#statusText");
const restartBtn = document.querySelector("#restartBtn");
const winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2]
];
let options = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let running = false;

initializeGame();

function initializeGame(){
   cells.forEach(cell => cell.addEventListener("click", cellClicked));
   restartBtn.addEventListener("click", restartGame);
   statusText.textContent = `${currentPlayer}'s turn` 
   running = true;
}
function cellClicked(){
   const cellIndex = this.getAttribute("cellIndex");

   if(options[cellIndex] != "" || !running){
      return; //don't do anything
   }

   //otherwise
   updateCell(this, cellIndex);
   checkWinner();
}
function updateCell(cell, index){
   options[index] = currentPlayer;
   cell.textContent = currentPlayer;
}
function changePlayer(){
   currentPlayer = (currentPlayer == "X") ? "O" : "X";
   statusText.textContent = `${currentPlayer}'s turn`;
}
function checkWinner(){
   let roundWon = false;

   for(let i = 0; i < winConditions.length; i++){
       const condition = winConditions[i];
       const cellA = options[condition[0]];
       const cellB = options[condition[1]];
       const cellC = options[condition[2]];

       if(cellA == "" || cellB == "" || cellC == ""){
          continue;
       }
       if(cellA == cellB && cellB == cellC){
          roundWon = true;
          break;
       }
   }

   if(roundWon){
       statusText.textContent = `${currentPlayer} wins!`;
       running = false;
   }
   else if(!options.includes("")){
       statusText.textContent = `Draw!`;
       running = false;
   }
   else{
       changePlayer(); 
   }
}
function restartGame(){
   currentPlayer = "X";
   options = ["", "", "", "", "", "", "", "", ""];
   statusText.textContent = `${currentPlayer}'s turn`;
   cells.forEach(cell => cell.textContent = "");
   running = true;
}
*/