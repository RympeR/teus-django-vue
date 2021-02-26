<script>
export default {
    name: "CityMixin",
    citiesSearch: [],
    data () {
        return {
            cities: [],
            city: {
                id: null,
                name: null,
            },
            filter: null,
        }
    },
    methods: {
        getCities() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/info/get-cities-list/', {
                                params: this.citiesSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.cities = response.data.results
                                
                                resolve(response)
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                                reject(response)
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            })
        },
        getCity(id) {
            const self = this;
            return new Promise((resolve, reject) => {
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/info/get-city/' + id + '/', {
                                params: this.citiesSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.city = response.data;
                                resolve(response)
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                                reject(response)
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            })
        },
        deleteCity(id) {
            if (this.deleteRequest('/api/info/delete-city/' , id))
                this.cities = this.cities.filter(element => element.id !== id);
        },
        saveCity(obj, id = null) {
            const self = this;

            let formData = new FormData();

            Object.keys(obj).map(function(key) {
                if (obj[key])
                    formData.append(key, obj[key]);
            });
            console.log(formData)
            if (id){
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .put(
                                process.env.VUE_APP_HOST + '/api/info/update-city/' + id + '/',
                                formData,
                                {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                        Authorization: token
                                    },
        
                                }
                            )
                            .then(function (response) {
                                self.templateShowSuccess(response);
                                self.getCity(id)
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            }else{
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .post(
                                process.env.VUE_APP_HOST + '/api/info/create-city/',
                                formData,
                                {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                        Authorization: token
                                    },
        
                                }
                            )
                            .then(function (response) {
                                console.log(response);
                                self.goBack()
                            })
                            .catch(function (response) {
                                console.log(response);
                                self.templateShowError(response);
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
            }
        },
    }
}
</script>

<style scoped>

</style>
