<template>
  <div class="mdl-layout mdl-js-layout">
    <header class="mdl-layout__header">
      <div class="mdl-layout__header-row">
        <span class="mdl-layout-title">Education Benin</span>
      </div>
    </header>
    <div class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
      <div class="mdl-tabs__tab-bar">
        <router-link class="mdl-tabs__tab mdl-navigation__link" :to="{ name: 'university'}">Universites</router-link>
        <router-link class="mdl-tabs__tab mdl-navigation__link" :to="{ name: 'faculty'}">UFR Public</router-link>
        <router-link class="mdl-tabs__tab mdl-navigation__link" :to="{ name: 'formation'}">Formation</router-link>
      </div>
    </div>
    <main class="mdl-layout__content">
      <div class="page-content">
        <div v-if="state.universities">
  				<router-view name="panel"></router-view>
  		</div>
      </div>
    </main>
  </div>
</template>


<script>
import store from '@/components/Store'
require('material-design-lite')

export default {
  name: 'app',
	data(){
		return {state: store.state}
	},
	methods: {
      hideMenu: function () {
        document.getElementsByClassName('mdl-layout__drawer')[0].classList.remove('is-visible')
        document.getElementsByClassName('mdl-layout__obfuscator')[0].classList.remove('is-visible')
      }
    }
}
</script>
<style>
@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
@import url('https://code.getmdl.io/1.2.1/material.blue-red.min.css');
</style>