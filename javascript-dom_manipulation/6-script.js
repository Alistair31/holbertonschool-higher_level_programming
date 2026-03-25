#!/usr/bin/node
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then(response => response.json())
    .then(data => {
        const character = document.getElementById("character");
        character.textContent = data.name;
    });