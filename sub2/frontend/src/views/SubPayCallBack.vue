<template>
  <div>
    <div class="mt-5 pt-5 row justify-content-center">
      <h2 class="text-center my-5 col-12">결제가 완료되었습니다!</h2>
      <div class="col-4 p-5 bg-light">
        <h3 class="text-center my-5">주문자 정보</h3>
        <div>
          <div class="my-3 row">
            <div class="h5 col-6">상품명</div>
            <div class="h6 col-6 text-right">정기구독</div>
          </div>
          <div class="my-3 row">
            <div class="h5 col-6">결제금액</div>
            <div class="h6 col-6 text-right">19900원</div>
          </div>
        </div>
        <div class="mt-5 pt-3 text-center">
          <a href="/" class="btn btn-warning">메인으로 돌아가기</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {};
  },
  created() {
    axios
      .get(
        process.env.VUE_APP_API_URL +
          "pay/subscriptionapproval/?pg_token=" +
          this.$route.query.pg_token +
          "&tid=" +
          this.$cookie.get("subtid")
      )
      .then(({ data }) => {
        axios
          .post(process.env.VUE_APP_API_URL + "subscription/ ", {
            kakaoemail: this.$cookie.get("emails"),
            address: this.$cookie.get("address"),
            continuemonth: "1",
          })
          .then(({ data }) => {
            this.$cookie.delete("emails");
            this.$cookie.delete("address");
            this.$cookie.delete("subtid");
          });
      });
  },
  mounted() {},
  methods: {},
};
</script>

<style scoped></style>
