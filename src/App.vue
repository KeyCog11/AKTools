<template>
  <v-app>
    <v-app-bar
      app
      color="secondary"
      class="d-flex justify-center"
      dark
    >
      <a class="d-flex align-center justify-center text-center  ">
        <img src="@/assets/img/sargon.png" height="50"/>
        <v-spacer></v-spacer>
        <h1>AKTools</h1>
      </a>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
};
</script>

<style>
  a {
  color:inherit !important;
  text-decoration: none !important;
 }

</style>
