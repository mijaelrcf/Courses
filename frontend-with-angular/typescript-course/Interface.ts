type Dni = number;

interface Persona {
    altura?: number;
    edad: number;
    nombre: string;
    apellido: string;
    dni: Dni;
}

const persona: Persona = {
    //altura: 1.69,
    edad: 27,
    nombre: 'Alan',
    apellido: 'Bucaglia',
    dni: 36363536
}

//? opcionales o no son requeridas