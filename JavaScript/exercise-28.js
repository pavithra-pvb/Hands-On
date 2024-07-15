let athleteFinalPosition = 'first place';

//1. write a switch statement to decide what medal to award an athlete.
switch (athleteFinalPosition) {
//2. Inside the switch statement, add three cases:The first case checks for the value 'first place'.If the expression’s value matches the value of the case then console.log() the string 'You get the gold medal!'.The second case checks for the value 'second place'.If the expression’s value matches the value of the case then console.log() the string 'You get the silver medal!'.The third case checks for the value 'third place'.If the expression’s value matches the value of the case then console.log() the string 'You get the bronze medal!'
    case 'first place':
        console.log('You get the gold medal!');
        break;
    case 'second place':
        console.log('You get the silver medal!');
        break;
    case 'third place':
        console.log('You get the bronze medal!');
        break;
  //3. add a default statement at the end of the switch that uses console.log() to print 'No medal awarded.'.
    default:
        console.log('No medal awarded.');
        break;
}