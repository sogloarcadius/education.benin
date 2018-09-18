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
        <div v-if="courses" v-for="course in computed_courses" :key=course.name class="mdl-cell--12-col university-card mdl-card mdl-shadow--2dp" @click="displayFormationDetail(course.name)">
                <div class="mdl-card__title mdl-card--expand">
                    <h2 class="mdl-card__title-text">{{course.name}}</h2>
                </div>
                <div class="mdl-card__supporting-text">
                    <strong>UFR : </strong> {{course.college.toUpperCase()}}<br/>
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

    props: ['courses', 'faculties'],

    data(){
        return {
            faculty_selected: '', 
            field_selected: '',
            computed_courses: this.courses
        }
    },

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
            response = _.uniq(response).sort();
            response = _.compact(response);

            return response;
        },

        FindCoursesByField(field_selected) {
            var courses = [];
            _.forEach(this.courses, (function(course) {
                if (_.includes(course.fields, field_selected.toLowerCase())) {
                    courses.push(course);
                }
                }));
            courses = _.uniq(_.flatten(courses)).sort();

            return courses;
        },
        
        Filter(){
            var self = this;
            var response = [];
            if (this.faculty_selected == '' && this.field_selected == ''){
                this.computed_courses = this.courses;
            } 
            else if (this.faculty_selected == '' && this.field_selected != ''){
                this.computed_courses = this.FindCoursesByField(this.field_selected);
            }
            else if(this.field_selected == '' && this.faculty_selected != '' ){
                response = _.filter(this.courses, function(course) {
                if (course.college.toUpperCase() == self.faculty_selected){
                    return faculty;
                }
                });
                this.computed_courses = response;
            } 
            else {
                var response = [];
                var courses = this.FindCoursesByField(this.field_selected);
                _.forEach(courses, (function(course){
                    if (course.college.toUpperCase() == self.faculty_selected){
                        response.push(course);
                    }
                }));         
                this.computed_courses = response;
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



