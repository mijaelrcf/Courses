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

            var curso3 = new Curso() {
                Nombre = "101"
            };
            
            var curso4 = new Curso() {
                Nombre = "201"
            };

            var curso5 = new Curso() {
                Nombre = "301"                
            };
            
            System.Console.WriteLine("===========");
            System.Console.WriteLine(curso3.Nombre + ", " + curso3.UniqueId);
            System.Console.WriteLine($"{curso4.Nombre} , {curso4.UniqueId}");
            System.Console.WriteLine(curso5);

            var arregloCursos = new Curso[3];
            arregloCursos[0] = new Curso()            
            {
                Nombre = "101"
            };

            var curso2 = new Curso()
            {
              Nombre = "201"  
            };
            arregloCursos[1] = curso2;

            arregloCursos[2] = new Curso
            {
                Nombre = "301"
            };

            System.Console.WriteLine(escuela);
            System.Console.WriteLine("==============");
            ImprimirCursos(arregloCursos);
        }

        private static void ImprimirCursos(Curso[] arregloCursos)
        {
            int contador = 0;
            while (contador < arregloCursos.Length)
            {
                Console.WriteLine($"Nombre {arregloCursos[contador].Nombre}, Id {arregloCursos[contador].UniqueId}");
                contador = contador++;
            }
        }
    }
}
