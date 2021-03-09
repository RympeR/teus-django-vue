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
    getItem({commit}, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/info/get-city/${id}/`, {
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
                    .put(process.env.VUE_APP_HOST + '/api/info/change-password/' + obj.id + '/', formData, {
                            headers: {
                                token: 'tset',
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
                axios.post(process.env.VUE_APP_HOST + '/api/info/create-city/', formData, {
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