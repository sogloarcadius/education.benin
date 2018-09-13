<template>
  <div>
    <div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--5-col">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                
                <label class="mdl-selectfield__label" for="fields">Domaine</label>
                <select v-model="field_selected" class="mdl-selectfield__select" id="field" name="field">
                  <option v-on:click="Filter()"></option>
                  <option v-for='field in ListOfFields()' :key=field v-on:click="Filter()">{{field}}</option>
                </select>
                &nbsp;

                <label class="mdl-selectfield__label" for="university">Université</label>
                <select v-model="university_selected" class="mdl-selectfield__select" id="university" name="university">
                  <option v-on:click="Filter()"></option>
                  <option v-for='university in ListOfUniversities()' :key=university v-on:click="Filter()">{{university}}</option>
                </select>
                &nbsp;

                <span v-if="ListOfFaculties(university_selected).length > 0">
                    <label class="mdl-selectfield__label" for="faculty">Faculté</label>
                    <select v-model="faculty_selected" class="mdl-selectfield__select" id="faculty" name="faculty">
                    <option v-on:click="Filter()"></option>
                    <option v-for='faculty in ListOfFaculties(university_selected)' v-on:click="Filter()">{{faculty}}</option>
                    </select>
                </span>
              </div>
          </span>
     </div>
    </div>
    <div class="mdl-grid">
        <div v-for="course in courses" class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone university-card mdl-card mdl-shadow--2dp">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">{{course.name}}</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Description : </strong> {{course.description}} <br/>
                <strong>Prérequis : </strong> {{course.prerequesite}} <br/>
                <strong>Année d'étude : </strong> {{course.yearofstudy}}<br/>
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
        courses: store.state.courses,
        faculties: store.state.faculties,
        universities: store.state.universities,
        university_selected: '',
        faculty_selected: ''
    }
  },
  methods: {
    ListOfFaculties(university_id) {
            var response = [];
            var faculties = [];
            _.forEach(store.state.faculties, (function(university) {
                    if (university.id.toUpperCase() == university_id) {
                        faculties.push(university.faculties);
                    }
                }));
            faculties = _.uniq(_.flatten(faculties)).sort();
            _.forEach(faculties, (function(faculty){
                response.push(faculty.id);
            }));

            response = _.map(response, _.method('toUpperCase'));
            response = _.compact(response);

            return response;
    },

    ListOfUniversities() {
        var response = [];
        _.forEach(store.state.universities, (function(university) {
            response.push(university.id);
        }));
        response = _.map(response, _.method('toUpperCase'));
        response = _.compact(response);
        
        return response;
    },

    ListOfFields(){
        var response = [];
        _.forEach(store.state.courses, (function(course){
            response.push(course.fields);
        }))

        response = _.flatten(response);
        response = _.map(response, _.method('toUpperCase'));
        response = _.uniq(response);
        response = _.compact(response);

        return response;
    },
    Filter(){
    }
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
  color: rgb(12, 11, 11);
  
}

.filter-wrapper {
  margin: 12px;
}
</style>



