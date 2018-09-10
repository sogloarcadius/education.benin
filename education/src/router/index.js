import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import About from '@/components/About'
import University from '@/components/University'
import UniversityDetail from '@/components/UniversityDetail'

export default new VueRouter({
  routes: [
		{
			path: '/',
			redirect: '/about',
		},
		{
			path: '/about',
			name: 'about',
			components: { panel: About }
		}, 
		{
			path: '/university',
			name: 'university',
			components: { panel: University },
		},
		{
			path: '/detail/:university',
			name: 'university_detail',
			components: { panel: UniversityDetail }
		}
		
  ]
})