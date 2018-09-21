import Vue from 'vue'
import Vuex from 'vuex'

import universities from '@/store/modules/universities'
import faculties from '@/store/modules/faculties'
import courses from '@/store/modules/courses'


Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    universities,
    faculties,
    courses
  }
})