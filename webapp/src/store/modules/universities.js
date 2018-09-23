import { UniversityApi } from '@/common/api'


// initial state
export const state = {
    all: [],
    loading: true
}

// getters
export const getters = {
}

// actions
export const actions = {
    getAllUniversities (context) {
        return UniversityApi.get()
        .then(function (response){
            context.commit('setUniversities', response.data)
         })
    }
}

// mutations
export const mutations = {
    setUniversities (state, universities) {
      state.all = universities;
      state.loading = false;
  }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}