
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { API_URL } from '@/common/config'
import { cacheAdapterEnhancer, throttleAdapterEnhancer } from 'axios-extensions';

export const BaseApi = {
  init () {
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = API_URL
    Vue.axios.defaults.adapter = throttleAdapterEnhancer(cacheAdapterEnhancer(Vue.axios.defaults.adapter))
  },

  setHeaders () {
    Vue.axios.defaults.headers.common['Cache-Control'] = 'no-cache'
    //Vue.axios.defaults.headers.common['Authorization'] = `Token ${Jwt.getToken()}`
  },

  query (resource, params) {
    return Vue.axios
      .get(resource, params)
      .catch((error) => {
        throw new Error(`[EDUBENIN] BaseApi ${error}`)
      })
  },

  get (resource, slug = '') {
    return Vue.axios
      .get(`${resource}/${slug}`)
      .catch((error) => {
        throw new Error(`[EDUBENIN] BaseApi ${error}`)
      })
  },

  post (resource, params) {
    return Vue.axios.post(`${resource}`, params)
  },

  update (resource, slug, params) {
    return Vue.axios.put(`${resource}/${slug}`, params)
  },

  put (resource, params) {
    return Vue.axios
      .put(`${resource}`, params)
  },

  delete (resource) {
    return Vue.axios
      .delete(resource)
      .catch((error) => {
        throw new Error(`[EDUBENIN] BaseApi ${error}`)
      })
  }
}


export const UniversityApi = {
    get() {
      return BaseApi.get('universities')
    }
}


export const FacultyApi = {
    get() {
      return BaseApi.get('faculties')
    }
}

export const CourseApi = {
    get() {
      return BaseApi.get('courses')
    }
}