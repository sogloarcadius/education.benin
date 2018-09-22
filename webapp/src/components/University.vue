<template>
  <div>
    <div>
    <br/>
    <div class="mdl-layout__title">
        <div class="mdl-layout">
            <div> 
                <strong>UNIVERSITES</strong>
            </div>
        </div>
    </div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--12-col mdl-cell--12-col-tablet mdl-cell--1-col-phone">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                <label class="mdl-selectfield__label" for="type">Statut</label>
                <select v-model="type_selected" class="mdl-selectfield__select" id="type" name="type">
                  <option v-on:click="Filter()"></option>
                  <option v-on:click="Filter()" value='PUBLIC'>PUBLIC</option>
                  <option v-on:click="Filter()" value='PRIVATE'>PRIVEE</option>
                </select>
                <label class="mdl-selectfield__label" for="city">Ville</label>
                <select v-model="city_selected" class="mdl-selectfield__select" id="city" name="city">
                  <option v-on:click="Filter()"></option>
                  <option v-for='city in ListOfCities()' :key=city v-on:click="Filter()">{{city}}</option>
                </select>
              </div>
          </span>
     </div>
      <div class="mdl-grid">
          <div v-for="university in filter_universities" :key="university.name" class="mdl-cell--12-col mdl-cell--12-col-tablet mdl-cell--12-col-phone university-card mdl-card mdl-shadow--2dp" @click="displayUniversityDetail(university.name)">
              <div class="mdl-card__title mdl-card--expand">
                  <h2 class="mdl-card__title-text">{{university.name}}</h2>
              </div>
              <div class="mdl-card__supporting-text">
                  <strong>Nom : </strong> {{university.fullname}} <br/>
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

import { mapState } from 'vuex'


export default {

  computed: mapState({
    universities: state => state.universities.all
  }),

  created () {
    this.$store.dispatch('universities/getAllUniversities')
  },
  
  data(){
		return {
      filter_universities: this.$store.state.universities.all,
      city_selected: '',
      type_selected: ''
    }
  },

  methods: {
    displayUniversityDetail (university_id) {
      this.$router.push({ name: 'university_detail', params: { university_id: university_id } })
    },

    Filter(){
      var self = this;
      var response = [];
      if (this.city_selected == '' && this.type_selected == ''){
          this.filter_universities = this.universities;
      } 
      else if (this.city_selected == '' && this.type_selected != ''){
          response = _.filter(this.universities, function(university) {
          if (university.status.toUpperCase() == self.type_selected ){
              return university;
          }
        });
        this.filter_universities = response;
      }
      else if( self.type_selected == '' && self.city_selected != '' ){
          response = _.filter(this.universities, function(university) {
          if (_.includes(_.mapValues(university.cities, _.method('toUpperCase')), self.city_selected)){
              return university;
          }
        });
        this.filter_universities = response;
      } 
      else {
          response = _.filter(this.universities, function(university) {
          if (_.includes(_.mapValues(university.cities, _.method('toUpperCase')), self.city_selected) && university.status.toUpperCase() == self.type_selected ){
                return university;
          }
          });
          this.filter_universities = response;
      }
    },

    ListOfCities() {
        var response = [];
        _.forEach(this.universities, (function(university) {
          response.push(university.cities);
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



