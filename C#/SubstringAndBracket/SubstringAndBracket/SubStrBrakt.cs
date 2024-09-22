using System;

namespace DNA
{
    class SubStrBrakt
    {
        static void Main(string[] args)
        {
            // DNA strand
            string startStrand = "ATGCGATGAGCTTAC";

            // Find location of "tga"
            int tga = startStrand.IndexOf("TGA");

            // Start point and stop point variables
            int startPoint = 0;
            int length = tga + 3;

            // Define final strand
            string dna = startStrand.Substring(startPoint, length);
            Console.WriteLine(dna);

            // DNA mutation search
            Console.WriteLine(dna[3]);
        }
    }
}
