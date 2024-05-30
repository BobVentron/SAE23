(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Récupère tous les formulaires qui nécessitent une validation
        var forms = document.getElementsByClassName('needs-validation');
        // Parcourt chaque formulaire et empêche la soumission si la validation échoue
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();  // Empêche la soumission
                    event.stopPropagation(); // Arrête la propagation de l'événement
                }
                form.classList.add('was-validated'); // Ajoute une classe pour indiquer que le formulaire a été validé
            }, false);
        });
    }, false);
})();

/**
 * Affiche le formulaire correspondant à la table et l'index donnés,
 * et cache les autres formulaires de la même table.
 *
 * @param {string} table - Le nom de la table.
 * @param {number} index - L'index du formulaire à afficher.
 */
function afficherFormulaire(table, index) {
    var formId = "form-" + table + "-" + index;
    var formulaire = document.getElementById(formId);
    var forms = document.getElementsByClassName("form-" + table);
    
    // Cache tous les formulaires de la même table
    for (var i = 0; i < forms.length; i++) {
        forms[i].style.display = "none";
    }
    
    // Affiche le formulaire sélectionné
    formulaire.style.display = "block";
}

/**
 * Affiche ou cache le formulaire de la partie.
 */
function afficherFormulaire1() {
    var formulaire = document.getElementById('formulairePartie');
    if (formulaire.style.display === "none" || formulaire.style.display === "") {
        formulaire.style.display = "block";
    } else {
        formulaire.style.display = "none";
    }
}

/**
 * Affiche ou cache le formulaire de la partie correspondant à l'index donné.
 *
 * @param {string} d - L'identifiant unique du formulaire.
 */
function afficherFormulaire2(d) {
    var formulaire = document.getElementById('formulairePartie2' + d);
    if (formulaire.style.display === "none" || formulaire.style.display === "") {
        formulaire.style.display = "block";
    } else {
        formulaire.style.display = "none";
    }
}

/**
 * Redirige l'utilisateur vers l'URL pour supprimer une table.
 *
 * @param {string} table - Le nom de la table à supprimer.
 */
function deleteTable(table) {
    window.location.href = "/Supprimer?table=" + table;
}

/**
 * Redirige l'utilisateur vers l'URL pour modifier une table.
 *
 * @param {string} table - Le nom de la table à modifier.
 */
function modifTable(table) {
    window.location.href = "/Modifier?table=" + table;
}