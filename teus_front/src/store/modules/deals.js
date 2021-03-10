// import axios from '@/plugins/axios'
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
    },

}

const actions = {
    getList({ commit }) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + '/api/containers/get-deal-list', {
                // params: this.linesSearch,
                // headers: {
                //     Authoriz ation: token
                // }
            })
                .then(response => {
                    let list = response.data.results;
                    console.log(list)

                    list.forEach((el) => {
                        el.amount = {
                            amount: el.amount,
                        };
                        el.first_user_phone = {
                            id: el.first_user.id,
                            phone: el.first_user.phone
                        };
                        el.first_user_name = {
                            id: el.first_user.id,
                            name: el.first_user.name
                        };
                        el.sec_user_phone = {
                            id: el.sec_user.id,
                            phone: el.sec_user.phone
                        };
                        el.sec_user_name = {
                            id: el.sec_user.id,
                            name: el.sec_user.name
                        };


                    });
                    commit('setList', list);

                    resolve(list);

                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    getItem({ commit }, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/containers/get-deal/${id}/`, {
                // params: this.linesSearch,
                headers: {
                    Authorization: "tset",
                },
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
    deleteItem({ state }, id) {
        let confirmDelete = confirm('Вы действительно хотите удалить этот запрос?');
        if (confirmDelete) {
            return new Promise((resolve, reject) => {
                axios.delete(`${process.env.VUE_APP_HOST}/api/containers/delete-deal/${id}/`)
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
    getFilteredItems({ commit, state }, obj) {
        console.log(obj)
        console.log(state)
        var str = `${process.env.VUE_APP_HOST}/api/containers/get-deal-list?`;
        for (var key in obj) {
            if (str != `${process.env.VUE_APP_HOST}/api/containers/get-deal-list?`) {
                str += "&";
            }
            str += key + "=" + encodeURIComponent(obj[key]);
        }
        console.log(str)
        return new Promise((resolve, reject) => {
            axios
                .get(str)
                .then(response => {
                    let list = response.data.results;

                    console.log(list)

                    list.forEach((el) => {
                        el.amount = {
                            amount: el.amount,
                        };
                        el.first_user_phone = {
                            id: el.first_user.id,
                            phone: el.first_user.phone
                        };
                        el.first_user_name = {
                            id: el.first_user.id,
                            name: el.first_user.name
                        };
                        el.sec_user_phone = {
                            id: el.sec_user.id,
                            phone: el.sec_user.phone
                        };
                        el.sec_user_name = {
                            id: el.sec_user.id,
                            name: el.sec_user.name
                        };


                    });

                    commit('setList', list);
                    resolve(list);
                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    saveItem({ state }, obj) {
        console.log(state)
        console.log(obj.id)
        obj.user_request = obj.first_user.id;
        obj.user_proposition = obj.sec_user.id;
        obj.line = obj.line.id;
        obj.container = obj.container.id;
        obj.city = obj.city.id;
        obj.handshake_time = obj.handshake;
        console.log(obj)
        let formData = new FormData();

        Object.keys(obj).map(function (key) {
            if (obj[key])
                formData.append(key, obj[key]);
        });

        if (obj.id) {
            return new Promise((resolve, reject) => {
                axios
                    .put(process.env.VUE_APP_HOST + '/api/containers/update-deal/' + obj.id + '/', formData, {
                        headers: {
                            Authorization: "tset",
                            'Content-Type': 'multipart/form-data'
                        },
                    }
                    )
                    .then(response => {
                        console.log(this)
                        state.item = {};
                        resolve(response.data);
                    })
                    .catch(response => {
                        console.log(response.error);
                        reject(response.error);
                    })
            })
        } else {
            return new Promise((resolve, reject) => {
                axios.post(process.env.VUE_APP_HOST + '/api/info/create-deal/', formData, {
                    headers: {
                        Authorization: "tset",
                        'Content-Type': 'multipart/form-data',
                    },
                })
                    .then(response => {
                        state.item = {};
                        resolve(response.data)
                        // console.log(response.data)
                    })
                    .catch(response => {
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