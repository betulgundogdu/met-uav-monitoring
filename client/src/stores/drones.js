import { defineStore } from 'pinia';
import { getDrones } from "@/services/apiService";

export const useDroneStore = defineStore({
  id: 'drones',
  state: () => ({
      drones: null,
  }),
  actions: {
    async loadDrones() {
      return getDrones()
        .then((response) => {
          if (response.status === 200) {
            this.drones = response.data;
          }
        })
    }
  }
});