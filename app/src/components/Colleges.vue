<template>
  <div>
    <div>
    <br/>
     <div class="search-wrapper">
          <span>
             <div class="public-private mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
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
          <div v-for="college in colleges" :key="college.id" class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone college-card mdl-card mdl-shadow--2dp" @click="displayDetails(college.id)">
              <div class="mdl-card__title mdl-card--expand">
                  <h2 class="mdl-card__title-text">{{college.id}}</h2>
              </div>
              <div class="mdl-card__supporting-text">
                  <strong>Name : </strong> {{college.name}} <br/>
                  <strong>Licence : </strong> {{college.type}} <br/>
                  <strong>Phone : </strong> {{college.phone}}<br/>
                  <strong>Address: </strong> {{college.address}}<br/>
                  <strong>Website: </strong> {{college.url}}
              </div>
              <div class="mdl-card__actions mdl-card--border">
                <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                  View
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
      colleges: store.state.colleges.colleges
    }
  },
  methods: {
    displayDetails (id) {
      this.$router.push({ name: 'detail', params: { id: id } })
    },

    FilterByType(mytype) {
      var response = [];

      if (mytype == "all") {
        response = store.state.colleges.colleges; 
      } else {
        response = _.filter(store.state.colleges.colleges, function(college) {
          return college.type == mytype;
        });
      }

      this.colleges = response;
      
    },
    FilterByCity(mycity) {
      var response = [];

      if (mycity == "all"){
        response = store.state.colleges.colleges;
      } else {
        response = _.filter(store.state.colleges.colleges, function(college) {
            if (_.includes(college.locations, mycity)){
                return college;
            }
        });
      }
      
      this.colleges = response;

    },

    ListOfCities() {
        var response = [];
        _.forEach(store.state.colleges.colleges, (function(college) {
          response.push(college.locations);
        }));
        response = _.uniq(_.flatten(response)).sort()
        return response;
    }

  },
}
</script>

<style scoped>

.college-card.mdl-card {
  width: 320px;
  height: 320px;
  margin: 12px;
}
.college-card > .mdl-card__title {
  color: #fff;
  background:
    url('../assets/img/school.svg') bottom right 15% no-repeat #46B6AC;
}

.search-wrapper > .public-private {
  padding: 20px;
}
</style>



