<template>
  <nuxt-link :to="`/lessons/${lesson.id}/`" tag="div">
    <div class="card lesson-card">
      <div class="card-body">
        <h5 class="card-title">
          {{ lesson.title }}
        </h5>
        <p class="card-info">
          {{ lesson.info }}
        </p>
      </div>
    </div>
  </nuxt-link>
</template>
<script>
export default {
  props: ['lesson', 'onDelete']
}
</script>
<style>
.lesson-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    height: auto;
    min-height: 13em;
    padding: 25px 18px;
    margin-bottom: 40px;
    background-color: #fff;
    border-radius: 16px;
    text-align: center;
    cursor: pointer;
    transition: .4s;
    align-self: stretch;
}
.card-body {
  display: flex;
  justify-content: space-between;
  flex-direction: column;
}
.card-title {
  font-size: 19px;
  font-weight: 500;
  line-height: 1.44;
  letter-spacing: 1.6px;
  text-align: center;
  color: #3c3a3a;
}
.card-info {
  font-size: 13px;
  letter-spacing: .8px;
  color: #666;
  margin-top: 8px;
}
</style>
