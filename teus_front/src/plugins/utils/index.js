import { freeSet } from '@coreui/icons'
import router from '@/router'
const UtilsPlugin = {}

UtilsPlugin.install = function(Vue) {
        console.log('Installing');
        Vue.freeSet = function () {
            return freeSet
        }
        Vue.transformDate = function (date) {
            console.log(date)
            console.log(Vue.$moment(String(date)).tz("UTC").format('YYYY-MM-DDTH:mm'))
            console.log('--------------------')
            return Vue.$moment(String(date)).tz("UTC").format('YYYY-MM-DDTH:mm')
        }
        Vue.templateShowSuccess = function (text = "Сохранено") {
            let alertSuccess = document.createElement('div');
            alertSuccess.classList = 'alert alert-success alert-custom';
            alertSuccess.innerText = text;
            document.querySelector('.app').append(alertSuccess);
            setTimeout(function () {
                document.querySelector('.alert-custom').remove();
            }, 5000);
        }
        Vue.collectError = function (response) {
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
        }
        Vue.templateShowError = function (response) {
            alert(Vue.collectError(response));
        }
        Vue.deleteRequest = function (address, id) {
            const self = Vue;
            let confirmDelete = confirm('Удалить?');
            if (confirmDelete) {
                Vue.$store.dispatch('token')
                    .then((token) => {
                        Vue.$axios
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
            } else
                return false
        }
        Vue.templateShowDeleted = function (response) {
            console.log(response);
            // alert(text);
            let alertSuccess = document.createElement('div');
            alertSuccess.classList = 'alert alert-info alert-custom';
            alertSuccess.innerText = "Удалено";
            document.querySelector('.app').append(alertSuccess);
            setTimeout(function () {
                document.querySelector('.alert-custom').remove();
            }, 5000);
        }
        Vue.goBack = function () {
            router.go(-1)
        }
        Vue.toSelectArray = function (data, text) {
            let response = [];
            response.push({ value: null, text: text });
            for (let [key, value] of Object.entries(data)) {
                response.push({ value: key, text: value });
            }
            return response
        }
        Vue.getCurrentTimestamp = function () {
            return new Date().getTime();
        }
        Vue.removeFromArray = function (arr) {
            let what, a = arguments, L = a.length, ax;
            while (L > 1 && arr.length) {
                what = a[--L];
                while ((ax = arr.indexOf(what)) !== -1) {
                    arr.splice(ax, 1);
                }
            }
            return arr;
        }

        Vue.recalculatePercent = function (total, current) {
            return ((current * 100) / total);
        }
    }

export default UtilsPlugin