using System;

namespace StoryTime
{
    class StringConcat
    {
        static void Main(string[] args)
        {
            // Declare the variables
            string beginning = "Once upon a time,";
            string middle = " there was a boy,";
            string end = " who avoided going to school.";

            // Concatenate the string and the variables
            string story = beginning + middle + end;

            // Print the story to the console 
            Console.WriteLine(story);
        }
    }
}
