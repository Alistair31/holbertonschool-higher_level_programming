#!/usr/bin/node
const header = document.querySelectorAll("header");
const toggle_header = document.getElementById("toggle_header");
toggle_header.addEventListener("click", function() {
    if (header[0].style.color === "rgb(255, 0, 0)") {
        header[0].style.color = "#00FF00";
    } else {
        header[0].style.color = "#ff0000";
    }
});