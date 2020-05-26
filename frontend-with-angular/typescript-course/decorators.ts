//decorator
function log(target, key) {
    console.log(key + 'se ha llamado');
}
//log es la function, al usar con @ 
//target hace representacion al elemento que contenga su funcionalidad -> Persona
//key hace referencia al elemento que estamos refiriendo -> sayMyName


class Persona {
    private name: string;
    
    constructor(name: string) {
        this.name = name;
    }

    @log
    sayMyName() {
        return this.name;
    }
    //tiene cierta complejidad para los decorators pero estas se pueden sobre escribir.
}

const persona: Persona = new Persona('Mijael');
persona.sayMyName(); //'Mijael' // 'sayMyName se ha llamado' 