"use strict";
// Q1: Q1 - Install Node.js, TypeScript and VS Code on your computer.
// Initial steps:
// - in cmd, write ' tsc --init '
// - make .ts file
// - in cmd, write 'tsc && node index.ts'
// Q2 - Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
let personName = "aLi";
console.log("Hi ", personName, "! Hope you are fine");
// Q3 - Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
console.log(personName.toLowerCase());
console.log(personName.toUpperCase());
// Error: titlecase part
// function toTitleCase(name: string): string {
//   return name
//     .split(" ")
//     .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
//     .join(" ");
// }
// const personName: string = "john doe";
// console.log(toTitleCase(personName)); // Output: "John Doe"
