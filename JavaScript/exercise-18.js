//1. Create a variable named myAge, and set it equal to your age as a number
const myAge = 41;
//2. Create a variable named earlyYears and save the value 2 to it. Note, the value saved to this variable will change
let earlyYears = 2;

//3. Use the multiplication assignment operator to multiply the value saved to earlyYears by 10.5 and reassign it to earlyYears
earlyYears = earlyYears * 10.5;

//4. take the myAge variable, and subtract 2 from it.Set the result equal to a variable called laterYears. We’ll be changing this value later.s
let laterYears = myAge - 2;

//5. Multiply the laterYears variable by 4 to calculate the number of dog years accounted for by your later years.
laterYears = laterYears * 4;

//6. print earlyYears and laterYears to the console
console.log(earlyYears);
console.log(laterYears);

//7. Add earlyYears and laterYears together, and store that in a variable named myAgeInDogYears.
let myAgeInDogYears = earlyYears + laterYears;

//8. Write your name as a string, call its built-in method .toLowerCase(), and store the result in a variable called myName.
myName = 'Pavithra'.toLowerCase();

//9.Write a console.log statement that displays your name and age in dog years. Use string interpolation to display the value
console.log(`My Name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`)

