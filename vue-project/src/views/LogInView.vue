<template>
  <div class="d-flex justify-content-center align-items-center min-vh-100">
    <div class="card" style="width: 24rem;">
      <div class="card-body">
        <h2 class="card-title text-center">로그인</h2>
        <form @submit.prevent="logIn">
          <div data-mdb-input-init id="username-form" class="form-outline mb-4">
            <input type="text" v-model.trim="username" id="username" class="form-control" placeholder="username">
          </div>
          <div data-mdb-input-init id="password-form" class="form-outline mb-4">
            <input type="password" v-model.trim="password" id="password" class="form-control" placeholder="password">
          </div>
          <div class="d-flex justify-content-center">
            <input type="submit" class="btn btn-primary mb-4" value="로그인">
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style>
input {
  text-align: center;
}
</style>
