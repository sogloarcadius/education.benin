<style>

div#app {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
}

div#app .wrapper {
  display: flex;
  max-width: 444px;
  flex-wrap: wrap;
  padding-top: 12px;
}
div#app .card {
  box-shadow: rgba(0, 0, 0, 0.117647) 0px 1px 6px, rgba(0, 0, 0, 0.117647) 0px 1px 4px;
  max-width: 124px;
  margin: 12px;
  transition: .15s all ease-in-out;
}

div#app .card:hover {
  transform: scale(1.1);
}
div#app .card a {
  text-decoration: none;
  padding: 12px;
  color: #03A9F4;
  font-size: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

div#app .card a img {
  height: 100px;
}

div#app .card a small {
  font-size: 10px;
  padding: 4px;
}

/* Style the buttons */
.btn {
  border: none;
  outline: none;
  padding: 12px 16px;
  background-color: #f1f1f1;
  cursor: pointer;
}

/* Add a light grey background on mouse-over */
.btn:hover {
  background-color: #ddd;
}

/* Add a dark background to the active button */
.btn.active {
  background-color: #666;
  color: white;
}

</style>

<template>	
	<div>
		<div id='app' class="wrapper">
			<div class="card" v-for="univ in universities">
				<a v-bind:href="univ.path" target="_blank">
					<img v-bind:src="'/filter_list.svg'"/>
					<small>{{univ.title}}</small>
				</a>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {};
	}, 
	computed:{
		universities() {
			let universities = this.$site.pages.filter(p => {
				return p.frontmatter.univ;
			});

			return universities;
		}
  },
  
}
</script>
