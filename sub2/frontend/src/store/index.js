import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userimg: "",
    name: "",
    email: "",
  },
  mutations: {
    login(state, payload) {
      state.email = payload.email;
      if (payload.name) state.name = payload.name;
      if (payload.userimg) state.userimg = payload.userimg;
    },
    logout(state) {
      state.email = "";
      state.name = "";
      state.userimg = "";
    },
  },
});
