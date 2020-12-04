<template>
  <div style="margin: 70px auto; text-align: center">
    <h3 style="margin-bottom: 50px">{{ msg }}</h3>
    <a class="primary-btn" href="/"> 메인으로 돌아가기 </a>
  </div>
</template>

<script>
export default {
  components: {},
  data: () => ({
    msg: "카카오 로그인 진행 중입니다.",
    isPossible: false,
    gender: "",
    drinkWith: "",
    percent: "",
    taste: [],
  }),
  computed: {},
  created() {
    this.getToken();
  },
  methods: {
    getToken() {
      if (this.$route.query.email) {
        if (this.$route.query.name)
          this.$cookie.set("name", this.$route.query.name);
        this.$cookie.set("email", this.$route.query.email);
        if (this.$route.query.userimg)
          this.$cookie.set("userimg", this.$route.query.userimg);
        this.$store.commit("login", {
          name: this.$route.query.name,
          email: this.$route.query.email,
          userimg: this.$route.query.userimg,
        });
        this.$router.push("/");
      } else {
        this.msg = "카카오 로그인 중 문제가 발생했습니다.";
      }
      // this.$store.commit("login", { name: "김수민", email: "aa" });
      // this.$cookie.set("token", "aa", {
      //   expires: "8h",
      // });
      // {"userimg": "http://k.kakaocdn.net/dn/cKFQpO/btqHiM0czN6/ks8kEIqn13N1rRGNw7BQ91/img_640x640.jpg",
      //"name": "\uae40\uc218\ubbfc",
      //"email": "rlatnals0805@kakao.com",
      //"age_range": "20~29"}
      // axios
      //   .get(
      //     process.env.VUE_APP_API_URL +
      //       "account/login/kakao/callback?code=" +
      //       this.$route.query.code
      //   )
      //   .then(({ data }) => {
      //     if (!data.age_range) {
      //       this.msg =
      //         "성인 인증이 필요한 서비스입니다. 반드시 연령대를 체크해주세요.";
      //       this.isPossible = true;
      //     } else if (data.age_range.split("~")[0] < 20) {
      //       this.msg = "성인만 로그인할 수 있습니다.";
      //     } else {
      //       this.$cookie.set("token", this.$route.query.code, {
      //         expires: "8h",
      //       });
      //       this.$store.commit("login", data);
      //       this.$router.push("/");
      //     }
      //   })
      //   .catch((data) => {
      //     this.msg = "카카오 로그인 중 문제가 발생했습니다.";
      //   });
    },
  },
};
</script>
<style lang="scss" scoped>
.price {
  margin: 10px 0px 20px 0px;
}
.tab-item-content {
  width: 98%;
  margin: 0 auto;
}
.content-btn {
  color: #808080;
  font-size: 30px;
  border: none;
  background: none;
  width: 80%;
  margin: 0 auto;
  border-bottom: 1px solid #cacaca;
}
input {
  width: auto;
  height: auto;
  margin: 0 3px 0px 10px;
}
.survey-form {
  border-radius: 30px;
  border: 2px solid #ffbbd6;
  box-shadow: 7px 11px 10px 0px #ecd4dd;
  padding: 30px;
  label {
    display: block;
    font-size: 13pt;
    font-weight: 600;
    margin-bottom: 10px;
    font-family: "JSDongkang-Bold";
  }
  select {
    border: 1px solid black;
    -webkit-appearance: auto;
  }
  .list {
    margin-bottom: 40px;
  }
}
.checkout-section {
  padding-top: 20px;
  padding-bottom: 80px;
}
</style>
