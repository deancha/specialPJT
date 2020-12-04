<template>
  <div id="oopss">
    <div id="error-text">
      <img
        src="https://cdn.rawgit.com/ahmedhosna95/upload/1731955f/sad404.svg"
        alt="500"
      />
      <h3>
        <strong>오류가 발생했습니다</strong>
      </h3>
      <h4>{{ msg }}</h4>
    </div>
  </div>
</template>

<script>
export default {
  name: "Error",
  created() {
    this.msg = this.$route.params.msg;
  },
  data() {
    return {
      msg: "",
    };
  },
};
</script>  

<style>
#error-text {
  text-align: center;
}
</style>