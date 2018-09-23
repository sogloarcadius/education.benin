import { FacultyApi } from '@/common/api' 


// initial state
export const state = {
    all: [],
    loading: true
}

// getters
export const getters = {}

// actions
export const actions = {
    getAllFaculties (context) {
        return  FacultyApi.get()
        .then(function (response){
            context.commit('setFaculties', response.data)
        })
    }
}

// mutations
export const mutations = {
    setFaculties (state, faculties) {
      state.all = faculties;
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