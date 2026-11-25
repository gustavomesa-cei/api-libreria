const url = "https://api-libreria-gamma.vercel.app";

// 01º llamada

const btn_call01 = document.getElementById("btn-call01");
const api_calls01 = document.getElementById("api-calls01");
const usuarioCreateInput = document.getElementById("usuario_create");
const claveCreateInput = document.getElementById("clave_create");

btn_call01.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/users/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nombre: usuarioCreateInput.value,
                clave: claveCreateInput.value
            })
        });
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem("token", data);
            api_calls01.innerHTML = "Usuario registrado exitosamente.";
        } else {
            api_calls01.innerHTML = `Error: ${data.detail}`;
        }
    } catch (error) {
        console.error("Error en la llamada de registro:", error);
    }
});

// 0º llamada

const btn_call0 = document.getElementById("btn-call0");
const api_calls0 = document.getElementById("api-calls0");
const usuarioInput = document.getElementById("usuario");
const claveInput = document.getElementById("clave");

btn_call0.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/users/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nombre: usuarioInput.value,
                clave: claveInput.value
            })
        });
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem("token", data);
            api_calls0.innerHTML = "Inicio de sesión exitoso. Token almacenado en localStorage.";
        } else {
            api_calls0.innerHTML = `Error: ${data.detail}`;
        }
    } catch (error) {
        console.error("Error en la llamada de inicio de sesión:", error);
    }
});


// 1º llamada

const btn_call1 = document.getElementById("btn-call1");
const api_calls1 = document.getElementById("api-calls1");

btn_call1.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/books`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
        });
        const data = await response.json();
        api_calls1.innerHTML = "";
        data.forEach(libro => {
            api_calls1.innerHTML += `<div class="api-call-result">id: ${libro.id} - ${libro.titulo} por ${libro.autor} en el año ${libro.anio}<br></div>`;
        });
    } catch (error) {
        api_calls1.innerHTML =  "Error al obtener los libros. Asegúrate de haber iniciado sesión correctamente.";
    }
});


// 2º llamada

const btn_call2 = document.getElementById("btn-call2");
const api_calls2 = document.getElementById("api-calls2");
const tituloInput = document.getElementById("titulo");
const autorInput = document.getElementById("autor");
const anioInput = document.getElementById("anio");

btn_call2.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/books`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify({
                titulo: tituloInput.value,
                autor: autorInput.value,
                anio: parseInt(anioInput.value)
            })
        });
        const data = await response.json();
        console.log(data);
        api_calls2.innerHTML = data.mensaje;
    } catch (error) {
        api_calls2.innerHTML = "Error al agregar el libro. Asegúrate de haber iniciado sesión correctamente.";
    }
});

// 3º llamada

const btn_call3 = document.getElementById("btn-call3");
const api_calls3 = document.getElementById("api-calls3");
const id_edit = document.getElementById("id_edit");
const anio_edit = document.getElementById("anio_edit");


btn_call3.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/books/${id_edit.value}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
            body: JSON.stringify({
                anio: parseInt(anio_edit.value)
            })
        });
        const data = await response.json();
        api_calls3.innerHTML = data.mensaje;
    } catch (error) {
        api_calls3.innerHTML = "Error al actualizar el libro. Asegúrate de haber iniciado sesión correctamente.";
    }
});

// 4º llamada

const btn_call4 = document.getElementById("btn-call4");
const api_calls4 = document.getElementById("api-calls4");
const delete_id = document.getElementById("delete_id");

btn_call4.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/books/${delete_id.value}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            },
        });
        const data = await response.json();
        api_calls4.innerHTML = data.mensaje;
    } catch (error) {
        api_calls4.innerHTML = "Error al eliminar el libro. Asegúrate de haber iniciado sesión correctamente.";
    }
});
