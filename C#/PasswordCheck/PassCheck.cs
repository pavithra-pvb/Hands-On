using System;

namespace PasswordCheck
{
    class PassCheck
    {
        static void Main(string[] args)
        {
            // Create password
            string password = "a9230!j2add";

            // Get password length
            int passwordLength = password.Length;

            // Check if password uses symbol
            int passwordCheck = password.IndexOf("!");

            // Print results
            Console.WriteLine($"The user password is {password}. Its length is {passwordLength} and it receives a {passwordCheck} check.");

        }
    }
}
