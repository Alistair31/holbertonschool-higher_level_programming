#!/usr/bin/node
const header = document.querySelectorAll("header");
const update_header = document.getElementById("update_header");
update_header.addEventListener("click", function() {
    header[0].textContent = "New Header!!!";
});