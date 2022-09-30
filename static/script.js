/* Hides the body scrollbar when the overlay menu is opened */

// Get the body element
const body = document.body;

// Get the checkbox element
const hamburgerToggler = document.querySelector(".toggler");

// Set event listener to the hamburger toggler
// so that we can detect when the overlay is opened and hide the body scrollbar
hamburgerToggler.addEventListener("change", (e) => {
  e.target.checked
    ? (body.style.overflowY = "hidden")
    : (body.style.overflowY = "scroll");
});
let menu=document.getElementById('shaun')

menu.addEventListener("click",function(){
    console.log('button is clicked')

    document.getElementById('mynav').style.width="100%"

    


})
let clos=document.getElementById('close')

clos.addEventListener("click",function(){
    console.log('button is clicked')

    document.getElementById('mynav').style.width="0%"

    


})