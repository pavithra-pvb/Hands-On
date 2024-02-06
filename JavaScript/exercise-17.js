//1.  create a variable named kelvin, and set it equal to 293
//const kelvin = 293;

//What’s 0 Kelvin in Fahrenheit?
const kelvin = 0;

//2. convert Kelvin to Celsius by subtracting 273 from the kelvin variable
const celsius = kelvin - 273;

//3. calculate Fahrenheit
let fahrenheit = celsius * (9/5) + 32;

//4. round down the Fahrenheit temperature
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);