let isLocked = false;

if (isLocked) {
  console.log('You will need a key to open the door.');
} else {
  console.log('You will not need a key to open the door.');
}

// 1. ternary output
isLocked ? console.log('You will need a key to open the door.')
: console.log('You will not need a key to open the door.');

let isCorrect = true;

if (isCorrect) {
  console.log('Correct!');
} else {
  console.log('Incorrect!');
}

//2. ternary output
isCorrect ? console.log('Correct!')
: console.log('Incorrect!');


let favoritePhrase = 'Love That!';

if (favoritePhrase === 'Love That!') {
  console.log('I love that!');
} else {
  console.log("I don't love that!");
}

//3. ternary output
favoritePhrase === 'Love That!' ? console.log('I love that!')
: console.log("I don't love that!");