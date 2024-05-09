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
   estadoTexto.textContent = `Turno de ${jugadorActual}`; 
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
   estadoTexto.textContent = `Turno de ${jugadorActual}`;
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
       estadoTexto.textContent = `${jugadorActual} ¡ Gana !`;
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
   estadoTexto.textContent = `Turno de ${jugadorActual}`;
   celdas.forEach(celda => celda.textContent = "");
   enEjecucion = true;
}
