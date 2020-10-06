using System;
using CoreEscuela.Entidades;

namespace Etapa1
{
    class Program
    {
        static void Main(string[] args)
        {
            var escuela = new Escuela("Platzi Academy", 2012);
            escuela.Pais = "Colombia";
            escuela.Ciudad = "Bogota";
            escuela.TipoEscuela = TiposEscuela.Primaria;
            
            Console.WriteLine(escuela);
            
            var escuela2 = new Escuela("Platzi Academy", 2012, TiposEscuela.PreEscolar,
                pais:"Bolivia"
            );
            Console.WriteLine(escuela2);
        }
    }
}
