// axios
import axios from 'axios'

const apiUrl = process.env.VUE_APP_API_ENDPOINT

export default axios.create({
  baseURL: apiUrl
})
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'
