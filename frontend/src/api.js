import axios from "axios";


const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});


export async function sendMessage(message, pnr) {

    const response = await API.post("/chat", {
        message: message,
        pnr: pnr
    });

    return response.data;
}