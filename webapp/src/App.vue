<template>
  <div class="mdl-layout mdl-js-layout">
    <div class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
        <div class="mdl-tabs__tab-bar">
            <router-link class="mdl-tabs__tab mdl-navigation__link" :to="{ name: 'about'}">Accueil</router-link>
        </div>    
    </div>
    <main class="mdl-layout__content">
      <div class="page-content">
  				<router-view name="panel"></router-view>
      </div>
    </main>
    
     <footer class="mdl-mini-footer education-footer">
       <div class="mdl-mini-footer__right-section">
          <div class="mdl-layout__header-row education-logo-row">
              <span class="mdl-layout__title">
                  <div class="education-logo"></div>
                  <span class="mdl-layout__title">edubenin.bj</span>
              </span>      
          </div>
       </div>
    </footer>
    
  </div>
</template>


<script>
require('material-design-lite')

export default {
  name: 'app',
	methods: {
      hideMenu: function () {
        document.getElementsByClassName('mdl-layout__drawer')[0].classList.remove('is-visible')
        document.getElementsByClassName('mdl-layout__obfuscator')[0].classList.remove('is-visible')
      }
    }
}
</script>
<style>
.mdl-mini-footer{
  background: white;
  border: 1px;
}

@import url('https://fonts.googleapis.com/icon?family=Material+Icons');
@import url('https://code.getmdl.io/1.2.1/material.blue-red.min.css');
</style>