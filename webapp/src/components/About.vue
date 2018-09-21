<template>
<div>
  <div class="mdl-cell mdl-cell--12-col mdl-card mdl-shadow--1dp">
     <span class="mdl-layout__title">
        <br/>
        <div class="education-logo"></div>
        <span class="mdl-layout__title">edubenin.bj</span>
        <br/>
        <span class="mdl-layout__title">La plateforme qui simplifie la vie des étudiant(e)s béninois(es).</span>
        <br/>
     </span>
    <div class="mdl-grid">
        <div class="university-card mdl-card mdl-shadow--2dp" @click="Redirect('university')">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">UNIVERSITES</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Liste des universités </strong>
            </div>
            <div class="mdl-card__actions mdl-card--border">
            <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                Voir
            </a>
            </div>
        </div>

        <div class="university-card mdl-card mdl-shadow--2dp" @click="Redirect('faculty')">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">FACULTES</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Liste des facultés </strong>
            </div>
            <div class="mdl-card__actions mdl-card--border">
            <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                Voir
            </a>
            </div>
        </div>

        <div class=" university-card mdl-card mdl-shadow--2dp" @click="Redirect('course')">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">FORMATION</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Rechercher une formation</strong>
            </div>
            <div class="mdl-card__actions mdl-card--border">
            <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                Voir
            </a>
            </div>
        </div>

        <div class=" university-card mdl-card mdl-shadow--2dp" @click="Redirect('company')">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">ENTREPRISES</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Rechercher une entreprise</strong>
            </div>
            <div class="mdl-card__actions mdl-card--border">
            <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                Voir
            </a>
            </div>
        </div>

         <div class=" university-card mdl-card mdl-shadow--2dp" @click="Redirect('jobs')">
            <div class="mdl-card__title mdl-card--expand">
                <h2 class="mdl-card__title-text">EMPLOI</h2>
            </div>
            <div class="mdl-card__supporting-text">
                <strong>Rechercher un emploi</strong>
            </div>
            <div class="mdl-card__actions mdl-card--border">
            <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                Voir
            </a>
            </div>
        </div>
      </div>
  </div>
</div>
</template>

<script>
export default {
    methods: {
        Redirect (endpoint) {
            this.$router.push({ name: endpoint})
        }
    }
};
</script>

<style scoped>
hr {
  margin: 5px;
}

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
  background: #46B6AC;
}
</style>