import { getDrones, getDroneById } from "@/services/apiService"

export const drones = {
    loadDrones(context) {
      return getDrones()
        .then((response) => {
          context.commit('setDrones', { tasks: response.data })
        })
    },
    loadDrone(context, { id }) {
      return getDroneById(id)
        .then((response) => {
          context.commit('setDrone', { tasks: response.data })
        })
    },
}