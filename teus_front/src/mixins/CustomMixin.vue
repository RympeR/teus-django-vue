<script>
import {freeSet} from '@coreui/icons'

export default {
    name: 'CustomMixin',
    freeSet,
    data() {
        return {
            static_data: {
                sex: {
                    0: "Ж",
                    1: "М",
                },
                golandTypes: {
                    R: "R",
                    I: "I",
                    A: "A",
                    S: "S",
                    E: "E",
                    C: "C",
                },
                valueTypes: {
                    achievement: "Achievement",
                    independence: "Independence",
                    recognition: "Recognition",
                    relationships: "Relationships",
                    support: "Support",
                    working_conditions: "Working Conditions",
                },
            },
        }
    },
    methods: {
        transformDate(date) {
            console.log(date)
            console.log(this.$moment(String(date)).tz("UTC").format('YYYY-MM-DDTH:mm'))
            console.log('--------------------')
            return this.$moment(String(date)).tz("UTC").format('YYYY-MM-DDTH:mm')
        },
        templateShowSuccess(response, text = "Сохранено") {
            console.log(response);
            // alert(text);
            let alertSuccess = document.createElement('div');
            alertSuccess.classList = 'alert alert-success alert-custom';
            alertSuccess.innerText = text;
            document.querySelector('.app').append(alertSuccess);
            setTimeout(function () {
                document.querySelector('.alert-custom').remove();
            }, 5000);
        },
        collectError(response) {
            console.log(response);
            let text = '';
            try {
                console.log(response.response);
                const status = response.response.status;
                if (status === 400) {
                    for (const [key, value] of Object.entries(response.response.data)) {
                        console.log(key);
                        console.log(value);
                        text += key + ': ' + value + '\n';
                        //text += value + '\n';
                    }
                } else if (status === 403) {
                    text = '403: Вам не разрешено проводить данное действие';
                } else if (status === 404) {
                    text = '404: Адрес не существует';
                } else if (status === 405) {
                    text = '405: Метод не разрешен';
                } else {
                    text = status + ': Неизвестная ошибка';
                }
            } catch (e) {
                text = response.response.status + ': Неизвестная ошибка';
            }
            return text;
        },
        templateShowError(response) {
            alert(this.collectError(response));
        },
        deleteRequest(address, id) {
            const self = this;
            let confirmDelete = confirm('Удалить?');
            if (confirmDelete) {
                this.$store.dispatch('token')
                    .then((token) => {
                        this.$axios
                            .delete(process.env.VUE_APP_HOST + address + id + '/', {
                                headers: {
                                    Authorization: token
                                },
                            })
                            .then(function (response) {
                                self.templateShowDeleted(response);
                            })
                            .catch(function (response) {
                                self.templateShowError(response);
                            })
                    })
                    .catch(response => {
                        console.log(response)
                    })
                return true
            }else
                return false
        },
        templateShowDeleted(response) {
            console.log(response);
            // alert(text);
            let alertSuccess = document.createElement('div');
            alertSuccess.classList = 'alert alert-info alert-custom';
            alertSuccess.innerText = "Удалено";
            document.querySelector('.app').append(alertSuccess);
            setTimeout(function () {
                document.querySelector('.alert-custom').remove();
            }, 5000);
        },
        goBack() {
            this.$router.go(-1)
        },
        toSelectArray(data, text) {
            let response = [];
            response.push({value: null, text: text});
            for (let [key, value] of Object.entries(data)) {
                response.push({value: key, text: value});
            }
            return response
        },
        getCurrentTimestamp() {
            return new Date().getTime();
        },
        removeFromArray(arr) {
            let what, a = arguments, L = a.length, ax;
            while (L > 1 && arr.length) {
                what = a[--L];
                while ((ax = arr.indexOf(what)) !== -1) {
                    arr.splice(ax, 1);
                }
            }
            return arr;
        },
        recalculatePercent(total, current) {
            return ((current * 100) / total);
        },
    },
}
</script>
