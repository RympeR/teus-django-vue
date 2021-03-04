import axios from 'axios'

const state = () => ({
    list: [],
    item: {},
    image: null,
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
            axios.get(process.env.VUE_APP_HOST + '/api/info/get-containers-list/', {
                    // params: this.linesSearch,
                    // headers: {
                    //     Authoriz ation: token
                    // }
                })
                .then(response => {
                    let list = response.data.results;
                    commit('setList', list);
                    console.log(list)
                    resolve(list);
                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },

    getItem({commit}, id) {
        return new Promise((resolve, reject) => {
            axios.get(`${process.env.VUE_APP_HOST}/api/info/get-container/${id}/`, {
                    // params: this.linesSearch,
                    // headers: {
                    //     Authorization: token
                    // }
                })
                .then(response => {
                    console.log(response.data)
                    commit('setItem', response.data);
                    resolve(response.data)
                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    deleteItem({state}, id) {
        let confirmDelete = confirm('Удаление типа контейнера приводит к удалению всех заявок и запросов где он использовался.');
        if (confirmDelete) {
            return new Promise((resolve, reject) => {
                axios.delete(`${process.env.VUE_APP_HOST}/api/info/delete-container/${id}/`)
                    .then(response => {
                        state.list = state.list.filter(element => element.id !== id);
                        resolve(response.data);
                    })
                    .catch(response => {
                        console.log(response.error);
                        reject(response.error);
                    })
            })
        }
    },
    
    saveItem({state}, obj) {
        // console.log(state)
        // console.log(obj.id)
        // if (typeof(obj.image) == 'string')
        //     delete obj.image;

        // if (obj.image === [])
        //     obj.image = null;
            
        let formData = new FormData();
        
        Object.keys(obj).map(function (key) {
            if (obj[key])
                formData.append(key, obj[key]);
        });

        // console.log(obj)
        if (obj.id) {
            return new Promise((resolve, reject) => {
                axios.put(`${process.env.VUE_APP_HOST}/api/info/update-container/${obj.id}/`,
                        formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },

                        }
                    )
                    .then(function (response) {
                        console.log(state)
                        state.item = {};
                        state.image = null;
                        console.log(response.data)
                        resolve(response.data);
                    })
                    .catch(function (response) {
                        console.log(response.error);
                        reject(response.error);
                    })
            })
        } else {
            return new Promise((resolve, reject) => {
                axios.post(`${process.env.VUE_APP_HOST}/api/info/create-container/`,
                        formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data',
                            },
                        }
                    )
                    .then(function (response) {
                        state.item = {};
                        state.image = null;
                        resolve(response.data)
                        this.goBack()
                    })
                    .catch(function (response) {
                        reject(response.error);
                    })
            })
        }
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