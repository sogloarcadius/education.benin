<template>
  <div>
    <div>
    <br/>
     <div class="mdl-grid filter-wrapper">
          <span class="mdl-cell--12-col">
             <div class="filter-wrapper-options mdl-selectfield mdl-js-selectfield mdl-selectfield--floating-label">
                
                <label class="mdl-selectfield__label" for="fields">Domaine</label>
                <select v-model="field_selected" class="mdl-selectfield__select" id="field" name="field">
                  <option v-on:click="Filter()"></option>
                  <option v-for='field in ListOfFields()' :key=field v-on:click="Filter()">{{field}}</option>
                </select>
                &nbsp;

                <label class="mdl-selectfield__label" for="university">Université</label>
                <select class="mdl-selectfield__select" id="university" name="university">
                  <option v-on:click="Filter()">{{this.$route.params.university_id.toUpperCase()}}</option>
                </select>
                &nbsp;

                <span v-if="faculties.length > 0">
                    <label class="mdl-selectfield__label" for="faculty">Faculté</label>
                    <select v-model="faculty_selected" class="mdl-selectfield__select" id="faculty" name="faculty">
                        <option v-on:click="Filter()"></option>
                        <option v-for='faculty in faculties' :key=faculty.id v-on:click="Filter()">{{faculty.id.toUpperCase()}}</option>
                    </select>
                </span>
              </div>
          </span>
     </div>
    </div>
    
    <div class="mdl-grid">
        <div v-if="courses" v-for="course in courses" :key=course.name class="mdl-cell--12-col university-card mdl-card mdl-shadow--2dp" @click="displayFormationDetail(course.name)">
                <div class="mdl-card__title mdl-card--expand">
                    <h2 class="mdl-card__title-text">{{course.name}}</h2>
                </div>
                <div class="mdl-card__supporting-text">
                    <strong>Description : </strong> {{course.description}} <br/>
                    <strong>Prérequis : </strong> {{course.prerequisite}} <br/>
                    <strong>Année d'étude : </strong> {{course.yearsofstudy}}<br/>
                </div>
                <div class="mdl-card__actions mdl-card--border">
                    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                    Voir
                    </a>
                </div>
        </div>
         
    </div>
  </div>
</template>

<script>
export default {
  data(){
      return {
          faculty_selected: '', 
          field_selected: ''
      }
  },
  props: ['courses', 'faculties'],
  methods: {
    displayFormationDetail (course_name) {
      this.$router.push({ name: 'course_detail', params: { course_name: course_name } })
    },
    ListOfFields(){
        var response = [];
        _.forEach(this.courses, (function(course){
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
  color: #fff;
  background:
    #46B6AC;
}

.filter-wrapper {
  margin: 12px;
}
</style>



