using System;

namespace FavoriteNumber
{
    class FavNum
    {
        static void Main(string[] args)
        {
            // Ask user for fave number
            Console.Write("Enter your favorite number!: ");
            int faveNumber = Convert.ToInt32(Console.ReadLine());

            // Turn that answer into an int
            Console.WriteLine(faveNumber);
            double num = 3;
           
            Console.WriteLine(num + 2);
           
            Console.WriteLine(num % 2);
            Console.WriteLine(num.ToUpper());
            Console.WriteLine(Math.Sqrt(num));

        }
    }
}