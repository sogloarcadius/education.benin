
<script>
export default {
  state: {
    colleges: null
  },
  load(){
  	var self = this
  	$.ajax({
  		url: 'src/store/colleges.json',
      cache: false,
  		complete(data) {
  			self.state.colleges = JSON.parse(data.responseText);
  		}
  	})
  }
}
</script>
