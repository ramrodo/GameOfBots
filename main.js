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

        
          switch (text) {
            case '1':
              resolve({"text": "Canción 1 elegida"});
              break;
            case '2':
              resolve({"text": "Canción 2 elegida"});
              break;
            case '3':
              resolve({"text": "Canción 3 elegida"});
              break;
            case '4':
              resolve({"text": "Canción 4 elegida"});
              break;
            case '5':
              resolve({"text": "Canción 5 elegida"});
              break;
            default:
              resolve({"text": "No entiendo"});
              break;
          }

       }
     });

   }
  }
