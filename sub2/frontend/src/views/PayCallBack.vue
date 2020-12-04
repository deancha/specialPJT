<template>
  <div style="margin: 50px 20px">
    <div class="mt-5 pt-5 row justify-content-center">
      <h3 class="text-center col-12">결제가 완료되었습니다!</h3>
      <div class="col-lg-6 col-md-9 p-5 bg-light">
        <h3 class="text-center my-5">주문자 정보</h3>
        <div v-if="order" class="order">
          <div class="my-3 row">
            <div class="h5 col-6">주문번호</div>
            <div class="h6 col-6 text-right">{{ order.tid }}</div>
          </div>
          <div class="my-3 row">
            <div class="h5 col-6">상품명</div>
            <div class="h6 col-6 text-right">{{ order.item_name }}</div>
          </div>
          <div class="my-3 row">
            <div class="h5 col-6">결제금액</div>
            <div class="h6 col-6 text-right">
              {{ order.amount.total.toLocaleString() }}원
            </div>
          </div>
          <div class="my-3 row">
            <div class="h5 col-6">결제승인시각</div>
            <div class="h6 col-6 text-right">{{ created_at }}</div>
          </div>
        </div>
        <div class="mt-5 pt-3 text-center">
          <a href="/" class="primary-btn">메인으로 돌아가기</a>
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
    return {
      order: null,
      created_at: null,
      tid: null,
    };
  },
  created() {
    axios
      .get(
        process.env.VUE_APP_API_URL +
          "pay/approval/?pg_token=" +
          this.$route.query.pg_token +
          "&tid=" +
          this.$cookie.get("tid")
      )
      .then(({ data }) => {
        this.order = data;
        this.created_at = data.created_at;
        this.tid = data.tid;

        axios
          .post(process.env.VUE_APP_API_URL + "order/", {
            tid: this.tid,
            order: this.$cookie.get("order"),
            kakaoemail: this.$cookie.get("emails"),
            address: this.$cookie.get("address"),
            uniqueness: this.$cookie.get("uniqueness"),
            phonenumber: this.$cookie.get("phonenumber"),
            created_at: this.created_at,
            username: this.$cookie.get("username"),
          })
          .then(({ data }) => {
            this.$cookie.delete("tid");
            this.$cookie.delete("order");
            this.$cookie.delete("emails");
            this.$cookie.delete("address");
            this.$cookie.delete("uniqueness");
            this.$cookie.delete("phonenumber");
            this.$cookie.delete("username");
          });
      })
      .catch((data) => {
        this.$router.push("/500/결제중 문제가 발생했습니다.");
        this.$cookie.delete("tid");
        this.$cookie.delete("order");
        this.$cookie.delete("email");
        this.$cookie.delete("address");
        this.$cookie.delete("uniqueness");
        this.$cookie.delete("phonenumber");
        this.$cookie.delete("username");
      });
  },
  mounted() {},
  methods: {},
};
</script>

<style scoped>
.order {
  word-break: break-all;
}
</style>
