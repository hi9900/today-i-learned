import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    result: "",
  },
  getters: {
  },
  mutations: {
    clickOX(state, data) {
      state.result = data
    }
  },
  actions: {
  },
  modules: {
  }
})
