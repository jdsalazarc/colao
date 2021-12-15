<template>
  <div>
    <HelloWorld />
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
        <div class="card-home py-5 px-4">
          <h4 class="py-3">Reglas del juego</h4>
          <ul class="card-home-list text-left">
            <li>
              Se tiene que guardar el nombre del usuario al inicio de la partida
              para llevar registro de sus resultados.
            </li>
            <li>
              Se tiene que seleccionar 1 objeto que no esté relacionado con los
              demás en un grupo de 4
            </li>
            <li>
              El tiempo para terminar un nivel es de 30 segundos, pero a partir
              del nivel 10 disminuye un segundo hasta llegar al 20.
            </li>
          </ul>
        </div>
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

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
};
</script>

<style>
h4 {
  font-weight: 900 !important;
}

.card-home {
  border: 3px solid #ff5656;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 20px;
}

.card-home-list li {
  text-align: left;
}
</style>
