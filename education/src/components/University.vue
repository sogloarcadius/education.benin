<template>
  <div>
    <div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--3-col">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                <label class="mdl-selectfield__label" for="type">Type</label>
                <select v-model="type_selected" class="mdl-selectfield__select" id="type" name="type">
                  <option v-on:click="Filter()"></option>
                  <option v-on:click="Filter()" value='PUBLIC'>PUBLIC</option>
                  <option v-on:click="Filter()" value='PRIVATE'>PRIVEE</option>
                </select>
                &nbsp;
                <label class="mdl-selectfield__label" for="city">Ville</label>
                <select v-model="city_selected" class="mdl-selectfield__select" id="city" name="city">
                  <option v-on:click="Filter()"></option>
                  <option v-for='city in ListOfCities()' :key=city v-on:click="Filter()">{{city}}</option>
                </select>
              </div>
          </span>
     </div>
      <div class="mdl-grid">
          <div v-for="university in universities" :key="university.id" class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone university-card mdl-card mdl-shadow--2dp" @click="displayUniversityDetail(university)">
              <div class="mdl-card__title mdl-card--expand">
                  <h2 class="mdl-card__title-text">{{university.id}}</h2>
              </div>
              <div class="mdl-card__supporting-text">
                  <strong>Nom : </strong> {{university.name}} <br/>
                  <strong>Email : </strong> {{university.email}} <br/>
                  <strong>Tél : </strong> {{university.phone}}<br/>
                  <strong>Address: </strong> {{university.address}}<br/>
                  <strong>Internet: </strong> {{university.url}}
              </div>
              <div class="mdl-card__actions mdl-card--border">
                <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                  Voir
                </a>
              </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>

import store from '@/components/Store'

export default {
  components: {},
  data(){
		return {
      universities: store.state.universities,
      city_selected: '',
      type_selected: ''
    }
  },
  methods: {
    displayUniversityDetail (university) {
      this.$router.push({ name: 'university_detail', params: { university_id: university.id } })
    },

    Filter(){
      var self = this;
      var response = [];
      if (this.city_selected == '' && this.type_selected == ''){
          this.universities = store.state.universities;
      } 
      else if (this.city_selected == '' && this.type_selected != ''){
          response = _.filter(store.state.universities, function(university) {
          if (university.type.toUpperCase() == self.type_selected ){
              return university;
          }
        });
        this.universities = response;
      }
      else if( self.type_selected == '' && self.city_selected != '' ){
          response = _.filter(store.state.universities, function(university) {
          if (_.includes(_.mapValues(university.locations, _.method('toUpperCase')), self.city_selected)){
              return university;
          }
        });
        this.universities = response;
      } 
      else {
          response = _.filter(store.state.universities, function(university) {
          if (_.includes(_.mapValues(university.locations, _.method('toUpperCase')), self.city_selected) && university.type.toUpperCase() == self.type_selected ){
                return university;
          }
          });
          this.universities = response;
      }
    },

    ListOfCities() {
        var response = [];
        _.forEach(store.state.universities, (function(university) {
          response.push(university.locations);
        }));

        response =_.flatten(response);
        response = _.map(response, _.method('toUpperCase'));
        response = _.uniq(response).sort();
        response = _.compact(response);
        return response;
    }

  },
}
</script>

<style scoped>

.university-card.mdl-card {
  width: 320px;
  height: 320px;
  margin: 12px;
}
.university-card > .mdl-card__title {
  color: #fff;
  background:
    url('../assets/img/school.svg') bottom right 15% no-repeat #46B6AC;
}

.filter-wrapper {
  margin: 12px;
}

</style>



