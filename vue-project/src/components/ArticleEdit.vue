<template>
    <div>
        <h4>게시글 수정</h4>
        <div>
            <form @submit="editArticle">
                <div class="m-4">
                    <label for="edit-title" class="me-2">제목 :</label>
                    <input type="text" name="edit-title" id="edit-title" v-model.trim="title">
                </div>
                <div class="m-4">
                    <label for="edit-content" class="me-2">내용 :</label>
                    <input type="text" name="edit-content" id="edit-content" v-model.trim="content">
                </div>
                <div>
                    <input type="submit" value="수정">
                    
                </div>
            </form>
            <button @click="$emit('switchType')">취소</button>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { useCounterStore } from '@/stores/counter.js';
import { ref, computed } from 'vue';

const store = useCounterStore()
const props = defineProps({
    articleId:Number
})
const title = ref('')
const content = ref('')
const token = computed(()=>{
    return store.token
})

const editArticle = function(){
    console.log(title)
    console.log(content)
    axios({
        url: `http://127.0.0.1:8000/article/articles/${props.articleId}/`,
        method:'put',
        data: {
            title: title.value,
            content: content.value
        },
        headers: {
            Authorization: `Token ${token.value}`
        }
    })
    .then(response => {
        console.log(response)
    })
    .catch(error => {
        console.log(error)
    })
}

</script>

<style scoped>

</style>