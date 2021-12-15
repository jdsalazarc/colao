<template>
  <div>
    <HelloWorld/>
    <div class="row my-3">
      <div class="col-md-3">
        <img
          class="d-block"
          style="margin-top: 80px"
          src="@/assets/img/woman.png"
          alt=""
        />
      </div>
      <div class="col-md-6">
        <form class="comenzar-form" @submit.prevent>
          <h5>Pon tu nombre para iniciar el juego</h5>
          <input
            class="form-control text-center w-full py-2 my-4"
            v-model="nombre"
            type="text"
          />
          <button
            @click="comenzarJuego"
            class="btn comenzar w-full py-2 text-white"
          >
            Comenzar
          </button>
        </form>
      </div>
      <div class="col-md-3">
        <img class="d-block" src="@/assets/img/man.png" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios"

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
  data() {
    return {
      nombre: "",
    };
  },
  methods: {
   async comenzarJuego() {
      try {
          const respuesta = await axios.post("http://127.0.0.1:8000/api/usuarios", this.nombre)
      console.log(respuesta)
      } catch (error) {
          console.log(error)
      }
    },
  },
};
</script>

<style>
h5 {
  font-weight: 600;
}
.comenzar {
  border-radius: 13px;
  background-color: #18a795;
  font-weight: 600;
  width: 400px;
}

.comenzar-form {
  margin: auto;
  width: 400px;
}

.form-control {
  color: #636363 !important;
}

.comenzar-form input {
  border: 3px solid #ff5656;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 13px;
  font-weight: 600;
}
</style>
