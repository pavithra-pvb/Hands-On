let mood = 'sleepy';
let tirednessLevel = 6;

//1. create an if...else statement that checks if mood is 'sleepy' and tirednessLevel is greater than 8.If both conditions evaluate to true, then console.log() the string 'time to sleep'. Otherwise, we should console.log() 'not bed time yet'.
if (mood === 'sleepy' && tirednessLevel > 8) {
  console.log('time to sleep');
} else {
  console.log('not bed time yet');
}

// || operator

if (mood === 'sleepy' || tirednessLevel > 8) {
  console.log('time to sleep');
} else {
  console.log('not bed time yet');
}

// ! operator

if (!mood === 'sleepy' && tirednessLevel > 8) {
  console.log('time to sleep')
} else {
  console.log('not bed time yet');
}