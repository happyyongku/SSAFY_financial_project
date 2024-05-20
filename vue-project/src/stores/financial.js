import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useFinancialStore = defineStore('financial', () => {
    const exchangeRate1 = ref(null)
    const exchangeRate2 = ref(null)
    const API_URL = 'http://127.0.0.1:8000'
    const router = useRouter()
    const product1 = ref(null)
    const product2 = ref(null)

    const get_bank = function() {
        axios({
            url : `${API_URL}/search/bank/`,
            method:'get'
        })
        
    }

    const compareProduct = function() {

    }
    
})