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
    getList({
        commit
    }) {
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

    getItem({
        commit
    }, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/info/get-container/${id}/`, {
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
        deleteRequest('/api/info/delete-container/', id)
            // state.list = state.list.filter(element => element.id !== id);
    },
    
    saveItem({commit}, obj) {
        console.log(commit)
        console.log(obj.id)
        if (typeof(obj.image) == 'string')
            delete obj.image;

        if (obj.image === [])
            obj.image = null;
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
                        process.env.VUE_APP_HOST + '/api/info/update-container/' + obj.id + '/',
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
                        process.env.VUE_APP_HOST + '/api/info/create-container/',
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