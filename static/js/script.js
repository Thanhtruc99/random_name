function getFiltres() {
  const filtres = [];
  if (document.querySelector('input[name="court"]').checked) filtres.push("court=on");
  if (document.querySelector('input[name="long"]').checked) filtres.push("long=on");
  if (document.querySelector('input[name="voyelle"]').checked) filtres.push("voyelle=on");

  if (document.querySelector('input[name="court_nom"]').checked) filtres.push("court_nom=on");
  if (document.querySelector('input[name="long_nom"]').checked) filtres.push("long_nom=on");
  if (document.querySelector('input[name="voyelle_nom"]').checked) filtres.push("voyelle_nom=on");

  return filtres.join("&");
}

function genererPrenoms() {
  const genre = document.getElementById('genre').value;
  const nombre = document.getElementById('nombre').value;
  const filtres = getFiltres();
  window.location.href = `/generer_prenoms?nombre=${nombre}&genre=${genre}&${filtres}`;
}

function genererNoms() {
  const genre = document.getElementById('genre').value;
  const nombre = document.getElementById('nombre').value;
  const filtres = getFiltres();
  window.location.href = `/generer_noms?nombre=${nombre}&genre=${genre}&${filtres}`;
}

function genererTout(event) {
  event.preventDefault();
  const genre = document.getElementById('genre').value;
  const nombre = document.getElementById('nombre').value;
  const filtres = getFiltres();
  window.location.href = `/generer_tout?nombre=${nombre}&genre=${genre}&${filtres}`;
}

document.addEventListener("DOMContentLoaded", function () {
  const courtCheckbox = document.querySelector('input[name="court"]');
  const longCheckbox = document.querySelector('input[name="long"]');
  const courtNomCheckbox = document.querySelector('input[name="court_nom"]');
  const longNomCheckbox = document.querySelector('input[name="long_nom"]');

  if (courtCheckbox && longCheckbox) {
    courtCheckbox.addEventListener("change", () => {
      if (courtCheckbox.checked) longCheckbox.checked = false;
    });

    longCheckbox.addEventListener("change", () => {
      if (longCheckbox.checked) courtCheckbox.checked = false;
    });
  }

  if (courtNomCheckbox && longNomCheckbox) {
    courtNomCheckbox.addEventListener("change", () => {
      if (courtNomCheckbox.checked) longNomCheckbox.checked = false;
    });

    longNomCheckbox.addEventListener("change", () => {
      if (longNomCheckbox.checked) courtNomCheckbox.checked = false;
    });
  }
});
