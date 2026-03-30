#!/usr/bin/node
const toggle_header = document.getElementById("toggle_header");
toggle_header.addEventListener("click", function () {
	if (header.classList === "green") {
		document.querySelector("header").classList.replace("red")
	} else if (header.classList === "red") {
		document.querySelector("header").classList.replace("green")
	}
});