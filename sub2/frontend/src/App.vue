<template>
  <div id="app">
    <Header />
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  components: {
    Header,
  },
  created() {
    $.initialize();
    if (this.$cookie.get("email") && !this.$store.state.email) {
      this.getLogin();
    }
  },
  mounted() {
    $.initialize();
    if (this.$cookie.get("email") && !this.$store.state.email) {
      this.getLogin();
    }
  },
  updated() {
    $.initialize();
    if (this.$cookie.get("email") && !this.$store.state.email) {
      this.getLogin();
    }
  },
  methods: {
    getLogin() {
      this.$store.commit("login", {
        email: this.$cookie.get("email"),
        name: this.$cookie.get("name"),
        userimg: this.$cookie.get("userimg"),
      });
    },
  },
};
</script>
