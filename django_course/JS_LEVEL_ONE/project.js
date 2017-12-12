alert('Hello and welcome to this website');
var firstName = prompt('What is your first name?');
console.log(firstName[0]);
var lastName = prompt('What is your last name?');
console.log(lastName[0]);
var height = prompt('How tall are you?');
console.log(height);
var pet = prompt('What is your pet\'s name?');
console.log(pet[pet.length - 1]);
alert('Thank you for the information');
if(firstName[0] === lastName[0] && height >= 170 && pet[pet.length - 1] === 'y'){
  console.log('Welcome comrade.');
} else {
  console.log('Nothing to see here.');
}
