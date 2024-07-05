<template>
  <div class="d-flex justify-content-center align-items-center min-vh-100">
    <div class="card" style="width: 24rem;">
      <div class="card-body border border-3 p-3">
        <h3 class="card-title text-center">회원가입</h3>
        <form @submit.prevent="signUp">
          <div data-mdb-input-init id="username-form" class="form-outline mb-4 border border-3">
            <input type="text" v-model.trim="username" id="username" class="form-control" placeholder="username">
          </div>
          <div data-mdb-input-init id="password1-form" class="form-outline mb-4 border border-3">
            <input type="password" v-model.trim="password1" id="password1" class="form-control" placeholder="password">
          </div>
          <div data-mdb-input-init id="password2-form" class="form-outline mb-4 border border-3">
            <input type="password" v-model.trim="password2" id="password2" class="form-control" placeholder="password confirmation">
          </div>
          <div class="d-flex justify-content-center">
            <input type="submit" class="btn btn-primary mb-4" value="회원가입">
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
const password1 = ref(null)
const password2 = ref(null)
const store = useCounterStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}
</script>

<style>
input {
  text-align: center;
}
</style>
