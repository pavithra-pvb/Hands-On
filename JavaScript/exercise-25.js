let tool = '';

// Use short circuit evaluation to assign  writingUtensil variable below:

//reassign the value of tool to 'marker'
//tool = 'marker';

//Assign to writingUtensil the value of tool and if tool is falsy, assign a default value of 'pen'.
let writingUtensil = tool || 'pen';

console.log(`The ${writingUtensil} is mightier than the sword.`);