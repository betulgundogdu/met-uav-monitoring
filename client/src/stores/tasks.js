import { getTasks, getTaskById } from "@/services/apiService"

export const tasks = {
    loadTasks(context) {
      return getTasks()
        .then((response) => {
          context.commit('setTasks', { tasks: response.data })
        })
    },
    loadTask(context, { id }) {
      return getTaskById(id)
        .then((response) => {
          context.commit('setTask', { tasks: response.data })
        })
    },
}