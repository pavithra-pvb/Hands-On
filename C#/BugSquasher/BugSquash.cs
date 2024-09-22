using System;

namespace BugSquasher
{
    class BugSquash
    {
        static void Main(string[] args)
        {
            /* int number = 38498.3222; */ //has wrong data type
            double number = 38498.3222;

           /* dinosaur = "Barney"; */ // missing a data type
            string dinosaur = "Barney";

            /* double lock = 293.000; */ //lock is a reserved keyword and can't be used
            double locks = 293.000;

            /* bool is.yes = true; */ //is.yes is an illegal variable name
            bool is_yes = true;

            /* string band = "The Low Anthem" */ // missing semicolon
            string band = "The Low Anthem";

            // Print Variables
            Console.WriteLine(number);
            Console.WriteLine(dinosaur);
            Console.WriteLine(locks);
            Console.WriteLine(is_yes);
            Console.WriteLine(band);
        }
    }
}