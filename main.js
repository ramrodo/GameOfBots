/*jshint esversion: 6 */

export default class Bot {

   constructor(args){
     this.args = args;
   }

   execute(){
     let args = this.args;
     let text = args.text;

     return new Promise ((resolve)=>{

       if (text){
        resolve({
          "text": "Lista de canciones:\n1.-Shakira\n2.-José José\n3.-Green Day\n"
           });
         if (text.indexOf("1") >= 0){
           resolve({
               "text": "¿Cómo te sientes con ésta canción"
           });
         }
         else{
           resolve({
             text : `Selecciona una opción correcta`
           });
         }
       }
     });

   }
  }
