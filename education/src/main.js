import Vue from 'vue'
import store from '@/components/Store'
import router from '@/router'
import App from '@/App'

store.load()

new Vue({
	el: '#app',
	router,
	data: {
		state: store.state
	},
	render: h => h(App)
})
