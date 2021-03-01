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
          <h2>Change Status</h2>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
              
              <form @submit="onSubmit">

                <div class="form-group row">
                  <label for="options1" class="col-sm-2 col-form-label">Status</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Active" name="options1" class="form-control" v-model.trim="form.status">
                  </div>
                </div>

                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" variant="success">Change status</b-button>
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
      activity: this.$route.params.activityId,
      form: {
        status: '',
      },
    }
  },
  methods: {

    getActivity () {
      const path = `http://0.0.0.0:8000/activities/${this.activity}/`

      axios.get(path).then((response) => {
        this.form.status = response.data.status
      })
      .catch((error) => {
        console.log(this.form)
      })
    },

    onSubmit (evt) {

      evt.preventDefault()
      
      const path = `http://0.0.0.0:8000/activities/${this.activity}/cancel/`
      
      axios.put(path, this.form).then((response) => {
        this.form.status = response.data.status
        swal("Cancel succesfull!", "", "success")
      })
      .catch((error) => {
        console.log(error)
        swal("Ooops!", "A problem ocurrs", "error")
      })
    },
  },

  created() {
    this.getActivity()
  },
}
</script>

<style lang="css" scoped>
</style>