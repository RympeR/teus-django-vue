<script>
export default {
    name: "LineMixin",
    linesSearch: [],
    data () {
        return {
            lines: [],
            line: {
                id: null,
                name: null,
            },
            filter: null,
        }
    },
    methods: {
        getLines() {
            return new Promise((resolve, reject) => {
                const self = this;
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/info/get-lines-list/', {
                                params: this.linesSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.lines = response.data.results
                                
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
        getLine(id) {
            const self = this;
            return new Promise((resolve, reject) => {
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .get(process.env.VUE_APP_HOST + '/api/info/get-line/' + id + '/', {
                                params: this.linesSearch,
                                headers: {
                                    Authorization: token
                                }
                            })
                            .then(function (response) {
                                console.log(response);
                                self.line = response.data;
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
        deleteLine(id) {
            if (this.deleteRequest('/api/info/delete-line/' , id))
                this.lines = this.lines.filter(element => element.id !== id);
        },
        saveLine(obj, id = null) {
            const self = this;

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
                                process.env.VUE_APP_HOST + '/api/info/update-line/' + id + '/',
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
                                self.getLine(id)
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
                                process.env.VUE_APP_HOST + '/api/info/create-line/',
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
