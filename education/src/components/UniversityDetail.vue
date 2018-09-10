<template>

    <div>
    <div class="mdl-grid center-items">
        <div class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone">
                <strong>Name : </strong> {{this.$route.params.university.name}} <br/>
                <strong>Licence : </strong> {{this.$route.params.university.type}} <br/>
                <strong>Phone : </strong> {{this.$route.params.university.phone}}<br/>
                <strong>Address: </strong> {{this.$route.params.university.address}}<br/>
                <strong>Website: </strong> {{this.$route.params.university.url}}<br/>
                <strong>Formations: </strong> {{FindCourses(this.$route.params.university.id).length}}<br/>
                <strong>Faculties: </strong> {{FindFaculties(this.$route.params.university.id).length}}
        </div>
    </div>
    <div class="mdl-grid">
        <div v-for="course in FindCourses(this.$route.params.university.id)" class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone university-card mdl-card mdl-shadow--2dp">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">{{course.name}}</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Name : </strong> {{course.name}} <br/>
                <strong>description : </strong> {{course.description}} <br/>
                <strong>prerequisite : </strong> {{course.prerequisite}}<br/>
                <strong>yearsofstudy: </strong> {{course.yearsofstudy}}<br/>
            </div>
        </div>
      </div>
    </div>
</template>

<script>
import store from '@/components/Store'

export default {
    data(){
        return {
            universities: store.state.universities,
            faculties: store.state.faculties,
            courses: store.state.courses
        }
    },
    methods: {
        FindFaculties(id) {

            var faculties = [];
            _.forEach(store.state.faculties, (function(university) {
                    if (university.id == id) {
                        faculties.push(university.faculties);
                    }
                }));
            
            faculties = _.uniq(_.flatten(faculties)).sort();

            return faculties;
        },

        FindCourses(id) {
            var response = [];
            response = _.filter(store.state.courses, function(course) {
                return course.university == id;
            });

            return response;
        }
    }
}
</script>


<style scoped>

.mdl-grid.center-items {
  justify-content: center;
}


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

</style>

