function logProperty(target, key) {
    let _val = this[key];
    const getter = () => {
        console.log(`Get: ${key} => ${_val}`);
        return _val;
    }
    const setter = (newValue) => {
        console.log(`Set: ${key} => ${_val}`);
        _val = newValue;
    }

    const objectProperty = {
        get: getter,
        set: setter
    }

    Object.defineProperty(target, key, objectProperty)
}


class Person {
    @logProperty
    public name: string;

    constructor(name: string) {
        this.name = name;
    }
}

const person = new Person('Mijael');
person.name = 'Platzi'; // Set: name => 'Platzi
const nameFromClass = person.name; // Get: name => 'Platzi'
