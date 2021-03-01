import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ListActivities',
      component: () => import('@/components/Activities/ListActivities.vue')
    },
    {
      path: '/:propertyId/create',
      name: 'CreateActivity',
      component: () => import('@/components/Activities/CreateActivity.vue')
    },
    {
      path: '/:activityId/status',
      name: 'ChangeStatus',
      component: () => import('@/components/Activities/ChangeStatus.vue')
    },
  ],
  mode: 'history',
})
