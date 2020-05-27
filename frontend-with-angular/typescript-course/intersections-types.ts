interface Interface1 {
    prop1: number;
}

interface Interface2 {
    prop2: number;
    prop3: number;
}

interface Interface3 {
    prop2: number;
}

type InterfaceMix_Intersection = Interface1 & Interface2 & Interface3;

const interfaceMix_intersection: InterfaceMix_Intersection = {
    prop1: 2,
    prop2: 2,
    prop3: 3
}