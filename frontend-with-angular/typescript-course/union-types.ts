type SumaParameter = string | number;
type SumaReturnType = string | number;

function Suma(num1: SumaParameter, num2: SumaParameter): SumaReturnType {
    return String(num1) + num2; 
    // no es necesario tratar a todos los parametros ya que typescript se basa en el primero
}

interface Interface1 {
    prop1: number;
}

interface Interface2 {
    prop2: number;
}

type InterfaceMix = Interface1 | Interface2;

const interfaceMix: InterfaceMix = {
    prop1: 2,
    prop2: 2
}