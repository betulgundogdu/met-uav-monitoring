<template>
    <div class="w-full h-screen flex flex-col">
        <div class="flex md:w-full justify-center">
            <img src="https://droneqube.com.tr/wp-content/uploads/2023/03/droneqube_logo-250x30.png"/>
        </div>
        <div class="w-full md:w-full h-5/6 flex justify-center items-center">
            <SignupComponent />
        </div>
    </div>
  </template>

<script setup>
  import { SignupComponent } from '@/components'; 
</script>