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
    getList({commit}) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST+'/api/containers/get-proposition-list', {
                    // params: this.linesSearch,
                    // headers: {
                    //     Authoriz ation: token
                    // }
                })
                .then(response => {
                    let list = response.data.results;
                    commit('setList', list);
                    console.log(list)
                   
                        list.forEach((el) => {
                        el.user.filter = el.user.phone;
                        el.city.filter = el.city.name;
                        el.line.filter = el.line.name;
                        el.container.filter = el.container.name;
                        el.amount = {
                            filter: el.amount,
                            amount: el.amount,
                        };
                        el.date = {
                            filter: el.date.start + ':' + el.date.end,
                            date: el.date.start + ':' + el.date.end,
                        };
                        
                    });
                    resolve(list);
                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    getItem({commit}, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/containers/get-proposition/${id}/`, {
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
    deleteItem({state}, id) {
        let confirmDelete = confirm('Вы действительно хотите удалить эту заявку?');
        if (confirmDelete) {
            return new Promise((resolve, reject) => {
                axios.delete(`${process.env.VUE_APP_HOST}/api/containers/delete-proposition/${id}/`)
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
        console.log(state)
        console.log(obj.id)
        
        let formData = new FormData();
        
        Object.keys(obj).map(function (key) {
            if (obj[key])
                formData.append(key, obj[key]);
        });
        
        if (obj.id) {
            return new Promise((resolve, reject) => {
                axios
                    .put(process.env.VUE_APP_HOST + '/api/containers/update-proposition/' + obj.id + '/', formData, {
                            headers: {
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
                axios.post(process.env.VUE_APP_HOST + '/api/info/create-proposition/', formData, {
                        headers: {
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