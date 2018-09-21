<template>

<div>
    <div>
    <br/>
    <br/>
    <div class="mdl-layout__title">
        <div class="mdl-layout">
            <div> 
                <strong>Formation: </strong> {{FindCourse().name}}
            </div>
            <hr/>
        </div>
    </div>
    </div>

    <div class="mdl-grid">
        <div class="mdl-cell--12-col mdl-cell--12-col-tablet mdl-cell--12-col-phone">
                <br/><br/>
                 <div>Description : {{FindCourse().description}}
                </div>
                <hr/>
                 <div>Diplome requis : {{FindCourse().prerequisite}}
                </div>
                <hr/>
                <div> Durée des études : {{FindCourse().yearsofstudy}} 
                </div>
                <hr/>
                <div>
                    <span>Métiers</span>
                    <ul v-for="role in FindCourse().professions" :key=role>
                        <li>{{role}}</li>
                    </ul>
                </div> 
                <hr/>
                <div>
                    <span>Domaines d'étude</span>
                    <ul v-for="field in FindCourse().fields" :key=field>
                        <li>{{field}}</li>
                    </ul>
                </div>
                <hr/>
        </div>
    </div>
</div>
</template>

<script>

import { mapState } from 'vuex'


export default {
    created () {
        this.$store.dispatch('courses/getAllCourses')
    },

    computed: mapState({
        courses: state => state.courses.all
    }),

    methods: {
        FindCourse() {
            var self = this;
            var response = {};
            _.forEach(this.courses, function(course) {
                if (course.name == self.$route.params.course_name){
                    response = course;
                }
            });
            return response;
        }
    }
}
</script>


<style scoped>

</style>

