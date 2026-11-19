const url = "https://api-libreria-gamma.vercel.app";
// 1º llamada

const btn_call1 = document.getElementById("btn-call1");
const api_calls1 = document.getElementById("api-calls1");

btn_call1.addEventListener("click", async () => {
    try {
        const response = await fetch(`${url}/books`);
        const data = await response.json();
        api_calls1.innerHTML = `${data.mensaje}`;
    } catch (error) {
        console.error("Error en la primera llamada:", error);
    }
});


// 2º llamada

const btn_call2 = document.getElementById("btn-call2");
const api_calls2 = document.getElementById("api-calls2");

btn_call2.addEventListener("click", async () => {
    try {
        const response = await fetch("http://localhost:3000/estado");
        const data = await response.json();
        api_calls2.innerHTML = `Estado del servidor: ${data.status}<br>${data.servidor}`;
    } catch (error) {
        console.error("Error en la segunda llamada:", error);
    }
});

// 3º llamada

const btn_call3 = document.getElementById("btn-call3");
const api_calls3 = document.getElementById("api-calls3");
const tituloInput = document.getElementById("titulo");
const autorInput = document.getElementById("autor");
const anioInput = document.getElementById("anio");

btn_call3.addEventListener("click", async () => {
    try {
        const response = await fetch("http://localhost:3000/libros_registro", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                titulo: tituloInput.value,
                autor: autorInput.value,
                anio: parseInt(anioInput.value)
            })
        });
        const data = await response.json();
        const libroRegistrado =  data.libro_recibido;
        api_calls3.innerHTML = `Libro registrado: ${libroRegistrado.titulo} por ${libroRegistrado.autor} (${libroRegistrado.anio})`;
    } catch (error) {
        console.error("Error en la tercera llamada:", error);
    }
});

// 4º llamada

const btn_call4 = document.getElementById("btn-call4");
const api_calls4 = document.getElementById("api-calls4");
const usuario_id = document.getElementById("usuario_id");

btn_call4.addEventListener("click", async () => {
    try {
        const response = await fetch(`http://localhost:3000/usuarios/${usuario_id.value}`);
        const data = await response.json();
        api_calls4.innerHTML = `Usuario encontrado: ${data.id_objetivo}`;
    } catch (error) {
        console.error("Error en la cuarta llamada:", error);
    }
});

// 5º llamada

const btn_call5 = document.getElementById("btn-call5");
const api_calls5 = document.getElementById("api-calls5");
const autor = document.getElementById("autor_name");
// Agrega este log para verificar el valor

btn_call5.addEventListener("click", async () => {
    try {
        let url = `http://localhost:3000/buscar`;
        if (autor.value !== "") {
            url += `?autor=${autor.value}`;
        }
        const response = await fetch(url);
        const data = await response.json();
        api_calls5.innerHTML = "";
        data.forEach(libro => {
            api_calls5.innerHTML += `<br>${libro.titulo} por ${libro.autor}`;
        });
    } catch (error) {
        console.error("Error en la quinta llamada:", error);
    }
});