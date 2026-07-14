import axios from "axios";

const api = axios.create({
  baseURL: "https://mohamed-z-ai-production-448c.up.railway.app",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;