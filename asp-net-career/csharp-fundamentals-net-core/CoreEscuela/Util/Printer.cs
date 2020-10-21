using static System.Console;

namespace CoreEscuela.Util
{
    public static class Printer
    {
        public static void DibujarLinea(int tam = 10)
        {
            var linea = string.Empty.PadLeft(tam, '=');
            WriteLine(linea);
        }

        public static void WriteTitle(string title)
        {
            var tamaño = title.Length + 4;
            DibujarLinea(tamaño);
            WriteLine($"| { title } |");
            DibujarLinea(tamaño);
        }

        public static void Pitar(int hz = 2000, int tiempo = 500, int cantidad = 1)
        {
            while (cantidad-- > 0)
            {
                Beep(hz, tiempo);                
            }
            
        }
    }
}