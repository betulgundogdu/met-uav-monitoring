import { defineStore } from 'pinia';
import router from '@/router';
import {login} from '@/services/apiService';

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        token: localStorage.getItem('token'),
        returnUrl: null
    }),
    actions: {
        async login(user) {
            const result = await login(user);

            if (result.status === 200) {
                // update pinia state
                this.token = result.data.access_token;

                // store user details and jwt in local storage to keep user logged in between page refreshes
                localStorage.setItem('token', this.token);

                // redirect to previous url or default to home page
                router.push('/dashboard');
            } else {
                console.log('sth wrong');
            } 
        },
        logout() {
            this.token = null;
            localStorage.removeItem('token');
            router.push('/');
        }
    }
});