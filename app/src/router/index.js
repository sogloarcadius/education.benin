import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import About from '@/components/About'
import Colleges from '@/components/Colleges'
import DetailView from '@/components/DetailView'

export default new VueRouter({
  routes: [
		{
			path: '/about',
			name: 'about',
			components: { panel: About }
		}, 
		{
			path: '/colleges',
			name: 'colleges',
			components: { panel: Colleges }
		},
		{
			path: '/detail/:id',
			name: 'detail',
			components: { panel: DetailView }
		}
  ]
})