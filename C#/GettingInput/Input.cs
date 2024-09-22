using System;

namespace GettingInput
{

    class Input
    {
        static void Main()
        {
            Console.WriteLine("How old are you?");
            string input = Console.ReadLine();
            Console.WriteLine($"You are {input} years old");
        }
    }
}