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
            axios.get(process.env.VUE_APP_HOST + '/api/user/profile/', {
                    // params: this.linesSearch,
                    // headers: {
                    //     Authoriz ation: token
                    // }
                })
                .then(response => {
                    let list = response.data.results;
                    console.log(list)
                    list.forEach((el) => {
                        // el= {
                        //     id : el.id,
                        //     name : el.name + ' ' + el.phone
                        // }
                        console.log(el)
                    });
                    commit('setList', list);
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
            axios.get(process.env.VUE_APP_HOST + `/api/user/profile/${id}/`, {
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
        state
    }, id) {
        let confirmDelete = confirm('Удаление этого пользователя также удалит все его запросы, заявки и чаты. Действительно удалить?');
        if (confirmDelete) {
            return new Promise((resolve, reject) => {
                axios.delete(`${process.env.VUE_APP_HOST}/api/user/delete-profile/${id}/`)
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
    getFilteredItems({commit, state}, obj){
        console.log(obj)
        console.log(state)
        var str = `${process.env.VUE_APP_HOST}/api/user/get-users-list?`;
        for (var key in obj) {
            if (str != `${process.env.VUE_APP_HOST}/api/user/get-users-list?`) {
                str += "&";
            }
            str += key + "=" + encodeURIComponent(obj[key]);
        }
        console.log(str)
        return new Promise((resolve, reject) =>{
            axios
            .get(str)
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
    saveItem({
        commit
    }, obj) {
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
                        process.env.VUE_APP_HOST + '/api/user/update-profile/' + obj.id + '/',
                        formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },

                        }
                    )
                    .then(function (response) {
                        console.log(this)
                        state.item = {};
                        resolve(response.data);
                    })
                    .catch(function (response) {
                        console.log(response);
                        reject(response);
                    })
            })
        } else {
            return new Promise((resolve, reject) => {
                axios.post(
                        process.env.VUE_APP_HOST + '/api/user/create-profile/',
                        formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data',
                            },

                        }
                    )
                    .then(function (response) {
                        state.item = {};
                        resolve(response.data)
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