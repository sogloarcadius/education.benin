<template>
<div>
    <br/>
    <br/>
    <div class="mdl-layout__title">
        <div class="mdl-layout">
            <div> 
                <strong>Nom de l'établissement : </strong> {{FindUniversity(this.$route.params.university_id).name}}
            </div>
            <hr/>
                <div> 
                <strong>Adresse : </strong> {{FindUniversity(this.$route.params.university_id).address}}
            </div>
            <hr/>
            <div> 
                <strong>Numéro de Téléphone : </strong> <a :href=' "tel:" + FindUniversity(this.$route.params.university_id).phone' target="_blank"> {{FindUniversity(this.$route.params.university_id).phone}}</a><br/>
            </div>
            <hr/>
            <div> 
                <strong>Email : </strong> <a :href=' "mailto:" + FindUniversity(this.$route.params.university_id).email' target="_blank">{{FindUniversity(this.$route.params.university_id).email}}</a><br/>
            </div>
            <hr/>
            <div> 
                <strong>Site Internet : </strong> <a :href=FindUniversity(this.$route.params.university_id).url target="_blank">{{FindUniversity(this.$route.params.university_id).url}}</a><br/>
            </div>
            <hr/>
            <div v-if="FindFaculties(this.$route.params.university_id).length > 0"> 
                <strong>Nombre de Facultés : </strong> {{FindFaculties(this.$route.params.university_id).length}}
            </div>
            <hr v-if="FindFaculties(this.$route.params.university_id).length > 0"/>
            <div> 
                <strong>Nombre de Formations : </strong> {{FindCourses(this.$route.params.university_id).length}}<br/>
            </div>
            <hr/>
        </div>
    </div>
    <div class="mdl-grid">
        <div class="mdl-cell--6-col mdl-cell--6-col-tablet mdl-cell--6-col-phone" v-if="FindFaculties(this.$route.params.university_id).length > 0">
            <br/><br/>               
            <div>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span><strong>FACULTES</strong></span>
                <faculty :faculties="FindFaculties(this.$route.params.university_id)"></faculty>
            </div> 
        </div>
        <div class="mdl-cell--6-col mdl-cell--6-col-tablet mdl-cell--6-col-phone">
            <br/><br/>
            <div>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span><strong>FORMATIONS</strong></span>
                <formation :courses="FindCourses(this.$route.params.university_id)" :faculties="FindFaculties(this.$route.params.university_id)"></formation>
            </div> 
      
        </div>
    </div>
    
</div>
</template>

<script>

import formation from '@/components/Formation'
import faculty from '@/components/Faculty'

import { mapState } from 'vuex'


export default {
    components: { formation, faculty },

    created () {
        this.$store.dispatch('universities/getAllUniversities'),
        this.$store.dispatch('faculties/getAllFaculties'),
        this.$store.dispatch('courses/getAllCourses')
    },

    computed: mapState({
        universities: state => state.universities.all,
        faculties: state => state.faculties.all,
        courses: state => state.courses.all
    }),
    methods: {
        FindUniversity(id){
            var response = "";
            _.forEach(this.universities, (function(university){
                if (university.name == id) {
                    response = university;
                }
            }));

            return response;
        },
        FindFaculties(id) {
            var faculties = [];
            _.forEach(this.faculties, (function(faculty) {
                    if (faculty.university == id) {
                        faculties.push(faculty);
                    }
                }));

            faculties = _.uniq(faculties);
            faculties = _.sortBy(faculties, o => o.name);

            return faculties;
        },
        
        FindCourses(id) {
            var response = [];
            response = _.filter(this.courses, function(course) {
                return course.university == id;
            });

            return response;
        }
    }
}
</script>


<style scoped>

.center-items {
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

