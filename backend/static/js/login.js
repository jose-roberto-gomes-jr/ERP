const registerForm = document.querySelector("#register-form");

registerForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const usuario = {
        nome: document.querySelector("#signup-name").value,
        email: document.querySelector("#signup-email").value,
        senha: document.querySelector("#signup-pass").value
    }

    console.log(usuario)

})