const loginForm = document.querySelector("#login-form");

loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.querySelector("#login-email");
    const senha = document.querySelector("#login-pass");

    const usuario = {
        email: email.value,
        senha: senha.value
    };

    const resposta = await fetch("/auth/login", {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(usuario)
    });

    const dados = await resposta.json();

    if (resposta.ok) {
        window.location.href = "/dashboard";
    } else {
        alert(dados.detail);
    }
});