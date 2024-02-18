#!/usr/bin/node

/** Star Wars Characters - Using the request module
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as  list in the /films/ endpoint
 */

const request = require('request');
const filmId = process.argv[2] + '/';
const urlApi = 'https://swapi-api.hbtn.io/api/films/';

// query API
request(urlApi + filmId, async (err, res, body) => {
  if (err) return console.error(err);

  // find URLs of each character in the film as a list obj
  const characters = JSON.parse(body).characters;
  showNames(characters);
});
// show results on the console
const showNames = (names, i = 0) => {
  if (i === names.length) return;
  request(names[i], (error, response, body) => {
    if (error) throw error;
    // finds each character name and prints in URL order
    console.log(JSON.parse(body).name);
    showNames(names, i + 1);
  });
};
