import axios from 'axios'
import { useAuthStore } from '@/stores';


const axiosClient = axios.create({
  baseURL: `http://localhost:5000/api`
});

axiosClient.interceptors.request.use((config) => {
  const authStore = useAuthStore();
  config.headers.Authorization = `Bearer ${authStore.token}`;
  return config;
})

export function getDrones() {
  return axiosClient.get(`/drones`)
}

export function createDrone(drone) {
  return axiosClient.post(`/drones`, drone)
}

export function updateDrone(drone) {
  return axiosClient.put(`/drones/${drone.id}`, drone)
}

export function getTasks() {
  return axiosClient.get(`/tasks`)
}

export function getTaskById(id) {
  return axiosClient.get(`/tasks/${id}`)
}

export function createTask(task) {
  return axiosClient.post(`/tasks`, task)
}

export function updateTask(task) {
  return axiosClient.put(`/tasks/${task.id}`, task)
}
  
export function login(user) {
  return axiosClient.post(`/login`, user)
}

export function register(user) {
  return axiosClient.post(`/register`, user);
}
