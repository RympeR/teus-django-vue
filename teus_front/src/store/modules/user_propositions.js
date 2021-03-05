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

                    console.log(list)
                    
                    list.forEach((el) => {
                        el.amount = {
                            amount: el.amount,
                        };
                        el.user = {
                            name: el.user.name,
                            phone: el.user.name + ' ' + el.user.phone
                        }
                        el.date = {
                            date: el.date,
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
    getItem({commit}, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/containers/get-proposition/${id}/`, {
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
    getFilteredItems({commit, state}, obj){
        console.log(obj)
        console.log(state)
        var str = `${process.env.VUE_APP_HOST}/api/containers/get-proposition-list?`;
        for (var key in obj) {
            if (str != `${process.env.VUE_APP_HOST}/api/containers/get-proposition-list?`) {
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
                
                console.log(list)
                
                list.forEach((el) => {
                    el.user = {
                        name: el.user.name,
                        phone: el.user.name + ' ' + el.user.phone
                    }
                    el.amount = {
                        amount: el.amount,
                    };
                    el.date = {
                        date: el.date,
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
    saveItem({state}, obj) {
        console.log(state)
        console.log(obj.id)
        obj.user = obj.user.id;
        obj.line = obj.line.id;
        obj.container = obj.container.id;
        obj.city = obj.city.id;
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