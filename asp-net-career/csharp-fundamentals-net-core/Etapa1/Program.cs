using System;
using CoreEscuela.Entidades;
using static System.Console;

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
                pais: "Bolivia"
            );
            Console.WriteLine(escuela2);

            var curso3 = new Curso()
            {
                Nombre = "101"
            };

            var curso4 = new Curso()
            {
                Nombre = "201"
            };

            var curso5 = new Curso()
            {
                Nombre = "301"
            };

            System.Console.WriteLine("===========");
            System.Console.WriteLine(curso3.Nombre + ", " + curso3.UniqueId);
            System.Console.WriteLine($"{curso4.Nombre} , {curso4.UniqueId}");
            System.Console.WriteLine(curso5);

            var arregloCursos = new Curso[3]
            {
                new Curso() { Nombre = "101"},
                new Curso() { Nombre = "201" },
                new Curso{ Nombre = "301"}
            };

            arregloCursos = new Curso[]
            {
                new Curso() { Nombre = "101"},
                new Curso() { Nombre = "201" },
                new Curso{ Nombre = "301"}
            };

            Curso[] arregloCursos2 = {
                new Curso() { Nombre = "101"},
                new Curso() { Nombre = "201" },
                new Curso{ Nombre = "301"}
            };

            escuela.Cursos = arregloCursos;
            //escuela = null;
            ImprimirCursosEscuela(escuela);

            // System.Console.WriteLine(escuela);
            // System.Console.WriteLine("==============");
            // System.Console.WriteLine("While");
            // ImprimirCursosWhile(arregloCursos);
            // System.Console.WriteLine("DoWhile");
            // ImprimirCursosDoWhile(arregloCursos);
            // System.Console.WriteLine("For");
            // ImprimirCursosFor(arregloCursos);
            // System.Console.WriteLine("Foreach");
            // ImprimirCursosForEach(arregloCursos);
        }

        private static void ImprimirCursosEscuela(Escuela escuela)
        {
            WriteLine("===============");
            WriteLine("Cursos Escuela");
            WriteLine("===============");
            
            if (escuela?.Cursos != null)
            {
                foreach (var curso in escuela.Cursos)
                {
                    WriteLine($"Nombre { curso.Nombre }, Id { curso.UniqueId }");
                }    
            }            
        }

        private static void ImprimirCursosWhile(Curso[] arregloCursos)
        {
            int contador = 0;
            while (contador < arregloCursos.Length)
            {
                Console.WriteLine($"Nombre {arregloCursos[contador].Nombre}, Id {arregloCursos[contador].UniqueId}");
                contador++;
            }
        }

        private static void ImprimirCursosDoWhile(Curso[] arregloCursos)
        {
            int contador = 0;
            do
            {
                Console.WriteLine($"Nombre {arregloCursos[contador].Nombre}, Id {arregloCursos[contador].UniqueId}");
                contador++;
            } while (contador < arregloCursos.Length);
        }

        private static void ImprimirCursosFor(Curso[] arregloCursos)
        {
            for (int i = 0; i < arregloCursos.Length; i++)
            {
                Console.WriteLine($"Nombre {arregloCursos[i].Nombre}, Id {arregloCursos[i].UniqueId}");
            }
        }

        private static void ImprimirCursosForEach(Curso[] arregloCursos)
        {
            foreach (var curso in arregloCursos)
            {
                Console.WriteLine($"Nombre { curso.Nombre }, Id { curso.UniqueId }");
            }
        }
    }
}
