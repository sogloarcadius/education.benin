
<script>
export default {
  state: {
		universities: null,
		faculties: null,
		courses: null
  },
  load(){
  	var self = this
  	$.ajax({
  		url: 'src/store/universities.json',
      cache: false,
  		complete(data) {
  			self.state.universities = JSON.parse(data.responseText);
  		}
		}),
		
		$.ajax({
			url: 'src/store/faculties.json',
			cache: false,
			complete(data) {
				self.state.faculties = JSON.parse(data.responseText);
			}
		}),

		$.ajax({
			url: 'src/store/courses.json',
			cache: false,
			complete(data) {
				self.state.courses = JSON.parse(data.responseText);
			}
		})


  }
}
</script>
