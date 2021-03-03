import axios from 'axios'

const state = () => ({
    list: [],
    item: {},
    iamge:null
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
    getList({
        commit
    }) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + '/api/info/get-lines-list/', {
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

    getItem({
        commit
    }, id) {
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
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    deleteItem({
        commit
    }, id) {
        function deleteRequest(address, id) {
            let confirmDelete = confirm('Удалить?');
            if (confirmDelete) {
                return new Promise((resolve, reject) => {
                    axios
                        .delete(process.env.VUE_APP_HOST + address + id + '/', {
                            headers: {},
                        })
                        .then(function (response) {
                            resolve(response.data)
                            return true
                        })
                        .catch(function (response) {
                            reject(response.error);
                        })
                })
            } else
                return false
        }
        console.log(commit)
        console.log(this)
        deleteRequest('/api/info/delete-line/', id)
            // state.list = state.list.filter(element => element.id !== id);
    },
    
    saveItem({commit}, obj) {
        console.log(commit)
        console.log(obj.id)
        let formData = new FormData();
        Object.keys(obj).map(function (key) {
            if (obj[key])
                formData.append(key, obj[key]);
        });

        console.log(obj)
        if (obj.id) {
            return new Promise((resolve, reject) => {
                  
                axios
                    .put(
                        process.env.VUE_APP_HOST + '/api/info/update-line/' + obj.id + '/',
                        formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },

                        }
                    )
                    .then(function (response) {
                        this.templateShowSuccess(response);
                        this.getItem(obj.id)
                    })
                    .catch(function (response) {
                        console.log(response);
                        reject(response);
                    })
            })
        } else {
            return new Promise((resolve, reject) => {
                axios.post(
                        process.env.VUE_APP_HOST + '/api/info/create-line/',
                        formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data',
                            },

                        }
                    )
                    .then(function (response) {
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