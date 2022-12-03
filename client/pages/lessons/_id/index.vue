<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">
          {{ lesson.title }}
        </h2>
      </div>
      <div class="col-md-6">
        <div class="lesson-details">
          <p><br></br></p>
          <p class="string">
            {{ lesson.detail }}
          </p>
          <p><br></br><br></br></p>
          <section id="app" class="button">
            <nuxt-link v-if="lesson.id > 1" :to="`/lessons/${(lesson.id-1)}`" tag="a" class="btn_10">
              <span>&lt;</span>
            </nuxt-link>
            <nuxt-link :to="`/lessons/`" tag="a" class="btn_10">
              <span>レッスン一覧</span>
            </nuxt-link>
            <nuxt-link v-if="lesson.id < 10" :to="`/lessons/${(lesson.id+1)}`" tag="a" class="btn_10">
              <span>&gt;</span>
            </nuxt-link>
          </section>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head () {
    return {
      title: 'lesson'
    }
  },
  data () {
    return {
      lesson: {
        title: '',
        info: '',
        detail: ''
      }
    }
  },
  async asyncData ({ $axios, params }) {
    try {
      const lesson = await $axios.$get(`/lessons/${params.id}`)
      return { lesson }
    } catch (e) {
      return { lesson: [] }
    }
  }
}
</script>
<style scoped>

p {
  -webkit-font-smoothing: antialiased;
  font-size: 18px;
}
.lesson-details {
  white-space: pre-line;
  font-size: 16px;
  font-weight: 400;
  letter-spacing: .4px;
  color: #333;
}

.string {
  line-height: 2.0;
}

.row {
  justify-content: center;
}

.col-md-6 {
    flex: 0 0 90%;
    max-width: 90%;
}

.button {
  max-width: 100%;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
a.btn_10 {
  color: #1B1B1B;
  text-decoration: none;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 33%;
  height: 50px;
  box-sizing: border-box;
  background: #fff;
  position: relative;
}
a.btn_10:hover {
  cursor: pointer;
  text-decoration: none;
}
a.btn_10::after {
  position: absolute;
  bottom: -4px;
  left: 0;
  content: '';
  width: 100%;
  height: 2px;
  background: #333;
  transform: scale(0.3, 0.8);
  transform-origin: center top;
  transition: transform .3s;
}
a.btn_10:hover::after {
  transform: scale(0.5, 1);
}

</style>
