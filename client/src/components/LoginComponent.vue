<template>
    <div class="card w-96 h-2/3 shadow-xl bg-slate-200">
        <div class="card-body flex justify-center">
            <h1 class="text-gray-900">Login</h1>
            <label class="input input-bordered flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" /></svg>
                <input type="text" class="grow" placeholder="Username" v-model="username"/>
            </label>
            <label class="input input-bordered flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4 opacity-70"><path fill-rule="evenodd" d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z" clip-rule="evenodd" /></svg>
                <input type="password" class="grow" value="password" v-model="password" id="passwordInput"/>
                <span>
                    <input class="opacity-0" type="checkbox" @click="togglePassword">
                    <span class="togglePwd">
                        <span id="eye-hide">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-slash" viewBox="0 0 16 16">
                                <path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7 7 0 0 0-2.79.588l.77.771A6 6 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755q-.247.248-.517.486z"/>
                                <path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829"/>
                                <path d="M3.35 5.47q-.27.24-.518.487A13 13 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7 7 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12z"/>
                            </svg>
                        </span>
                        <span id="eye-open" class="hidden">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye" viewBox="0 0 16 16">
                                <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8M1.173 8a13 13 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5s3.879 1.168 5.168 2.457A13 13 0 0 1 14.828 8q-.086.13-.195.288c-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5s-3.879-1.168-5.168-2.457A13 13 0 0 1 1.172 8z"/>
                                <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5M4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0"/>
                            </svg>
                        </span>
                    </span>
                </span>
            </label>
            <div class="card-actions justify-end">
                <button class="btn btn-primary w-full" @click="onSubmit">Sign in</button>
            </div>
            <div class="w-full flex justify-between items-center">
                <span class="text-sm">Don't have an account? </span>
                <RouterLink to="/signup"><button class="btn bg-slate-50">Sign up</button></RouterLink>
            </div>
        </div>
    </div>
  </template>
  
<script setup>
    import { useAuthStore } from '@/stores'

    let username = "";
    let password = "";
    const store = useAuthStore();

    function onSubmit() {
        let formData = {
            username: username,
            password: password,
        }
        store.login(formData).then(() => {
            console.log('done');
        });
    };

    function togglePassword() {
        let pwdInput = document.getElementById("passwordInput");
        let eyeOpenSvg = document.getElementById("eye-open");
        let eyeHideSvg = document.getElementById("eye-hide");

        if (pwdInput.type === "password") {
            pwdInput.type = "text";
            eyeOpenSvg.classList.remove("hidden");
            eyeHideSvg.classList.add("hidden");
        } else {
            pwdInput.type = "password";
            eyeOpenSvg.classList.add("hidden");
            eyeHideSvg.classList.remove("hidden");
        }
    }
        
  </script>

<style scoped>
    .togglePwd svg {
        margin-top: -20px !important;
    }
</style>