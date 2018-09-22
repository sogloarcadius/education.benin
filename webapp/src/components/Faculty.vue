<template>
  <div>
    <div>
    <br/>
    <div class="mdl-layout__title">
        <div class="mdl-layout">
            <div> 
                <strong>FACULTES</strong>
            </div>
        </div>
    </div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--12-col mdl-cell--12-col-tablet mdl-cell--1-col-phone">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                <label class="mdl-selectfield__label" for="university">Université</label>
                <select v-model="university_selected" class="mdl-selectfield__select" id="university" name="university">
                  <option v-on:click="Filter()"></option>
                  <option v-for='university in ListOfUniversities()' :key=university v-on:click="Filter()">{{university}}</option>
                </select>
                <label class="mdl-selectfield__label" for="fields">Domaine</label>
                <select v-model="field_selected" class="mdl-selectfield__select" id="field" name="field">
                  <option v-on:click="Filter()"></option>
                  <option v-for='field in ListOfFields()' :key=field v-on:click="Filter()">{{field}}</option>
                </select>
              </div>
          </span>
     </div>
    </div>
    <div class="mdl-grid">
        <div v-for="faculty in computed_faculties" :key=faculty.name class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone university-card mdl-card mdl-shadow--2dp">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">{{faculty.name.toUpperCase()}}</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Nom : </strong> {{faculty.name.toUpperCase()}} <br/>
                <strong>Description : </strong> {{faculty.fullname}} <br/>
                <strong>Université : </strong> {{faculty.university}} <br/>
                <strong>Ville : </strong> {{faculty.city.toUpperCase()}}<br/>
            </div>
        </div>
    </div>
  </div>
</template>

<script>

import { mapState } from 'vuex'


export default {

    created () {
        this.$store.dispatch('faculties/getAllFaculties')
    },

    computed: mapState({
        faculties: state => state.faculties.all
    }),

    data(){
        return {
            university_selected: '',
            field_selected: '',
            computed_faculties: this.$store.state.faculties.all
        }
    },
    methods: {
        ListOfFields(){
            var response = [];
            _.forEach(this.faculties, (function(faculty){
                response.push(faculty.fields);
            }))

            response = _.flatten(response);
            response = _.map(response, _.method('toUpperCase'));
            response = _.uniq(response).sort();
            response = _.compact(response);

            return response;
        },

        ListOfUniversities() {
            var response = [];
            _.forEach(this.faculties, (function(faculty){
                    response.push(faculty.university);
            }));

            response = _.map(response, _.method('toUpperCase'));
            response = _.uniq(response).sort();
            response = _.compact(response);
            return response;
        },

        FindFacultiesByField(field_selected) {
            var faculties = [];
            _.forEach(this.faculties, (function(faculty) {
                if (_.includes(faculty.fields, field_selected.toLowerCase())) {
                    faculties.push(faculty);
                }
                }));
            faculties = _.uniq(_.flatten(faculties)).sort();

            return faculties;
        },

        Filter(){
            var self = this;
            var response = [];
            if (this.university_selected == '' && this.field_selected == ''){
                this.computed_faculties = this.faculties;
            } 
            else if (this.university_selected == '' && this.field_selected != ''){
                this.computed_faculties = this.FindFacultiesByField(this.field_selected);
            }
            else if(this.field_selected == '' && this.university_selected != '' ){
                response = _.filter(this.faculties, function(faculty) {
                if (faculty.university.toUpperCase() == self.university_selected){
                    return faculty;
                }
                });
                this.computed_faculties = response;
            } 
            else {
                var response = [];
                var faculties = this.FindFacultiesByField(this.field_selected);
                _.forEach(faculties, (function(faculty){
                    if (faculty.university.toUpperCase() == self.university_selected){
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
    #46B6AC;
}

.filter-wrapper {
  margin: 12px;
}
</style>



