import axios from 'axios'

const API_ENDPOINT = `http://localhost:5000/api`;

export function getDrones() {
  return axios.get(`${API_ENDPOINT}/drones/`)
}

export function createDrone(drone) {
  return axios.post(`${API_ENDPOINT}/drones/`, drone)
}

export function updateDrone(drone) {
  return axios.put(`${API_ENDPOINT}/drones/${drone.id}`, drone)
}

export function getTasks() {
  return axios.get(`${API_ENDPOINT}/tasks/`)
}

export function getTaskById(id) {
  return axios.get(`${API_ENDPOINT}/tasks/${id}`)
}

export function createTask(task) {
  return axios.post(`${API_ENDPOINT}/tasks/`, task)
}

export function updateTask(task) {
  return axios.put(`${API_ENDPOINT}/tasks/${task.id}`, task)
}
  
export function login(user) {
  return axios.post(`${API_ENDPOINT}/login`, user)
}

export function register(user) {
  return axios.post(`${API_ENDPOINT}/register`, user, {
    withCredentials: true
  });
}
