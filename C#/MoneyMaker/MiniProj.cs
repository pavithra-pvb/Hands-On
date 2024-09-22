using System;

namespace MoneyMaker
{
    class MiniProj
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Money Maker!");
            Console.WriteLine("\nEnter amount to convert to coins :");
            string totalAsString = Console.ReadLine();
            double totalAsNumber = Convert.ToDouble(totalAsString);
            Console.WriteLine($"{totalAsNumber} cents is equal to: ");

            // Define the coin values
            int goldValue = 10;
            int silverValue = 5;

            // Calculate the change
            double goldCoins = Math.Floor(totalAsNumber / goldValue);
            double remainder = totalAsNumber % goldValue;
            
            double silverCoins = Math.Floor(remainder / silverValue);
            remainder = remainder % silverValue;
            
            // Print all the coins
            Console.WriteLine($"Gold Coins: {goldCoins}");
            Console.WriteLine($"Silver Coins: {silverCoins}");
            Console.WriteLine($"Bronze Coins: {remainder}");

        }
    }
}