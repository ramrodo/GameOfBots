/*jshint esversion: 6 */

export default class Bot {
	constructor(args){
		this.args = args;
	}

	execute(){
		return new Promise((resolve)=>{
			resolve({
				"text" : "Helo! I'am a Recime bot. How may I help you?"
			});
		});
	}
}
