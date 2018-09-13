<template>

    <div>
    <div class="mdl-grid center-items">
        <div class="mdl-cell--3-col mdl-cell--2-col-tablet mdl-cell--1-col-phone">
                <strong>Name : </strong> {{FindUniversity(this.$route.params.university_id).name}} <br/>
                <strong>Licence : </strong> {{FindUniversity(this.$route.params.university_id).type}} <br/>
                <strong>Phone : </strong> {{FindUniversity(this.$route.params.university_id).phone}}<br/>
                <strong>Address: </strong> {{FindUniversity(this.$route.params.university_id).address}}<br/>
                <strong>Website: </strong> {{FindUniversity(this.$route.params.university_id).url}}<br/>
                <strong>Formations: </strong> {{FindCourses(this.$route.params.university_id).length}}<br/>
                <strong>Faculties: </strong> {{FindFaculties(this.$route.params.university_id).length}}
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
        FindUniversity(id){
            var response = "";
            _.forEach(store.state.universities, (function(university){
                if (university.id == id) {
                    response = university;
                }
            }));

            return response;
        },
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

