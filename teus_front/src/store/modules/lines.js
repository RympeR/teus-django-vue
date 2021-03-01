import axios from 'axios'

const state = () => ({
    list: [],
    item: {},
})

const mutations = {
    setList(state, list) {
        state.list = list;
    },
    setItem(state, item) {
        state.item = item;
    }
}

const actions = {
    getList({commit}) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + '/api/info/get-lines-list/', {
                    // params: this.linesSearch,
                    // headers: {
                    //     Authorization: token
                    // }
                })
                .then(response => {
                    let list = response.data.results;
                    commit('setList', list);
                    resolve(list);
                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    
    getItem({commit}, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/info/get-line/${id}/`, {
                    // params: this.linesSearch,
                    // headers: {
                    //     Authorization: token
                    // }
                })
                .then(response => {
                    commit('setItem', response.data);
                    resolve(response.data)
                })
                .catch(response =>  {
                    reject(response.error);
                })
        })
    },
}

const getters = {

}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}