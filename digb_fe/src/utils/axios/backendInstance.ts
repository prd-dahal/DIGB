import axios from "axios";

const backEndAxios = axios.create({
  baseURL: process.env.NEXT_PUBLIC_BACKEND_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "*/*",
  },
});

export { backEndAxios };
