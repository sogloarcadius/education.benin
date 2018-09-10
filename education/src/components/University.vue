<template>
  <div>
    <div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--3-col">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                <label class="mdl-selectfield__label" for="type">Type</label>
                <select class="mdl-selectfield__select" id="type" name="type">
                  <option v-on:click="FilterByType('all')" value="all">all</option>
                  <option v-on:click="FilterByType('public')" value="option1">public</option>
                  <option v-on:click="FilterByType('private')" value="option2">private</option>
                </select>
                &nbsp;
                <label class="mdl-selectfield__label" for="city">Ville</label>
                <select class="mdl-selectfield__select" id="city" name="city">
                  <option :key="all" value="all" v-on:click="FilterByCity('all')">all</option>
                  <option v-for='city in ListOfCities()' :key=city value=city v-on:click="FilterByCity(city)">{{city}}</option>
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
                  <strong>Name : </strong> {{university.name}} <br/>
                  <strong>Licence : </strong> {{university.type}} <br/>
                  <strong>Phone : </strong> {{university.phone}}<br/>
                  <strong>Address: </strong> {{university.address}}<br/>
                  <strong>Website: </strong> {{university.url}}
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
      universities: store.state.universities
    }
  },
  methods: {
    displayUniversityDetail (university) {
      this.$router.push({ name: 'university_detail', params: { university: university } })
    },

    FilterByType(mytype) {
      var response = [];

      if (mytype == "all") {
        response = store.state.universities; 
      } else {
        response = _.filter(store.state.universities, function(university) {
          return university.type == mytype;
        });
      }

      this.universities = response;
      
    },
    FilterByCity(mycity) {
      var response = [];

      if (mycity == "all"){
        response = store.state.universities;
      } else {
        response = _.filter(store.state.universities, function(university) {
            if (_.includes(university.locations, mycity)){
                return university;
            }
        });
      }
      
      this.universities = response;

    },

    ListOfCities() {
        var response = [];
        _.forEach(store.state.universities, (function(university) {
          response.push(university.locations);
        }));
        response = _.uniq(_.flatten(response)).sort()
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



