<template>
  <div id="app">
    <nav>
      <router-link to="/">Props/Emit</router-link> |
      <router-link to="/global">EventBus(Global)</router-link> |
      <router-link to="/vuex">Vuex</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #2c3e50;
}
nav a.router-link-exact-active {
  color: #42b983;
}
.container {
  display: flex;
  justify-content: center;
  align-content: center;
}
.A {
  flex: 8;
  cursor: pointer;
}
.B {
  flex: 2;
}
.A .box {
  height: 20px;
}
.B .box {
  height: 40px;
  text-align: center;
  margin: 3px;
}
.box {
  border: gray solid 0.5px;
  padding: 3px;
}
</style>
