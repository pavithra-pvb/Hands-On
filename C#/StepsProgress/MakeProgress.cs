using System;

namespace StepsProgress
{
    class MakeProgress
    {
        static void Main(string[] args)
        {
            // Declare steps variable
            int steps = 0;

            // Two steps forward 
            steps += 2;

            // One step back 
            steps -= 1;

            // Print result to the console
            Console.WriteLine(steps);
        }
    }
}
