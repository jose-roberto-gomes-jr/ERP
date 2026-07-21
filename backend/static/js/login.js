const registerForm = document.querySelector("#register-form");

registerForm.addEventListener("submit", async (event) => {

    event.preventDefault();

       const nome = document.querySelector("#signup-name");
       const email = document.querySelector("#signup-email");
       const senha = document.querySelector("#signup-pass");
    
    const usuario = {
        nome: nome.value,
        email: email.value,
        senha: senha.value
    };

    const resposta = await fetch ("/auth/cadastrar", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },

        body: JSON.stringify(usuario)



    })
})

