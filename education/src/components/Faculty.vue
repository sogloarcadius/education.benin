<template>
  <div>
    <div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--3-col">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                <label class="mdl-selectfield__label" for="type">Université</label>
                <select v-model="university_selected" class="mdl-selectfield__select" id="university" name="university">
                  <option v-on:click="Filter()"></option>
                  <option v-for='university in ListOfUniversities()' :key=university v-on:click="Filter()">{{university}}</option>
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
    </div>
    <div class="mdl-grid">
        <div v-for="faculty in computed_faculties" class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone university-card mdl-card mdl-shadow--2dp">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">{{faculty.id.toUpperCase()}}</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Nom : </strong> {{faculty.id.toUpperCase()}} <br/>
                <strong>Description : </strong> {{faculty.name}} <br/>
                <strong>Ville : </strong> {{faculty.city.toUpperCase()}}<br/>
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
        faculties: store.state.faculties,
        university_selected: '',
        city_selected: '',
        computed_faculties: this.FindFaculties()
    }
  },
  methods: {
    ListOfCities() {
        var response = [];
        _.forEach(store.state.faculties, (function(university) {
            var faculties = university.faculties;
            _.forEach(faculties, (function(faculty){
                response.push(faculty.city);
            }))
        }));

        response =_.flatten(response);
        response = _.map(response, _.method('toUpperCase'));
        response = _.uniq(response).sort();
        response = _.compact(response);
        return response;
    },

    ListOfUniversities() {
        var response = [];
        _.forEach(store.state.faculties, (function(university) {
            response.push(university.id);
        }));
        response = _.map(response, _.method('toUpperCase'));
        return response;
    },

    FindFaculties() {
        var faculties = [];
        _.forEach(store.state.faculties, (function(university) {
              faculties.push(university.faculties);
            }));
        faculties = _.uniq(_.flatten(faculties)).sort();
        faculties = _.compact(faculties);
        return faculties;
    },

    FindFacultiesById(id) {
            var faculties = [];
            _.forEach(store.state.faculties, (function(university) {
                    if (university.id.toUpperCase() == id) {
                        faculties.push(university.faculties);
                    }
                }));
            faculties = _.uniq(_.flatten(faculties)).sort();

            return faculties;
    },

    Filter(){
      var self = this;
      var response = [];
      if (this.city_selected == '' && this.university_selected == ''){
          this.computed_faculties = this.FindFaculties();
      } 
      else if (this.city_selected == '' && this.university_selected != ''){
        this.computed_faculties = this.FindFacultiesById(this.university_selected);
      }
      else if(this.university_selected == '' && this.city_selected != '' ){
          response = _.filter(this.FindFaculties(), function(faculty) {
          if (faculty.city.toUpperCase() == self.city_selected){
              return faculty;
          }
        });
        this.computed_faculties = response;
      } 
      else {
          var response = [];
          var faculties = this.FindFacultiesById(this.university_selected);
          _.forEach(faculties, (function(faculty){
              if (faculty.city.toUpperCase() == self.city_selected){
                response.push(faculty);
              }
          }));         
          this.computed_faculties = response;
      }
    },

  }
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



