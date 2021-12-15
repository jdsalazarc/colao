<template>
  <div class="container-xxl">
    <div id="nav">
    <router-link class="btn btn-primary" to="/">Reglas</router-link> |
    <router-link class="btn btn-primary" to="/comenzar">Continuar</router-link>
  </div>
  <router-view v-slot="{Component}">
    <transition name="fade" mode="out-in">
      <component :is="Component"></component>
    </transition>
  </router-view>
  </div>
 
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #636363!important;
  overflow: hidden;
  padding-top:50px
  
  
}

*{
 
  font-family: 'Poppins', sans-serif!important;
}

body{
  overflow:hidden;
  background-image: url('assets/img/back.svg');
  background-size:104%;
  background-position:center;
  background-repeat: no-repeat;
  width: 1270px;
  height: 660px;
}



#nav a {
  font-weight: bold;
  
}

.fade-enter-from,
.fade-leave-to{
  opacity:0
}

.fade-enter-active,
.fade-leave-active{
  transition:opacity 0.3s ease-out
}



#nav a.router-link-exact-active {
 
  border: 4px solid #FF6363;
}
</style>
