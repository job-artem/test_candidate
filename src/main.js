import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
// import axios from 'axios
import axios from './axios.js'
import VueAxios from 'vue-axios'

Vue.prototype.$http = axios
Vue.config.performance = true

Vue.use(Vuetify, VueAxios)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
