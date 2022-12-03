<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4" style="margin-bottom: 1.5rem !important;">
        <div class="d-flex justify-content-between">
          <h3>レッスン一覧</h3>
        </div>
      </div>
      <template v-for="lesson in lessons">
        <div :key="lesson.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <lesson-card :onDelete="deleteLesson" :lesson="lesson"></lesson-card>
        </div>
      </template>
    </div>
  </main>
</template>
<script>

import LessonCard from '~/components/LessonCard.vue'

export default {
  head () {
    return {
      title: 'lessons list'
    }
  },
  components: {
    LessonCard
  },
  data () {
    return {
      lessons: []
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const lessons = await $axios.$get(`/lessons/`)
      return { lessons }
    } catch (e) {
      return { lessons: [] }
    }
  },
  methods: {
    async deleteLesson (lesson_id) { // eslint-disable-line
      try {
        await this.$axios.$delete(`/lessons/${lesson_id}/`) // eslint-disable-line
        const newLessons = await this.$axios.$get('/lessons/')
        this.lessons = newLessons
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
<style scoped>
</style>
