<template>
    <div class = "sign-up">
        <iframe src='https://muse-eeg-app.firebaseapp.com/'></iframe>
    </div>
</template>
<script>

export default {
    name: 'monitor-brain',
    data() {
        return {}
    },
    methods: {
        
    }
}
</script>

<style scoped>
    .sign-up {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        justify-content: center;
        align-items: center;
        background-color: #dbe0f5;
    }
    input {
        margin: 10px 0;
        width: 20%;
        padding: 15px;
    }
    .radio-stack {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        justify-content: center;
        align-items: flex-end;
        width: 70%;
        font-size: 2rem;
    }
    .e-form-label {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 0.5rem;
    }
    #return-bttn {
        position: absolute;
        top: 1rem;
        left: 1rem;
        display: block;
        height: auto;
        width: auto;
        font-size: 1.2rem;
        text-decoration: none;
        color: black;
    }
    .complete {
        width: 80%;
        display: flex;
        justify-content: center;
        text-align: center;
    }
    .complete-cont {
        display:flex;
        justify-content: center;
        align-items: center;
    }
    @import "../assets/css/elios_entry.css";
</style>