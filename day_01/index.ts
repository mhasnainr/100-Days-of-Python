// Q1: Q1 - Install Node.js, TypeScript and VS Code on your computer.

// Initial steps:
// - in cmd, write ' tsc --init '
// - make .ts file
// - in cmd, write 'tsc && node index.ts'

//

// Q2 - Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

let fullName = "aLi haShir";
console.log("Hi ", fullName, "! Hope you are fine");

//

// Q3 - Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

console.log(fullName.toLowerCase());
//
console.log(fullName.toUpperCase());
//

// error in titlecase: it is converting only first word, nor more than that
console.log(fullName.charAt(0).toUpperCase() + fullName.slice(1).toLowerCase());
