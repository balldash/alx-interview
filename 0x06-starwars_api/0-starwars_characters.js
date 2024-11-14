#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: node script_name.js <movie_id>');
    process.exit(1);
}

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error('Error fetching film details:', error);
        return;
    }

    if (response.statusCode === 200) {
        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        characters.forEach(characterUrl => {
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Error fetching character details:', charError);
                    return;
                }

                if (charResponse.statusCode === 200) {
                    const characterData = JSON.parse(charBody);
                    console.log(characterData.name);
                } else {
                    console.error(`Error fetching character details: ${charResponse.statusCode}`);
                }
            });
        });
    } else {
        console.error(`Error fetching film details: ${response.statusCode}`);
    }
});
