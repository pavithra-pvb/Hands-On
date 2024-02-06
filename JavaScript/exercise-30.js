//Race Day Project

let raceNumber = Math.floor(Math.random() * 1000);
let registeredEarly = true;
let age = 41;

if (age > 18 && registeredEarly) {
  raceNumber += 1000;
}

if (age > 18 && registeredEarly) {
  console.log(`Race will begin at 9:30 am. Your race number is ${raceNumber}`);
} else if (age > 18 && !registeredEarly) {
  console.log(`You will race at 11:00 am. Your race number is ${raceNumber}`);
} else if (age < 18) {
  console.log(`You will race at 12:30 pm. Your race number is ${raceNumber}`);
} else {
  console.log('Please go to the registration desk');
}