using System;
using System.Collections.Generic;
using CoreEscuela.Entidades;
using static System.Console;

namespace Etapa1
{
    class Program
    {
        static void Main(string[] args)
        {
            //EtapaUno();
            //EtapaDos();
            EtapaTres();
        }

        private static void EtapaUno()
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

            System.Console.WriteLine(escuela);
        }

        private static void EtapaDos()
        {
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

            bool rta = 10 == 10;
            int cantidad = 10;

            if (rta == false)
            {
                //hago algo
                WriteLine("Se cumplio la condicion 1");
            }
            else if (cantidad > 15)
            {
                //hago otra cosa
                WriteLine("Se cumplio la condicion 2");
            }
            else
            {
                //hacer otra cosa si no cumple
                WriteLine("NO se cumplio la condicion 2");
            }

            System.Console.WriteLine("While");
            ImprimirCursosWhile(arregloCursos);
            System.Console.WriteLine("DoWhile");
            ImprimirCursosDoWhile(arregloCursos);
            System.Console.WriteLine("For");
            ImprimirCursosFor(arregloCursos);
            System.Console.WriteLine("Foreach");
            ImprimirCursosForEach(arregloCursos);
        }

        private static void EtapaTres()
        {
            var escuela = new Escuela("Platzi Academy", 2020);

            var listaCursos = new List<Curso>()
            {
                new Curso() { Nombre = "101", Jornada = TiposJornada.Mañana },
                new Curso() { Nombre = "201", Jornada = TiposJornada.Mañana },
                new Curso{ Nombre = "301", Jornada = TiposJornada.Mañana }
            };

            escuela.ListCursos = listaCursos;

            escuela.ListCursos.Add(new Curso() { Nombre = "102", Jornada = TiposJornada.Tarde });
            escuela.ListCursos.Add(new Curso() { Nombre = "202", Jornada = TiposJornada.Tarde });

            var otraCollection = new List<Curso>()
            {
                new Curso() { Nombre = "401", Jornada = TiposJornada.Mañana },
                new Curso() { Nombre = "501", Jornada = TiposJornada.Mañana },
                new Curso{ Nombre = "502", Jornada = TiposJornada.Tarde }
            };

            Curso tmp = new Curso{Nombre = "101-Vacacional", Jornada = TiposJornada.Noche };
            //otraCollection.Clear();            
            
            escuela.ListCursos.AddRange(otraCollection);
            //escuela.ListCursos.Add(tmp);

            ImprimirCursosEscuela(escuela);
            WriteLine("Curso.Hash: " + tmp.GetHashCode());

            // Predicado
            //Predicate<Curso>  miAlgoritmo = Predicado;
            //escuela.ListCursos.RemoveAll(miAlgoritmo);
            
            // Delegados
            escuela.ListCursos.RemoveAll(delegate(Curso cur) 
            {
                return cur.Nombre == "301";
            });

            // Expresiones Lambda
            escuela.ListCursos.RemoveAll((cur) => cur.Nombre == "501" && cur.Jornada == TiposJornada.Mañana);

            escuela.ListCursos.Remove(tmp);
            ImprimirCursosEscuela(escuela);

            
        }

        private static int PredicadoMalHecho(string abc)
        {
            return 101;
        }

        private static bool Predicado(Curso curobj)
        {
            return curobj.Nombre == "301";
        }
        private static void ImprimirCursosEscuela(Escuela escuela)
        {
            WriteLine("===============");
            WriteLine("Cursos Escuela");
            WriteLine("===============");

            if (escuela?.ListCursos != null)
            {
                // foreach (var curso in escuela.Cursos)
                // {
                //     WriteLine($"Nombre { curso.Nombre }, Id { curso.UniqueId }");
                // }
                foreach (var curso in escuela.ListCursos)
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
