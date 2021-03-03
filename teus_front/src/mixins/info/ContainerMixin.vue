<script>
export default {
    name: "ContainerMixin",
    containersSearch: [],
    data () {
        return {
            containers: [],
            container: {
                id: null,
                name: null,
                image: null
            },
            image: null,
            filter: null,
        }
    },
    methods: {
        getContainers() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/info/get-containers-list/', {
                                params: this.containersSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.containers = response.data.results
                                
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
        getContainer(id) {
            const self = this;
            return new Promise((resolve, reject) => {
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/info/get-container/' + id + '/', {
                                params: this.containersSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response.data);
                                self.container = response.data;
                                self.image = response.data.image;
                                self.container.image = null;
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
        deleteContainer(id) {
            if (this.deleteRequest('/api/info/delete-container/' , id))
                this.containers = this.containers.filter(element => element.id !== id);
        },
        saveContainer(obj, id = null) {
            const self = this;
            if (typeof(obj.image) == 'string')
                delete obj.image;

            if (obj.image === [])
                obj.image = null;
            
            let formData = new FormData();
            Object.keys(obj).map(function(key) {
                if (obj[key])
                    formData.append(key, obj[key]);
            });

            if (id){
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .put(
                                process.env.VUE_APP_HOST + '/api/info/update-container/' + id + '/',
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
                                self.getContainer(id)
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
                                process.env.VUE_APP_HOST + '/api/info/create-container/',
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
