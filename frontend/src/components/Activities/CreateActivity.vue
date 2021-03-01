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
          <h2>Create Menu</h2>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
              
              <form @submit="onSubmit">

                <div class="form-group row">
                  <label for="day" class="col-sm-2 col-form-label">Day/Time</label>
                  <div class="col-sm-6">
                    <input type="datetime-local" name="day" class="form-control" v-model.trim="form.schedule">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="options0" class="col-sm-2 col-form-label">Title</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Activity 1" name="options0" class="form-control" v-model.trim="form.title">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="options1" class="col-sm-2 col-form-label">Status</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Active" name="options1" class="form-control" v-model.trim="form.status">
                  </div>
                </div>

                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" variant="success">Create</b-button>
                  </div>
                </div>

              </form>

            </div>
          </div>
        </div>
      </div>
    
    </div>

  </div>
</template>

<script>

import axios from 'axios';
import swal from 'sweetalert';

export default {
  data () {
    return {
      form: {
        property: Number(this.$route.params.propertyId),
        schedule: '',
        title: '',
        status: '',
      },
    }
  },
  methods: {

    onSubmit (evt) {

      evt.preventDefault()
      
      const path = `http://0.0.0.0:8000/activities/`
      
      axios.post(path, this.form).then((response) => {
        this.form.property = response.data.property
        this.form.schedule = response.data.schedule
        this.form.title = response.data.title
        this.form.status = response.data.status
        swal("Menu creation succesfull!", "", "success")
      })
      .catch((error) => {
        console.log(error)
        swal("Ooops!", "A problem ocurrs", "error")
      })
    },
  },
}
</script>

<style lang="css" scoped>
</style>