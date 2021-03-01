<template lang="html">
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item href="/">Activities</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2>Today Activities</h2>

          <div class="col-md-12">
            <div class="overflow-auto">
              <b-pagination
                v-model="currentPage"
                :total-rows="rows"
                :per-page="perPage"
                aria-controls="my-table"
              ></b-pagination>
            </div>
            <p class="mt-3">Página: {{ currentPage }}</p>

            <b-table striped hover :items="activities" :fields="fields">
              <template v-slot:cell(property)="row">
                <p>{{row.item.property.title}}</p>
              </template>
              <template v-slot:cell(title)="row">
                <p>{{row.item.title}}</p>
              </template>
              <template v-slot:cell(schedule)="row">
                <p>{{row.item.schedule}}</p>
              </template>
              <template v-slot:cell(status)="row">
                <p>{{row.item.status}}</p>
              </template>
            </b-table>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      perPage: 5,
      currentPage: 1,
      fields: [
        { key: 'property', label: 'Property'},
        { key: 'title', label: 'Title'},
        { key: 'schedule', label: 'Schedule'},
        { key: 'status', label: 'Status'},
      ],
      activities: [],
    }
  },
  methods: {

    getActivities () {
      const path = `http://0.0.0.0:8000/current_activities/`
      axios.get(path).then((response) => {
        this.activities = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    rows() {
      return this.activities.length
    }
  },
  created(){
    this.getActivities()
  }
}
</script>

<style lang="css" scoped>
</style>