let season = 'summer';

if (season === 'spring') {
  console.log('It\'s spring! The trees are budding!');
// 1. add an else if statement that checks if season is equal to 'winter'.Inside the code block of the else if statement, add a console.log() that prints the string 'It\'s winter! Everything is covered in snow.'.
} else if (season === 'winter') {
  console.log('It\'s winter! Everything is covered in snow.');

//2. another else if statement that checks if season is equal to 'fall'.Inside the code block of the else if statement you just created, add a console.log() that prints the string 'It\'s fall! Leaves are falling!'.
} else if (season === 'fall') {
  console.log('It\'s fall! Leaves are falling!');

//3. else if statement that checks if season is equal to 'summer'.Inside the code block of the else if statement you just created, add a console.log() that prints the string 'It\'s sunny and warm because it\'s summer!'.
} else if (season === 'summer') {
  console.log('It\'s sunny and warm because it\'s summer!');
} else {
  console.log('Invalid season.');
}
