#!/usr/bin/node
const header = document.querySelectorAll("header");
const redHeader = document.getElementById("red_header");
redHeader.addEventListener("click", function() {
    header[0].style.color = "#ff0000";
});
