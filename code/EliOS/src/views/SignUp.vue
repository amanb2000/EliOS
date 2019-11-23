<template>
    <div class = "sign-up">
        <p>Welcome! Create your new new account:</p>
        <input type="text" placeholder="Email"><br>
        <input type="password" placeholder="Password"><br>
        <button>Sign Up</button>
        <span>Or <router-link to="/login">back to login.</router-link></span>
    </div>
</template>

<script>
export default {
    name: 'signUp',
    data() {
        return {}
    },
    methods: {},
}
</script>

<style scoped>
    .signup {
        margin-top: 40px;
    }
    input {
        margin: 10px 0;
        width: 20%;
        padding: 15px;
    }
    button {
        margin-top: 10px;
        width: 10%;
        cursor: pointer;
    }
    span {
        display: block;
        margin-top: 20px;
        font-size: 11px;
    }
</style>